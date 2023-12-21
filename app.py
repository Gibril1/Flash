import asyncio, json
from telethon import TelegramClient
from constants import api_hash, api_id

# Class Implementation
class TelegramReader:
    def __init__(self) -> None:
        self.api_hash = api_hash
        self.api_id = api_id
        self.client = TelegramClient('me', self.api_id, self.api_hash)
    
    async def get_channels_and_groups(self):
    # First of all, get all the channels and their ID's and store 
        channels = []
        async for dialog in self.client.iter_dialogs():
            if dialog.is_channel or dialog.is_group:
                channels+=[{
                    'channel_id': dialog.id,
                    'channel_name': dialog.name
                }]
        return channels
    
    async def get_channel_id(self, name):
        for channel in await self.get_channels_and_groups():
            if name == channel['channel_name']:
                return channel['channel_id']
        return None
    
    async def channel_messages(self, id):
        messages = []
        async for message in self.client.iter_messages(id):
            messages+=[{
                'message_id': message.id,
                'message': message.text,
            }]
        return messages


async def main():
    reader = TelegramReader()

    async with reader.client:
        # Get the channels
        channels = await reader.get_channels_and_groups()

        # put the channels in a json file
        with open('channels.json', 'w') as channel_file:
            json.dump(channels, channel_file, indent=4)

        # Print the channels
        for index, channel in enumerate(channels):
            print(f"{index} ---- {channel['channel_name']}\n")

        print("All channels have been printed")
        desired_channel = input('Choose from the list, the channel you want to read messages\n')

        # get the id of your channel
        channel_id = await reader.get_channel_id(desired_channel)
        while not channel_id:
            # Prompt the user for the channel name
            print('\n You did not enter the right channel name. Try Again...\n')
            desired_channel = input('Which channel messages do you want to scrape:\n ')
            channel_id = await reader.get_channel_id(desired_channel)
        

        # print the messages in the channel
        messages = await reader.channel_messages(channel_id)
        with open('messsages.json', 'w') as messages_file:
            json.dump(messages, messages_file, indent=4)
        
        for index, message in enumerate(messages):
            print(f"{index} ---- {message['message']}\n")

if __name__ == "__main__":
    asyncio.run(main())
