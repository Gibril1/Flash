import os
from dotenv import load_dotenv
load_dotenv()
from openai import AsyncOpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


class OpenAIService:
    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=OPENAI_API_KEY
        )

    async def prompt(self, message:str):
        response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant designed to give meaningful responses to users"},
                    {"role": "user", "content": message}
                ]
                )
        return response.choices[0].message.content