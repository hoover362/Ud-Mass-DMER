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
    Text = input("[+] Enter Text : ")
    if Text =="TEXT_HERE":
        print("You didn't add text?")
        input("Make sure to add text")
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
  for user in client.user.friends:
    try:
      Shikoku = discord.Embed(color= discord.Color(000000))
      Shikoku.set_footer(text="Shikoku")
      Shikoku.set_author(name="")
      Shikoku.add_field(name="Shikoku owns you",value=Text)
      Shikoku.set_image(url="https://media.discordapp.net/attachments/830442015006130180/830442093351534592/original_12.gif")
      await user.send(embed=Heyo)
      print(f"messaged: {user.name}")
    except:
       print(f"Message failed to send to: {user.name}")
       print(f"Finished")


client.run(token, bot=False)