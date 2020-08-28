# インストールした discord.py を読み込む
import discord

# Webスクレイピング
import requests
from bs4 import BeautifulSoup



# WebサイトのURLを指定
url = "https://api.github.com/zen"

# Requestsを利用してWebページを取得する
r = requests.get(url)

# BeautifulSoupを利用してWebページを解析する
soup = BeautifulSoup(r.text, 'html.parser')

#WebサイトのHTMLを出力
print(soup)



# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzQ1NDk4ODg0NDI3NjEyMjMw.Xzyp8A.mg07XDO9AmhV6MjIU4Blqx7M1l4'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/810':
        await message.channel.send(soup)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
