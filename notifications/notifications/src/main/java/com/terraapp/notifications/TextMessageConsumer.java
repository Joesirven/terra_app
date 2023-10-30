package com.terraapp.notifications;

import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.errors.WakeupException;
import org.apache.kafka.common.serialization.StringDeserializer;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

public class TextMessageConsumer {
    private final Consumer<String, String> consumer;
    private final TwilioSender twilioSender;
    private static volatile boolean running = true;

    private final ObjectMapper objectMapper = new ObjectMapper();

    public TextMessageConsumer() {
        // Create Twilio configuration
        TwilioConfig twilioConfig = new TwilioConfig();
        this.twilioSender = new TwilioSender(twilioConfig);

        // Configure Kafka consumer
        Properties properties = new Properties();
        properties.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.put(ConsumerConfig.GROUP_ID_CONFIG, "terra-notification-sms");
        properties.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

        this.consumer = new KafkaConsumer<>(properties);

        // Subscribe to topic
        consumer.subscribe(Collections.singleton("terra-notification-sms"));
    }

    public void start() {
        try {
            while (running) {
                System.out.println("running in start()");
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));

                records.forEach(record -> {
                    System.out.printf("Received record with key %s and value %s%n", record.key(), record.value());

                    try {
                        JsonNode jsonNode = objectMapper.readTree(record.value());
                        String phoneNumber = jsonNode.get("phoneNumber").asText();
                        String message = jsonNode.get("message").asText();

                        // Validate phoneNumber and message before sending
                        if (isValidPhoneNumber(phoneNumber) && isValidMessage(message)) {
                            System.out.println("Received phone number: " + phoneNumber);
                            System.out.println("Received message: " + message);
                            System.out.println("if state before sendMessage()");

                            twilioSender.sendMessage(phoneNumber, message);
                            System.out.println("if state after sendMessage()");
                        } else {
                            System.out.println("Invalid phone number or message");
                        }
                    } catch (Exception e) {
                        System.out.println("Failed to parse record value: " + e.getMessage());
                    }
                });
            }
        } catch (WakeupException e) {
            if (running) {
                throw e;
            }
            System.out.println("Consumer is closing");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        } finally {
            consumer.close();
        }
    }

    // Implement these validation methods as needed
    private boolean isValidPhoneNumber(String phoneNumber) {
        if (phoneNumber == null || phoneNumber.isEmpty()) {
            return false;
        }
        String regex = "^\\+[1-9]\\d{1,14}$";
        return phoneNumber.matches(regex);
    }

    private boolean isValidMessage(String message) {
        if (message == null || message.isEmpty()) {
            return false;
        }

        // Check message length
        if (message.length() > 160) {
            System.out.println("Message is too long");
            return false;
        }

        // Add additional checks as necessary
        return true;
    }
    public void shutdown() {
        running = false;
        consumer.wakeup();
    }
}
