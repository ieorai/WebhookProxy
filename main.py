from boto.s3.connection import S3Connection
from fastapi import FastAPI
import os
import requests
Discord_Webhook = S3Connection(os.environ['Auth_key'], )
Website_Api = S3Connection(os.environ['Website_Key'], os.environ['Auth_key'])

def SendMessageToDiscord(Msg):
    Message = {
        "content": Msg
    }
    requests.post(Discord_Webhook, data=Message)

# app = FastAPI()

@app.get("/discord")
async def read_items(Key: str, Message: str):
    if Key == Website_Api:
      SendMessageToDiscord(Message)
    else:
        return "Incorrect key"
