from fastapi import FastAPI
import os
import requests
Webhook_Link = "https://discord.com/api/webhooks/"
Discord_Webhook = ""

def SendMessageToDiscord(Msg):
    Message = {
        "content": Msg
    }
    requests.post(Discord_Webhook, data=Message)

app = FastAPI()

@app.get("/discord")
async def read_items(Webhook: str, Message: str):
    Discord_Webhook = Webhook_Link+Webhook
    SendMessageToDiscord(Message)
    return "Success."
