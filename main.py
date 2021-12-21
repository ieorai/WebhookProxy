from fastapi import FastAPI
import os
import requests
Discord_Webhook = os.environ.get('Discord_Webhook')
Website_Api = os.environ.get('Website_Key')

def SendMessageToDiscord(Msg):
    Message = {
        "content": Msg
    }
    requests.post(Discord_Webhook, data=Message)

app = FastAPI()

@app.get("/discord")
async def read_items(Key: str, Message: str):
    if Key == Website_Api:
      SendMessageToDiscord(Message)
    else:
        return "Incorrect key"
