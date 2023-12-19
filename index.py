import os
import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv
load_dotenv()


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('me', api_id, api_hash)

async def get_channels():
    # First of all, get all the channels and their ID's and store 
    channels = []
    async for dialog in client.iter_dialogs():
        channels+=[{
            'channel_id': dialog.id,
            'channel_name': dialog.name
        }]
    
    return channels

def get_channel_id(channels, name):
    for channel in channels:
        if name == channel['channel_name']:
            return channel['channel_id']
    return None

async def channel_messages(id):
    async for message in client.iter_messages(id):
        print(message.id, message.text)
    



async def main():
    async with client:
        channel_data = await get_channels()

        desired_channel = input('Which channel messages do you want to scrape:\n ')
        channel_id = get_channel_id(channel_data, desired_channel)
        
        if channel_id:
            await channel_messages(channel_id)
        else:
            print('Channel not found.')

if __name__ == "__main__":
    asyncio.run(main())