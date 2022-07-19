import asyncio, os
import hypercorn.asyncio
from flask import Flask
from asgiref.wsgi import WsgiToAsgi
from hypercorn.config import Config

from telethon import TelegramClient, events
from telethon.sessions import StringSession



app = Flask(__name__)
aapp = WsgiToAsgi(app)


#heroku support##
#Procfile ~> web: python3 web.py --workers 1 
port = int(os.environ.get("PORT", 5000))
config = Config()
config.bind = [f"0.0.0.0:{port}"] 
###*###


bot = TelegramClient()


@app.route('/')
async def hello_world():
   return 'Hello World'

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    return await event.respond('hello World!')


async def sbot():
  await bot.start()
  print("bot started")
   
def main():
 if __name__ == "__main__":
   bot.loop.run_until_complete(sbot()) 
   bot.loop.run_until_complete(hypercorn.asyncio.serve(aapp, config))
 
 
main()
  

  
  
