import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC02428c9c7fb839e5cb4f31e3e9d2acb4"
auth_token = "790b6caf692569d1cccec7b35d63e3f0"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='whatsapp:+14155238886',
         body='Hi, Vraj! Thanks for placing an order with us. We’ll let you know once your order has been processed and delivered. Your order number is O12235234',
         to='whatsapp:+919099735209'
     )

print(message.sid)