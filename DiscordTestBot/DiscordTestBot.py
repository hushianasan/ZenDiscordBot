# インストールした discord.py を読み込む
import discord

#HTTPのライブラリ
import requests


# Botのアクセストークン
TOKEN = ''

client = discord.Client()

############################################

def login_check():
    @client.event
    async def on_ready():
        print("Discordにログインしました")


def Discord_Message():    
    response = requests.get('https://api.github.com/zen')
    soup = response.text
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

