# インストールした discord.py を読み込む
import discord

#HTTPのライブラリ
import requests


import aiohttp
import asyncio


# Botのアクセストークン
TOKEN = 'NzQ1NDk4ODg0NDI3NjEyMjMw.Xzyp8A.mg07XDO9AmhV6MjIU4Blqx7M1l4'

client = discord.Client()

############################################

def login_check():
    @client.event
    async def on_ready():
        print("Discordにログインしました")

def Discord_Message():
    async with aiohttp.ClientSession() as session:


'''def Discord_Message():    
    response = requests.get('https://api.github.com/zen')
    soup = response.text
    return soup'''

def command_judge():
    @client.event
    async def on_message(message):
        if message.author.bot:
            print("Bot送信")
            return
        if message.content == '/810':
            print("User送信")
            print(Discord_Message())
            await message.channel.send(Discord_Message())
        
############################################

login_check()

command_judge()



client.run(TOKEN)

