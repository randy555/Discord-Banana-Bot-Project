from BananaVariables import* 

# Discord bot meant for my friends and their friends. Also just a side project to start learning about discords api better.


print('''
    The code in this bot is copyrighted and all rights are reserved by the creator SIЯ.MILҜGФББLΞЯ™#8836 usr id 953522173157449768. If you have a question about this file and using my discord ID does not work please contact me by looking up my discord ID on discord.id You can then add me using that info.
    This code is provided "as is" without warranty of any kind. The creator is not responsible for any harm or damage caused by using the code.
    This code should not be used by anyone other than the creator unless given express permission.
    By using the code, you agree to these terms.
''')



# Create a new Discord client and other variables



####### Command sections

# Help command#
@bot.command(
    name="help", 
    description="This command will disply help commands"
)
async def help_command(interaction):
    await interaction.response.send_message(help_text,ephemeral=True)

# Bot Credits#
@bot.command(
    name="credits", 
    description="This Command gives credit to my creator!"
)
async def credits(interaction):
    await interaction.response.send_message(f'<@953522173157449768> is the creator of this bot, thats me! I hope everyone enjoys using it for the memes.')

#Fact Command, Gives fact to user based on their selection#
@bot.command(
    name="facts", 
    description="Gives a fact about any of the following: Bananas, Plantains, Pears, and Tomatos"
)
@app.describe(choice='Please choose the item you want a fact about')
@app.choices(choice=[
    app.Choice(name="Banana Fact", value="1"),
    app.Choice(name="Plantain Fact", value="2"),
    app.Choice(name="Pear Fact", value="3"),
    app.Choice(name="Tomato Fact", value="4")
    ]
)
async def facts(interaction, choice:str):
    await interaction.response.send_message(get_fact(choice))

# Call command (Displays a window using tkinter)#
@bot.command(
    name='call', 
    description="This command will display a window on Sir.MilkGobblers computer"
)
@app.describe(message1='This will be displayed on Sir.MilkGobblers computer')

#Initial Call command arguments and info.#
async def call(interaction, message1: str):

    guild_name, guild_id, user_display_name,user_id = interaction.guild.name, interaction.guild.id, interaction.user.display_name, interaction.user.id
    channel_id = interaction.channel.id
    print(f"\n\n{user_id} used the call function in guild {guild_id}\n\n")
    await interaction.response.send_message(f"'{message1}' been displayed on <@953522173157449768> Computer.")

    thread = Thread(target=_show_window, args=(message1,user_id,user_display_name,guild_name,guild_id,channel_id))
    thread.start()

# Window creation for call command. #
def _show_window(message1: str, user_id: str, user_display_name: str, guild_name, guild_id,channel_id):
    obj = Tk()
    obj.title("BananaBot-Call")
    obj.geometry("900x500")
    wintext = Text(obj)
    label = ttk.Label(obj, text=f'{user_id} {user_display_name} said:  {message1} ')
    label.pack(pady=10)
    text = tk.Text(obj)
    text.pack(pady=10)
    button = ttk.Button(obj, text="Send", command=lambda: _send_message(guild_id, channel_id, text.get("1.0", "end"), user_id))
    button.pack(pady=10)
    wintext.insert(END, f"\n\n\nUserID= {user_id} Display Name= {user_display_name}\nGuild ID= {guild_id} Guild Name= {guild_name}")
    wintext.pack()
    obj.after(100, lambda: winsound.PlaySound("F:/Documents/videos/tennnis_og.wav", winsound.SND_FILENAME))
    obj.mainloop()
def _send_message(guild_id, channel_id, message, user_id):
    asyncio.run_coroutine_threadsafe(client.get_channel(channel_id).send(f"Randy says: {message}"), client.loop)

# Sends a random fact about a monkey into the chat the command was run in.#
@bot.command(
    name='start-stop', 
    description="This will start/stop monkey facts every hour, type 'start' or 'stop'"
)
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
@bot.command(
    name="time_difference", 
    description='This command can claculate the amount of time between two dates or the current date'
)
@app.describe(
date2='Format YYYY-MM-DD, MM/DD/YYYY, MM-DD-YYYY, or YYYY/MM/DD',
date1='Format YYYY-MM-DD, MM/DD/YYYY, MM-DD-YYYY, or YYYY/MM/DD',
privacy='Wether you want the message and its contents to be able to be seen by other guild memebers.'
)
@app.choices(privacy=[
    app.Choice(name="True", value="True")
    ]) # Chooseable value so users do not have to enter True manually.
async def time_difference(interaction, date1:str, date2:str=None, privacy:str='False'):
    privacy = app.Choice(name=privacy, value=privacy)
    # Privacy Check
    if privacy.value == "True":
        await interaction.response.send_message(discord_time_check(date1, date2),ephemeral=True)
    elif privacy.value == "False" or privacy == None:
        await interaction.response.send_message(discord_time_check(date1, date2))

# bug report command
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

    await sendDm(guild_name, guild_id, user_display_name,user_id,bug,user,choice=1)
    await interaction.response.send_message("Bug report received and added to the list. Thank you for helping :) \nP.S. Only you can see this message.",ephemeral=True)    


# Recommendation report command
@bot.command(
    name ='recommendation_report',
    description=f'Please use this command if you would like to give a recommendation for Banana Facts :)'
)
@app.describe(
    recommendation='Please type the recommendation here!'
)

# Gets user info for documentiation about the Recommendation report#
async def Recomendation_Report(interaction, recommendation:str):
    user = await client.fetch_user("953522173157449768")

    # Attempts to get guild information, this allows the command to work in DM's
    try:
        guild_name, guild_id = interaction.guild.name, interaction.guild.id
    except:
        guild_id,guild_name = '`From DMs`','`From DMs`'
            
    # User Id and Display for documentation
    user_display_name,user_id =interaction.user.display_name, interaction.user.id

    Recommendation_Report_txt(guild_name, guild_id, user_display_name,user_id, recommendation)

    await sendDm(guild_name, guild_id, user_display_name,user_id,user=user,choice=3)
    await interaction.response.send_message("Recommendation report received and added to the list. Thank you for helping :) \nP.S. Only you can see this message.",ephemeral=True)    


###### End of command sections

# Command tree sync
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await bot.sync()
    print(f"Command tree synced at {current_time(5)}")
    
    thread_Main = Thread(target=Display)
    thread_Main.start()

    # On join guild message.
@client.event
async def on_guild_join(guild):
    user = await client.fetch_user("953522173157449768")    
    general = guild.system_channel
    
    if general and general.permissions_for(guild.me).send_messages:
        
        await general.send(
'''
Hello {}! Thank you for adding me to your server! 
If you have any questions please use the `"/help"` command.

Id like to credit my creator <@953522173157449768>. I would also like to mention, if you notice any bugs or issues with the bot please message my creator and let him know! Or use the `"/bug_report"` command.



'''

.format(guild.name))
    await sendDm(guild.name,guild.id,user=user,chocie=2)

    #run bot
client.run(TOKEN)
