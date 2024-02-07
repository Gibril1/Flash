import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from openai_service import OpenAIService
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
chat_id = os.getenv('CHAT_ID')
bot_token = os.getenv('BOT_TOKEN')
client = TelegramClient('me', api_id, api_hash)


ai_service = OpenAIService()



    
# Event handler for incoming messages
@client.on(events.NewMessage)
async def handle_message(event):
    if event.is_private:  # Respond only to private messages
        
        user_input = event.message.text
        # Process user input and generate response
        response = await ai_service.prompt(user_input)
        # Send response back to the user
        await event.respond(response)

# Start the Telethon client
client.start(bot_token=bot_token)

# Run the client
client.run_until_disconnected()
 
      


    
        

