import ccxt
import time
from os import system, name

print("   ######    ######      #######    #######     #######     ###### ")
print("   #         #    #         #       #     #        #       #      # ")
print("   #         #####          #       # #####        #       #      # ")
print("   #         #    #         #       #              #       #      #  ")
print("   #         #     #        #       #              #       #      # ")
print("   ######    #      #    #######    #              #        ######  ")

apikey = str(input("\nInsert your ApiKey: "))
print("=====================================================================================")
secret_phrase = str(input("Insert your secret phrase: "))

exchange = ccxt.binance({
    'apiKey': apikey,
    'secret': secret_phrase,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',
    },
})

exchange.load_markets()

def find_price():
    time.sleep(1)
    print("\n===================================================================================")
    what_find = str(input("What price could i find: "))
    price = exchange.fetchTicker(what_find)['last']
    print("=======================================================================================")
    print(price)
    time.sleep(1)
    print("\n=======================================================================================")
    print("PRICE FOUND")

def buy():
    time.sleep(1)
    print("\n=======================================================================================")
    what_buy = str(input("What could i buy: "))
    print("=======================================================================================")
    how_buy = str(input(f"How {what_buy} could i buy: "))
    time.sleep(1)
    exchange.fapiPrivate_post_order({'symbol':what_buy, 'side':'buy', 'type':'MARKET', 'quantity':how_buy, 'workingType':'CONTRACT_PRICE'})
    time.sleep(1)
    print("\n=======================================================================================")
    print("CRYPTO BOUGHT")

def sell():
    print("\n=======================================================================================")
    what_sell = str(input("What could i sell: "))
    print("=======================================================================================")
    how_sell = str(input(f"How {what_sell} could i sell: "))
    time.sleep(1)
    exchange.fapiPrivate_post_order({'symbol':what_sell, 'side':'sell', 'type':'MARKET', 'quantity':how_sell, 'workingType':'CONTRACT_PRICE'})
    time.sleep(1)
    print("\n=======================================================================================")
    print("CRYPTO SOLD")

def start():
    time.sleep(1)
    print("\n\n===============================================================================")
    what_do = input("WHAT DO: Find Crypto Price, Buy Crypto, Sell Crypto: ").lower()
    if what_do == "find crypto price" or what_do == "find price":
        find_price()
    elif what_do == "buy crypto" or what_do == "buy":
        buy()
    elif what_do == "sell crypto" or what_do == "sell":
        sell()
    else:
        print("\n================================================================================")
        print("PLEASE, ANOTHER TIME INSERT A CORRECT VALUE")
        start()
    
    print("\n===================================================================================")
    reStart = input("Do you want to re-start the Bot, Y/N: ").lower()
    if reStart == "y" or reStart == "yes":
        time.sleep(2)
        _ = system('cls')
        start()
    else:
        print("\n====================================================================================")
        print("OKAY, THANKS FOR USING MY BOT")
        time.sleep(2)
        _ = system('cls')
        
    
start() 





