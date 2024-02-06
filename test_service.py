import asyncio
from telegram_service import TelegramService


telegram_service = TelegramService()

async def main():

    async with telegram_service.client:
        try:
            message = await telegram_service.reply_messages('Write C++ code to determine if a number is a prime number')
            

            
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    asyncio.run(main())