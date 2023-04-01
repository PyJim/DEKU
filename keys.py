from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

account_sid = 'AC793f77012fb143c2100a6974f50bd2b7'
auth_token = '000a11aeaa3018231d66eb3999d80f9c'

twilio_number = '+15856393403'
target_number = '+233592407690'


client = Client(account_sid, auth_token)

def sendSMSmessage(Message):
    message = client.messages.create(
        body = Message,
        from_ = twilio_number,
        to = target_number
    )

def call():
    call = client.calls.create(
        url= 'http://demo.twilio.com/docs/voice.xml',
        to = target_number,
        from_= twilio_number
    )
