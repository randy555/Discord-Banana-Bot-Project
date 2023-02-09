from BananaVariables import* 

print('''
    The code in this bot is copyrighted and all rights are reserved by the creator SIЯ.MILҜGФББLΞЯ™#8836 usr id 953522173157449768. If you have a question about this file and using my discord ID does not work please contact me by looking up my discord ID on discord.id You can then add me using that info.
    This code is provided "as is" without warranty of any kind. The creator is not responsible for any harm or damage caused by using the code.
    This code should not be used by anyone other than the creator unless given express permission.
    By using the code, you agree to these terms.
''')



# Create a new Discord client and other variables
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = app_commands.CommandTree(client)
task = None
app = app_commands

                    ####### Command sections

                    # Help command#
@bot.command(name="help", description="This command will disply help commands")
async def help_command(interaction):
    await interaction.response.send_message(help_text,ephemeral=True)

                    # Bot Credits#
@bot.command(name="credits", description="This Command gives credit to my creator!")
async def credits(interaction):
    await interaction.response.send_message(f'<@953522173157449768> is the creator of this bot, thats me! I hope everyone enjoys using it for the memes.')

                    # Banana fact command using the list from BananaVariables#
@bot.command(name="banana", description="This command gives a banana fact!")
async def banana_fact(interaction):
                # Prevents the same fact from being sent after calling banana twice
    B_fact = random.choice(banana_facts)
    b_fact_c = B_fact
    if B_fact == b_fact_c:
        B_fact = random.choice(banana_facts)
    await interaction.response.send_message(B_fact)

                    # Plantain fact command using the list from BananaVariables#
@bot.command(name="plantains", description="This command gives a plantain fact!")
async def Plantain_Fact(interaction):

            # Prevents the same fact from being sent after calling plantains twice
    P_fact = random.choice(Plantain_Facts)
    P_fact_c = P_fact
    if P_fact == P_fact_c:
        P_fact = random.choice(Plantain_Facts)
    await interaction.response.send_message(P_fact)

                    # Pear fact command using the list from BananaVariables#
@bot.command(name="pear", description="This command gives a pear fact!")
async def Plantain_Fact(interaction):

                # Prevents the same fact from being sent after calling pear twice
    PE_fact = random.choice(Pear_Facts)
    PE_fact_c = PE_fact
    if PE_fact == PE_fact_c:
        PE_fact = random.choice(Pear_Facts)
    await interaction.response.send_message(PE_fact)

                    # tomato fact command using the list from BananaVariables#
@bot.command(name="tomato", description="This command gives a tomato fact!")
async def Plantain_Fact(interaction):

                # Prevents the same fact from being sent after calling tomato twice
    T_fact = random.choice(Tomato_Facts)
    T_fact_c = T_fact
    if T_fact == T_fact_c:
        T_fact = random.choice(Tomato_Facts)
    await interaction.response.send_message(T_fact)

                    # Call command (Displays a window using tkinter)#
@bot.command(name='call', description="This command will display a window on Sir.MilkGobblers computer")
@app.describe(message1='This will be displayed on Sir.MilkGobblers computer')
                    
                    #Initial Call command arguments and info.#
async def call(interaction, message1: str):

    guild_name, guild_id, user_display_name,user_id = interaction.guild.name, interaction.guild.id, interaction.user.display_name, interaction.user.id
    
    print(user_id, user_display_name, "Used the call function in guild", guild_id,guild_name)
    await interaction.response.send_message(f"'{message1}' been displayed on <@953522173157449768> Computer.")
    thread = Thread(target=_show_window, args=(message1, user_id, user_display_name, guild_name, guild_id))
    thread.start()

                    # Window creation for call command.#
def _show_window(message1: str, user_id: str, user_display_name: str, guild_name = "Error (Probably a dm?)", guild_id = "Error (Probably a dm?)"):
    obj = Tk()
    obj.title("BananaBot-Call")
    obj.geometry("900x500")
    wintext = Text(obj)
    wintext.insert(INSERT, message1)
    wintext.insert(END, f"\n\n\nUserID= {user_id} Display Name= {user_display_name}\nGuild ID= {guild_id} Guild Name= {guild_name}")
    wintext.pack()
    obj.after(100, lambda: winsound.PlaySound("F:/Documents/videos/tennnis_og.wav", winsound.SND_FILENAME))
    obj.mainloop()

                    # Sends a random fact about a monkey into the chat the command was run in.#
