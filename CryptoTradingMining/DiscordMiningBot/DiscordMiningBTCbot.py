import discord
from discord import Client
from discord.ext.tasks import loop
from requests import get
import ccxt
import time

exchange = ccxt.binance({})

intents = discord.Intents.all()   #For set the intents in the bot

bot = Client(intents=intents)    #Assigned at the variable bot the value Client from library discord

channel_id = 

TOKEN = ''    #Rappresentative TOKEN of the channel

FILENAME = ''

def get_target_price():
    with open(FILENAME) as f:
        target_price = float(f.read())
    return target_price


def set_target_price(new_target_price):
    with open(FILENAME, 'w') as f:
        f.write(new_target_price)


#For start the bot with his main function
@bot.event
async def on_ready():
    send_quote.start()


#For send quote of the BTC price    
@loop(hours=12)     
async def send_quote():
    actual_price = exchange.fetchTicker('BTC/EUR')['last']
    channel = bot.get_channel(channel_id)
    text = f"Il prezzo attuale di 1 BTC è {actual_price} euro"
    if actual_price < get_target_price():
        await channel.send(text)
        await channel.send(f"E' arrivata l'ora di comprare! 🤑")


#For answer at the messages of the user
@bot.event
async def on_message(message):
    autor = message.author
    text = message.content
    channel = message.channel
    if autor == bot.user:
        return
    if text.startswith('!prezzo'):
        new_target_price = text.split()[1]
        set_target_price(new_target_price)
        await channel.send(f"Ho aggiornato il prezzo a {get_target_price()} euro!")
        return
    await channel.send(f"Ciao {autor.name} 😊")
    time.sleep(1)
    await channel.send(f"Ti avviso non appena 1 BTC costa meno di {get_target_price()} euro!")
    time.sleep(1)
    await channel.send(f"Per settare il prezzo target utilizza il comando `!prezzo <nuovo_prezzo_target>` ")

#For run the bot
bot.run(TOKEN)








