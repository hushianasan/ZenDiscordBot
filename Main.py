# インストールした discord.py を読み込む
import discord

#HTTPのライブラリ
import requests


import aiohttp
import asyncio


# Botのアクセストークン
TOKEN = ''

client = discord.Client()

############################################

#Discordのログイン確認
def login_check():
    @client.event
    async def on_ready():
        print("Discordにログインしました")

#requestsでZenBotのGet
'''def Discord_Message():    
    response = requests.get('https://api.github.com/zen')
    soup = response.text
    return soup'''

#aiohttpでZenBotのGet
async def Discord_Message():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/zen') as resp:
            print(await resp.text())
            soup = await resp.text()
            return soup
loop = asyncio.get_event_loop()
loop.run_until_complete(Discord_Message())


#送信のジャッジ
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

            print(Discord_Message())
            await message.channel.send(Discord_Message())
        
############################################

login_check()

command_judge()



client.run(TOKEN)

