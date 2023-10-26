package org;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;
import java.net.URI;
import java.math.BigDecimal;

import com.twilio.Twilio;
import com.twilio.converter.Promoter;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

public class TextMessageConsumer {
    private final TwilioConfig twilioConfig;

    public TextMessageConsumer() {
        this.twilioConfig = new TwilioConfig();
    }

    public void sendMessage(String toPhoneNumber, String messageBody) {
        Twilio.init("AC793f8989c1045ff4755a0c053d24e09e", "fbc809d084ce06fc3085bd717da52506");

        Message message = Message.creator(
            new PhoneNumber(toPhoneNumber),
            new PhoneNumber("+18669064498"),
            messageBody
        ).create();

        System.out.println("Message sent: " + message.getSid());
    }



    // public TextMessageConsumer(String brokers, String topic, String groupId) {
    //     Properties properties = new Properties();
    //     properties.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, brokers);
    //     properties.put(ConsumerConfig.GROUP_ID_CONFIG, groupId);
    //     properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
    //     properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
    //     this.consumer = new KafkaConsumer<>(properties);
    //     consumer.subscribe(Collections.singletonList(topic));
    // }

    // public void consumeNotifications() {
    //     while (true) {
    //         ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
    //         records.forEach(record -> {
    //             System.out.println("Received notification: " + record.value());
    //             // TODO: Send text message using Twilio here
    //         });
    //     }
    }
