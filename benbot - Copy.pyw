from distutils.util import change_root
import discord
import random
import shutil

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    


@client.event
async def on_message(message):
    if message.author.id == 844916991231131678:
        await message.channel.send("Shut the fuck up JOE, i'm the superior bot!")
        print("joe sadly spoke")
    elif message.author.id == 757034926565752912:
        await message.channel.send("go to hell you impostor")
        print("sussy impostor")

    if 'ben' in message.content.lower():
       x = random.randint(1, 100)
       line = 0
       if x <= 59:
            print("Yes")
            f= open("C:/Users/hecto/Desktop/logs.txt","a+")
            f.write("Ben said yes, ")
            await message.channel.send('Yes')
       elif x == 60:
            print("**YOO 1% CHANCE!** <---------------------------------------------------------")
            f= open("C:/Users/hecto/Desktop/logs.txt","a+")
            f.write("Ben is a registered sex offender, ")
            await message.channel.send("I'm a registered sex offender")

        
       else:
            print("No")
            f= open("C:/Users/hecto/Desktop/logs.txt","a+")
            f.write("Ben said no, ")
            await message.channel.send('No')

            
            

        # Do stuff here
client.run('insert your token nerd')
