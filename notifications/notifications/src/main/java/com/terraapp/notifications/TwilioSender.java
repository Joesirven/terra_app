package com.terraapp.notifications;

import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

public class TwilioSender {
    private final TwilioConfig twilioConfig;

    public TwilioSender(TwilioConfig twilioConfig) {
        this.twilioConfig = twilioConfig;
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
