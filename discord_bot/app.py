# discord_bot.py
import os
import discord
from dotenv import load_dotenv
from neuralintents.main import GenericAssistant
import pickle
import nltk



nltk.download('omw-1.4')
chatbot = GenericAssistant('intents.json') 
chatbot.train_model()
chatbot.save_model()


#PeterBot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #PeterBot command
    if message.content.startswith("!P"):
        
        response = chatbot.request(message.content)
        await message.channel.send(str(response))
    if message.content =='?P Calcryx':
        with open('Calcryx (2).png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

client.run(TOKEN)