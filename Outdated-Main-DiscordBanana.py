import discord
import random
from discord import app_commands
from threading import Thread
import winsound
from tkinter import Tk, Text, INSERT, END

# Create a new Discord client
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = app_commands.CommandTree(client)


# Define the bot's token
TOKEN = 'MTA0NDgzODg5MTEyNDk1MzEzOA.Gq6ZTu.rg8zV76jaIxNOoGU22RjVsgy3J-rd8F_u9JKMQ'

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
### Command sections

# Help command
@bot.command(name="help", description="This command will disply help commands")
async def help_command(interaction):
    await interaction.response.send_message(f'Use "/banana" for a banana fact. \nUse "/credits" to see who created me. \nYou can also use "/call message:" to display a message on <@953522173157449768> Computer. ')

# Banana fact command
@bot.command(name="banana", description="This command gives a banana fact!")
async def banana_fact(interaction):
    fact = random.choice(banana_facts)
    await interaction.response.send_message(fact)

# Bot Credits
@bot.command(name="credits", description="This Command gives credit to the bots creator!")
async def credits(interaction):
    await interaction.response.send_message(f'<@953522173157449768> is the creator of this bot, thats me! I hope everyone enjoys using it for the memes.')

# Call command (Displays a window using tkinter)
@bot.command(name='call', description="This command will display a window on Sir.MilkGobblers computer")
async def call(interaction, message: str):
    await interaction.response.send_message(f"'{message}' been displayed on <@953522173157449768> Computer.")
    thread = Thread(target=_show_window, args=(message,))
    thread.start()

#Window creation
def _show_window(message: str):
    obj = Tk()  
    obj.title("BananaBot-Call")  
    obj.geometry("900x500")  
    wintext = Text(obj)  
    wintext.insert(INSERT, message)  
    wintext.insert(END, "")  
    wintext.pack()  
    obj.after(100, lambda: winsound.PlaySound("F:/Documents/videos/tennnis_og.wav", winsound.SND_FILENAME))
    obj.mainloop()

##### End of command sections


# Command tree sync
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await bot.sync()
    print(f"Command tree synced")

#run bot
client.run(TOKEN)    