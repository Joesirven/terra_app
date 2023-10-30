package com.terraapp.notifications;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.


public class Main {
    public static void main(String[] args) {
        System.out.println("Hello and welcome!");
        TextMessageConsumer consumer = new TextMessageConsumer();

        Thread consumerThread = new Thread(consumer::start);
        consumerThread.start();

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("Shutting down consumer...");
            consumer.shutdown();
            try {
                consumerThread.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Shutdown interrupted: " + e.getMessage());
            }
            System.out.println("Consumer shut down successfully");
        }));
    }
}
