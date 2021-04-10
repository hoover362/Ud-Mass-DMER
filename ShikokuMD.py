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
            .d8888b.  888       d8b 888                  888               
            d88P  Y88b 888      Y8P 888               888               
            Y88b.      888          888               888               
             "Y888b.   88888b.  888 888  888  .d88b.  888  888 888  888 
                "Y88b. 888 "88b 888 888 .88P d88""88b 888 .88P 888  888 
                  "888 888  888 888 888888K  888  888 888888K  888  888 
            Y88b  d88P 888  888 888 888 "88b Y88..88P 888 "88b Y88b 888 
             "Y8888P"  888  888 888 888  888  "Y88P"  888  888  "Y88888 
            Jud owns you                          
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
        friends = []
        for i in massdm.client.user.friends:
            friends.append(i)
        massdm.banner()
        input(f"{Fore.LIGHTGREEN_EX}Press any button to continue..")
        messagetosend = input(f"{Fore.LIGHTGREEN_EX}Insert message to send: ")
        print("Starting...")
        utils.rename(f"Sending message to {len(friends)} friends..")
        for i in friends:
            try:
                await i.send(messagetosend)
                print(f"{Fore.LIGHTCYAN_EX}Message sent to: {i.name}{Fore.RESET}")
            except Exception as err:
                print(f"{Fore.RED} Error sending DM to {i.name}: {err}{Fore.RESET}")
        input(f"{Fore.GREEN}Message have been dmed to {len(friends)} friends! Press any button to exit..")
        utils.rename("Done sending messages")

    def run(token):
        massdm.client.run(token, bot=False)

massdm.run(token)
