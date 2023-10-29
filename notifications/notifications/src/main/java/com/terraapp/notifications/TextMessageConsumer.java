package com.terraapp.notifications;

import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

public class TextMessageConsumer {
    public static void main(String[] args) {
        // Configure Kafka
        Properties properties = new Properties();
        properties.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.put(ConsumerConfig.GROUP_ID_CONFIG, "terra-notification-sms");
        properties.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

        // Create Kafka consumer
        Consumer<String, String> consumer = new KafkaConsumer<>(properties);

        // Subscribe to topic
        consumer.subscribe(Collections.singleton("terra-notification-sms"));

        // Load Twilio configuration
        TwilioConfig twilioConfig = new TwilioConfig();
        TwilioSender twilioSender = new TwilioSender(twilioConfig);

        // Poll for new data with error handling
        try {
            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));

                records.forEach(record -> {
                    System.out.printf("Received record with key %s and value %s%n", record.key(), record.value());

                    // TODO: Extract phone number and message from record.value() and validate them
                    String phoneNumber = "+1234567890"; // Placeholder value
                    String message = record.value(); // Using the record value directly as the message

                    // Send SMS
                    twilioSender.sendMessage(phoneNumber, message);
                });
            }
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
            consumer.close();
        }
    }
}
