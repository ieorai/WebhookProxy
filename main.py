from fastapi import FastAPI
import os
import requests
Discord_Webhook = " "

def SendMessageToDiscord(Msg):
    Message = {
        "content": Msg
    }
    requests.post(Discord_Webhook, data=Message)

app = FastAPI()

@app.get("/discord")
async def read_items(Webhook: str, Message: str):
    Discord_Webhook = Webhook
    SendMessageToDiscord(Message)
    return "Success."
