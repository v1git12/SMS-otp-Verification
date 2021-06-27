from twilio.rest import Client
import math,random,os
digits="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
OTP=""
for i in range(8):
    OTP+=digits[math.floor(random.random()*62)]
otp = OTP + " is your OTP to verify your identity"
msg= otp
#print(msg)


# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", 
    from_="+15017250604",
    body=f"{msg}")

print(message.sid)
