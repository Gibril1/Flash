import os
import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv
load_dotenv()


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('me', api_id, api_hash)



async def get_channels_and_groups():
    # First of all, get all the channels and their ID's and store 
    channels = []
    async for dialog in client.iter_dialogs():
        if dialog.is_channel or dialog.is_group:
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
    messages = []
    async for message in client.iter_messages(id):
        messages+=[{
            'message_id': message.id,
            'message': message.text
        }]
    return messages
    

async def get_channel_subscribers(id):
    member_details = []
    participants = await client.get_participants(id, aggressive=True)
    for participant in participants:
        member_details += [{
            'first_name': participant.first_name ,
            'last_name': participant.last_name,
            'phone_number': participant.phone,
            'username': participant.username
        }]
    return member_details

async def main():
    async with client:
        channel_data = await get_channels_and_groups()

        # Print the channels 
        print('\n\nSee the list of channels you can choose from')
        for index, channel in enumerate(channel_data):
            print(f"{index}. {channel['channel_name']}\n")
    
        # Prompt the user for the channel name
        desired_channel = input('Which channel or group messages do you want to scrape:\n ')

        channel_id = get_channel_id(channel_data, desired_channel)  
        while not channel_id:
            # Prompt the user for the channel name
            print('\n You did not enter the right channel name. Try Again...\n')
            desired_channel = input('Which channel messages do you want to scrape:\n ')
            channel_id = get_channel_id(channel_data, desired_channel)
        
        
        messages = await channel_messages(channel_id)
        # Display the messages in the channel to the user
        print('These are the members of the channels')
        participants = await get_channel_subscribers(channel_id)
        print(participants)
        

if __name__ == "__main__":
    asyncio.run(main())



