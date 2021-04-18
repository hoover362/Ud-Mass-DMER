import discord
import os
import ctypes
import colorama
import requests
import time
from colorama import Fore
from discord.ext import commands


def Clear():
    os.system('cls')
Clear()

while True:
    Text = input("[+] Enter Text : ")
    if Text =="TEXT_HERE":
        print(f'[{Fore.RED}-{Fore.RESET}] You didnt put a message')
        input("Press any key")
        exit(0)
    else:
        print("[+] Press Enter to continue")
        break
Clear()


token = input("Please Enter Token : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Valid token')
    input("Press any key")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Incorrect Token')
    input("Press any key")
    exit(0)
Clear()

def skad():
    try:
            text = f'''  
            888     888 8888888b.  
            888     888 888  "Y88b 
            888     888 888    888 
            888     888 888    888 
            888     888 888    888 
            888     888 888    888 
            Y88b. .d88P 888  .d88P 
             "Y88888P"  8888888P"                   
        '''
        
            bad_colors = ['MAGENTA', 'YELLOW']
            codes = vars(colorama.Fore)
            colors = [codes[color] for color in codes if color in bad_colors]
            colored_chars = [random.choice(colors) + char for char in text]
            print(''.join(colored_chars))

    except KeyboardInterrupt:
        sys.exit() 


@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      Shikoku = discord.Embed(color= discord.Color(000000))
      Shikoku.set_footer(text="Shikoku Mass Dmer")
      Shikoku.set_author(name="")
      Shikoku.add_field(name="`Shikoku",value=Text)
      await user.send(embed=Shikoku)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")
       print(f"Directed messaged all users friends")


client.run(token, bot=False)
