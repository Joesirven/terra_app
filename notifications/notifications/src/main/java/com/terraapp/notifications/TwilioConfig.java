package com.terraapp.notifications;

public class TwilioConfig {
    private String accountSid;
    private String authToken;
    private String fromPhoneNumber;

    public TwilioConfig() {
        this.accountSid = System.getenv("TWILIO_ACCOUNT_SID");
        this.authToken = System.getenv("TWILIO_AUTH_TOKEN");
        this.fromPhoneNumber = System.getenv("TWILIO_FROM_PHONE_NUMBER");

        System.out.println(System.getenv());

        System.out.println("Debug - Account SID: " + this.accountSid);
        System.out.println("Debug - Auth Token: " + this.authToken);
        System.out.println("Debug - Phone Number: " + this.fromPhoneNumber);
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