@bot.command(name='start-stop', description="This will start/stop monkey facts every hour, type 'start' or 'stop'")
async def start_stop(interaction, message: str):
    #Getting ch ID
    wanted_channel_id = interaction.channel_id
    await interaction.response.send_message(f"Hello <@{interaction.user.id}>! Thank you for using me!")



    global task
    if message == 'start':
        if task is not None:
            await client.get_channel(wanted_channel_id).send("Monkey facts are already running.")
            return
        await client.get_channel(wanted_channel_id).send('Ok! Starting monkey facts!')
        task = asyncio.create_task(monkey_facts_loop(wanted_channel_id))
    elif message == 'stop':
        if task is None:
            await client.get_channel(wanted_channel_id).send("Monkey facts are already stopped.")
            return
        task.cancel()
        task = None
        await client.get_channel(wanted_channel_id).send('Ok! Stopping monkey facts!')
    else:
        await client.get_channel(wanted_channel_id).send("Invalid command, use 'start' or 'stop'.")
                    
                    #Monkey Facts Loop#
async def monkey_facts_loop(wanted_channel_id):
    while True:
        Monkey = random.choice(Monkey_Facts)
        Monkey1 = Monkey
        if Monkey == Monkey1:
            Monkey = random.choice(Monkey_Facts)
        await client.get_channel(wanted_channel_id).send(Monkey)
        await asyncio.sleep(3600)


                    #Calculates the time difference from a later date to the current date or a specified date#
@bot.command(name="time_difference", description='This command can claculate the amount of time between two dates or the current date')
@app.describe(
date2='Format YYYY-MM-DD, MM/DD/YYYY, MM-DD-YYYY, or YYYY/MM/DD',
date1='Format YYYY-MM-DD, MM/DD/YYYY, MM-DD-YYYY, or YYYY/MM/DD',
privacy='Wether you want the message and its contents to be able to be seen by other guild memebers.'
)
@app.choices(privacy=[
    app.Choice(name="True", value="True"),
    app.Choice(name="False", value="False"),
    ])
async def time_difference(interaction, date1:str, date2:str=None, privacy:app.Choice[str]=None):
    print(privacy)
    if privacy.value == "True":
        await interaction.response.send_message(discord_time_check(date1, date2),ephemeral=True)
    elif privacy.value == "False" or privacy == None:
        await interaction.response.send_message(discord_time_check(date1, date2))

                    # bug report command!
@bot.command(
    name ='bug_report',
    description=f'Please use this command to report bugs with Banana Facts :)'
)
@app.describe(
    bug='Please type the problem you are having here!'
)

                    # Gets user info for documentiation about the bug report#
async def bug_report(interaction, bug:str):
    user = await client.fetch_user("953522173157449768")

    # Attempts to get guild information, this allows the command to work in DM's
    try:
        guild_name, guild_id = interaction.guild.name, interaction.guild.id
    except:
        guild_id,guild_name = '`From DMs`','`From DMs`'
            
    # User Id and Display for documentation
    user_display_name,user_id =interaction.user.display_name, interaction.user.id

    Bug_report_txt(guild_name, guild_id, user_display_name,user_id, bug)

    await sendDm(guild_name, guild_id, user_display_name,user_id,bug,user)
    await interaction.response.send_message("Bug report received and added to the list. Thank you for helping :) \nP.S. Only you can see this message.",ephemeral=True)    
                    
                    ###### End of command sections


    # Command tree sync
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await bot.sync()
    print(f"Command tree synced at {current_time(5)}")

    # On join guild message.
@client.event
async def on_guild_join(guild):
    user = await client.fetch_user("953522173157449768")    
    general = guild.system_channel
    
    if general and general.permissions_for(guild.me).send_messages:
        
        await general.send(
'''
Hello {}! Thank you for adding me to your server! 
If you have any questions please use the "/help" command.

Id like to credit my creator <@953522173157449768>. I would also like to mention, if you notice any bugs or issues with the bot please message my creator and let him know! Or use the `"/bug_report"` command.
'''

.format(guild.name))
    await sendDm(guild.name,guild.id,user=user)

    #run bot
client.run(TOKEN)