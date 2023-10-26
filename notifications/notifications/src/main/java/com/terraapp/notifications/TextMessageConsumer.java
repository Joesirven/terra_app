package com.terraapp.notifications;

import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

public class TextMessageConsumer {
    private final TwilioConfig twilioConfig;

    public TextMessageConsumer() {
        this.twilioConfig = new TwilioConfig();

        System.out.println("Twilio account SID: " + twilioConfig.getAccountSid());
        System.out.println("Twilio auth token: " + twilioConfig.getAuthToken());
        System.out.println("Twilio phone number: " + twilioConfig.getFromPhoneNumber());
    }

    public void sendMessage(String toPhoneNumber, String messageBody) {

        Twilio.init(twilioConfig.getAccountSid(), twilioConfig.getAuthToken());

        Message message = Message.creator(
            new PhoneNumber(toPhoneNumber),
            new PhoneNumber(twilioConfig.getFromPhoneNumber()),
            messageBody
        ).create();

        System.out.println("Message sent: " + message.getSid());
    }
}
