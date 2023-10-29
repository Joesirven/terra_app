package com.terraapp.notifications;

public class TwilioConfig {
    private String accountSid;
    private String authToken;
    private String fromPhoneNumber;

    public TwilioConfig() {
        this.accountSid = System.getenv("TWILIO_ACCOUNT_SID");
        this.authToken = System.getenv("TWILIO_AUTH_TOKEN");
        this.fromPhoneNumber = System.getenv("TWILIO_FROM_PHONE_NUMBER");
    }

    public String getAccountSid() {
        return accountSid;
    }

    public String getAuthToken() {
        return authToken;
    }

    public String getFromPhoneNumber() {
        return fromPhoneNumber;
    }

}
