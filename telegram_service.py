import os
from dotenv import load_dotenv
from telethon import TelegramClient
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
chat_id = os.getenv('CHAT_ID')
client = TelegramClient('me', api_id, api_hash)

from openai_service import OpenAIService

ai_service = OpenAIService()

class TelegramService:
    def __init__(self) -> None:
        print('Telegram service')
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = client

    
    async def send_message_to_channel(self, message: str):
        message = await self.client.send_message('FlashGPT_bot', message)

        return message
    
    async def reply_messages(self, message: str):
        sending_message = await self.send_message_to_channel(message)

        ai_response = await ai_service.prompt(sending_message.raw_text)

        # await sending_message.respond(ai_response)
        await self.client.reply_messages(chat_id, ai_response)

       


    
        

