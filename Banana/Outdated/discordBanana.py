# Discord Bot for me and my buddies

import discord
import random
from discord import app_commands
import time
from datetime import datetime
from tkinter import*
import threading
import winsound

# Create a new Discord client with the intents parameter
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Define the bot's token
TOKEN = ''



# Define a list of banana facts
banana_facts = [
    "Bananas are actually berries.",
    "Bananas are a good source of potassium.",
    "Bananas are the world's most popular fruit.",
    "Bananas come in many different varieties.",
    "Bananas are rich in vitamins and minerals.",
    "Bananas are often used in baking.",
    "Did you know if you eat 6.48 trillion bananas you would have the same amount of radiation that Chernobyl did?",
    "Did you know that if you eat 100 bananas you get the same amount of radiation from a normal day in the United States?",
    "Did you know that it would require 118 billion bananas to equal the same amount of enriched plutonium in a nuclear bomb?",
    "Did you know that if you ate 10,000,000 bananas at once you would die from radiation poisoning?",
    "Did you know that if you ate 274 bananas a day for seven years you would experience chronic radiation symptoms?",
    "Did you know that there are more than 1,000 varieties of bananas grown in over 150 countries?",
    "Did you know that nearly all the bananas supplied to the United States are Cavendish bananas since they are more resilient to the effects of traveling?",
    "Did you know that the biggest producers of bananas are India and China?",
    "Did you know that the plant that produces bananas is commonly called a tree but is the largest herbaceous flowering plant? The trunk is actually a false stem.",
    "Did you know that each bunch of bananas could have between 3 to 20 tiers and each tier could contain up to 20 bananas?",
    "Did you know that bananas that are exported are picked green and ripened at the destination country?",
    "Did you know that bananas have 19 grams of sugar, 450 Mg of potassium, 1 gram of protein, and 30 grams of Carbs?",
    "Did you know that moderate consumption of bananas could protect against kidney cancer?",
    "Did you know that commercial bananas have been bred to contain three sets of genes so they don't produce mature seeds and are therefore sterile."
    "Did you know that banana peels are edible and actually extremely nutritious? They contain high amounts of B6, B12, Magnesium, and potassium!",
    "DID YOU KNOW THAT BANANAS ARE CONSIDERED BERRIES?",
    "Did you know that a bunch of bananas is called a hand?",
    "Did you know that a single banana is called a finger?",
    "Did you know that there is almost 1,000 varieties of bananas?",
    "Did you know that botanically, there is no difference between plantains and bananas?",
    "Did you know that the world's largest banana producers are India, China, and Indonesia? In descending order",
    "Did you know that wild bananas grow throughout Southeast Asia, but most are inedible for humans, as they are studded with hard seeds?",
    "Did you know that the fastest time to eat a banana with no hands is 20.33 seconds? This record was set by Leah Shutkever in the UK.",
    "Did you know that bananas are fucking amazing?"
]



#Help command
@tree.command(name="help", description= "This command will disply help commands"  )
async def Credits(interaction):
    await interaction.response.send_message(f'Use /banana for a banana fact. Use /credits to see who created me. Use /get-this-man-his-pimp-cup to spam ping the bot creator. /banana-multi does not work currently.')



#Banana fact command for use in the server
@tree.command(name = "banana", description = "This command gives a banana fact!" ) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def Banana_command(interaction):
    fact = random.choice(banana_facts)
    await interaction.response.send_message(fact)




#credits
@tree.command(name="credits", description= "This Command gives credit to the bots creator!"  )
async def Credits(interaction):
    await interaction.response.send_message(f'<@953522173157449768> is the creator of this bot, thats me! I hope everyone enjoys using it for the memes.')





#testing various responses
@tree.command(name="date", description= " Nothing" )
async def MultiBanana(interaction):
    time= datetime.now().strftime("%H:%M:%S")
    await interaction.response.send_message(time)
    # fact = random.choice(banana_facts)


# Command which creates window on host machine using input from discord user.
@tree.command(name='call', description="This command will display a window on Sir.MilkGobblers computer" )
async def call(interaction, message:str):
    await interaction.response.send_message(f"'{message}' been displayed on <@953522173157449768> Computer.")
    threading.Thread(target=_show_window, args=(message,)).start()

# Window creation
def _show_window(message:str):
    obj=Tk()  
    obj.title("Discord banana bot command")  
    obj.geometry("900x500")  
    wintext = Text(obj)  
    wintext.insert(INSERT, message)  
    wintext.insert(END, "")  
    wintext.pack()  
    obj.after(100, lambda: winsound.PlaySound("F:/Documents/videos/tennnis_og.wav", winsound.SND_FILENAME))
    obj.mainloop()



# # Synicing commands
# @client.event
# async def on_ready():
#     await tree.sync()
#     print("Ready!")
#     print(f'{client.user} has connected to Discord!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await tree.sync()

@client.event
async def on_message(message):
    await tree.handle_message(message)


# Define the event that runs when the bot receives a message
@client.event
async def on_message(message):
    # Check if the message content starts with "banana"
    if message.content.startswith("banana"):
        # Select a random banana fact
        fact = random.choice(banana_facts)

        # Send the selected fact to the channel
        await message.channel.send(fact)


# Run the bot
client.run(TOKEN)