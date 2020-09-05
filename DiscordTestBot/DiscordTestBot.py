# インストールした discord.py を読み込む
import discord

#HTTPのライブラリ
import requests


import aiohttp
import asyncio


# Botのアクセストークン
TOKEN = 'NzQ1NDk4ODg0NDI3NjEyMjMw.Xzyp8A.SSKoo61xXapSt2Ldsrie-eTgmpE'

client = discord.Client()

############################################

def login_check():
    @client.event
    async def on_ready():
        print("Discordにログインしました")


'''def Discord_Message():    
    response = requests.get('https://api.github.com/zen')
    soup = response.text
    return soup'''

async def Discord_Message():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/zen') as resp:
            #soup = await resp.text()
            loop = asyncio.get_event_loop()
            soup = loop.run_until_complete(Discord_Message())
            return soup

def command_judge():
    @client.event
    async def on_message(message):
        if message.author.bot:
            print("Bot送信 : ", end="")
            print(Discord_Message())
            return
        if message.content == '/810':
            print("User送信 : ", end="")
            print(message.content)
            await message.channel.send(Discord_Message())
        
############################################

login_check()

command_judge()



client.run(TOKEN)

