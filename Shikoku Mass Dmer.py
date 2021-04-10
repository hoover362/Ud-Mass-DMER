import discord
import os
import ctypes
import colorama
import requests
import time
from colorama import Fore



def Clear():
    os.system('cls')
Clear()


while True:
    password = input("[+] Enter Password: ")
    if password =="HeyoW":
        print("Correct password")
        input("[+] enter to continue to mass dm")
        break
    else:
        print("InCorrect password")
Clear()

while True:
    Text = input("[+] Enter Text you want to send : ")
    if Text =="TEXT_HERE":
        print("you forgot to add text")
        input("Wyd you didnt add text")
        exit(0)
    else:
        print("[+] Enter to continue to mass dm")
        break
Clear()


token = input("Enter token noob : ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('[+] Valid token')
    input("Press any key")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Wrong token tuff')
    input("Press any key")
    exit(0)
Clear()


print(f'''{Fore.MAGENTA}                   
 ██░ ██ ▓█████▓██   ██▓ ▒█████  
▓██░ ██▒▓█   ▀ ▒██  ██▒▒██▒  ██▒
▒██▀▀██░▒███    ▒██ ██░▒██░  ██▒
░▓█ ░██ ▒▓█  ▄  ░ ▐██▓░▒██   ██░
░▓█▒░██▓░▒████▒ ░ ██▒▓░░ ████▓▒░
 ▒ ░░▒░▒░░ ▒░ ░  ██▒▒▒ ░ ▒░▒░▒░ 
 ▒ ░▒░ ░ ░ ░  ░▓██ ░▒░   ░ ▒ ▒░ 
 ░  ░░ ░   ░   ▒ ▒ ░░  ░ ░ ░ ▒  
 ░  ░  ░   ░  ░░ ░         ░ ░  
               ░ ░                                                                                    ''')

client = discord.Client()


@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      Heyo = discord.Embed(color= discord.Color(000000))
      Heyo.set_footer(text="Rloxx#0009")
      Heyo.set_author(name="")
      Heyo.add_field(name="`Zheyo runs u`",value=Text)
      Heyo.set_image(url="https://media.discordapp.net/attachments/801447972989566996/801800626253463562/image0.gif")
      await user.send(embed=Heyo)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")
       print(f"Directed messaged all users friends")


client.run(token, bot=False)