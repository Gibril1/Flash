import os
from dotenv import load_dotenv
load_dotenv()
from openai import AsyncOpenAI

import logging
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OpenAIService:
    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=OPENAI_API_KEY
        )
    logging.info('An OpenAI service class has been created')

    async def prompt(self, message:str):
        logging.info(f'The prompt method received the message {message}')
        response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant designed to give meaningful responses to users"},
                    {"role": "user", "content": message}
                ]
                )
        return response.choices[0].message.content