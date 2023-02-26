import discord
import random
from discord import app_commands
from discord import User
from threading import Thread
import winsound
import tkinter as tk
from tkinter import*
import tkinter.ttk as ttk
import asyncio
from discord.ext import tasks 
import time
from datetime import datetime, timedelta



#       Hello if you're reading this and not me thats actually kind of cool
#       Its nice to see someone other than me reading my programs, but if youre reading this and you shouldnt be, shame on you, Its actually a bad idea to have people use this file.
#       If I sent you this file I probably removed the str for the token variable.
#       :)
#
#
#


            #### Varaibles
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = app_commands.CommandTree(client)
task = None
app = app_commands
now = datetime.now()
TOKEN = """

"""

#Fact lists
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
    "Did you know that commercial bananas have been bred to contain three sets of genes so they don't produce mature seeds and are therefore sterile.",
    "Did you know that banana peels are edible and actually extremely nutritious? They contain high amounts of B6, B12, Magnesium, and potassium!",
    "DID YOU KNOW THAT BANANAS ARE CONSIDERED BERRIES?",
    "Did you know that a bunch of bananas is called a hand?",
    "Did you know that a single banana is called a finger?",
    "Did you know that there is almost 1,000 varieties of bananas?",
    "Did you know that botanically, there is no difference between plantains and bananas?",
    "Did you know that the world's largest banana producers are India, China, and Indonesia? In descending order",
    "Did you know that wild bananas grow throughout Southeast Asia, but most are inedible for humans, as they are studded with hard seeds?",
    "Did you know that the fastest time to eat a banana with no hands is 20.33 seconds? This record was set by Leah Shutkever in the UK.",
    "Did you know that bananas are fucking amazing?",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
]
        #Plantain Facts used in the Plantain facts command.
Plantain_Facts = [
    "The term “plantain” is loosely applied to any banana cultivar that is eaten when cooked. However, there is no formal botanical distinction between bananas and plantains.",
    "Ripe plantains can be eaten raw, since the starches are converted to sugars as they ripen.",
    "In some countries, there may be a clear distinction between plantains and bananas, but in other countries, where many more cultivars are consumed, the distinction isn't made.",
    "All modern plantain cultivars have three sets of chromosomes.",
    "Many modern plantains are hybrids derived from the cross of two wild species, the Musa acuminata and Musa balbisiana.",
    "Fe'i bananas from the Pacific Islands are often eaten roasted or boiled, which is why they're informally called “mountain plantains.”",
    "Plantains are a major food staple in West and Central Africa, the Caribbean islands, Central America, and northern, coastal parts of South America.",
    "Mature, yellow plantains can be peeled like typical dessert bananas. The pulp is softer than in immature, green fruit and some of the starch has been converted to sugar.",
    "As a staple, plantains are treated in a similar way as potatoes and with a similar neutral flavor and texture when the unripe fruit is cooked by steam, boiling or frying.",
    "Since they fruit all year round, plantains are a reliable all-season staple food, particularly in developing countries with inadequate food storage, preservation and transportation technologies.",
    "In Africa, plantains and bananas provide more than 25 percent of the carbohydrate requirements for over 70 million people.",
    "In countries in Central America and the Caribbean, the plantain is either simply fried, boiled or made into plantain soup.",
    "In Kerala, an Indian state, ripe plantain is steamed, which is a popular breakfast dish.",
    "In Ghana of West Africa, boiled plantain is eaten with kontomire stew, cabbage stew or fante-fante stew.",
    "In Nigeria, plantain is eaten boiled, fried or roasted. Boli, which is roasted plantain, is usually eaten with palm oil or groundnut.",
    "In Puerto Rico, the Dominican Republic and Cuba, plantain is mashed after it has been friend and is made into mofongo, or fried and made into tostones, tajadas, or platanutres.",
    "Plantains are sometimes dried and ground into flour. In southern India, dried plantain powder is mixed with a little bit of fennel seed powder and boiled in milk or water to make baby food.",
    "In Peru, plantains are boiled and blended with water, spices and sugar to make chapo.",
    "Plantains are packed with potassium, which is known as a powerful vasodilator. Potassium can help in relaxing the tension in your blood vessels and arteries.",
    "Plantains contain high levels of vitamin C, meaning that they help keep your immune system stimulated and producing white blood cells.",
    "Plantains contain high levels of dietary fiber, which can help optimized digestion by stimulating peristaltic motion, improving the nutrient uptake efficiency and balancing the bacterial levels in the gut.",
    "Plantains are packed with magnesium, which is known to increase the release of tryptophan and serotonin in the body, which can help people relax and sleep.",
    "Plantains are high in iron, which is essential for the production of red blood cells.",
    "Plantains are packed with vitamin A, which has been directly linked to improved eye health in numerous studies. Vitamin A functions as an antioxidant in the body, working to reduce oxidative stress in the eyes.",
    "Plantains are used in the Ivory Coast dish aloco as the main ingredient. Friend plantains are covered in an onion-tomato sauce, often with a grilled fish between the plantains and sauce.",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
]

        #Pear Facts used in the pear facts command.
Pear_Facts = [
    "Pear belongs to the family of roses. It's the cultivation of pears about 1100 years BC in China.",
    "The scientific name for pear is Pyrus communis.",
    "There are over 3000 varieties of pears that can be found around the world today.",
    "Pears are broadly classified based upon their place of origin as Asian-pears and European-pears. Asian varieties are crispy and firm that does not change even after harvesting or storage whereas, European types generally become soft and juicy when allowed to ripen.",
    "China is the world leader in the production of pears.",
    "The first pear tree was planted in North America in 1620 in the Massachusetts Bay colony. Presently the USA is one of the largest producers of pears in the world which is mostly grown on the coast, mainly in Oregon and Washington.",
    "The Bartlett is the most popular variety of pear in the United States. It got its American name when a Bostonian named Enoch Bartlett bought a pear orchard and began distributing them as Bartlett pears.",
    "Pear can grow to the height of 40 to 50 feet and has a pyramid-shaped crown. It has oval or heart-shaped green leaves that are alternately arranged.",
    "Pears are actually harvested green because it continues to ripen after removal from the tree. That it is prevented from being overripe.",
    "Pears are also known as “butter fruit” because they have a soft, butter-like texture when they are ripe.",
    "Pear starts to produce fruit 4 years after planting. The plant can survive from 10 to 50 years.",
    "Pear is about 5 inches long and weighs about 200 gm. A medium pear has about 75 calories. It can be consumed raw or as a part of fruit salads, cakes, and other desserts.",
    "Doctors recommend pears for babies when they are weaning and being introduced to baby food as pears are a low acid fruit that is unlikely to cause digestion problems in babies and pear allergy is rare.",
    "Pears are a good source of minerals such as copper, iron, potassium, manganese, and magnesium as well as B-complex vitamins such as folates, riboflavin, and pyridoxine (vitamin B6).",
    "Pears boost the immune system because they contain antioxidants such as vitamin C and copper which fight off free radicals and disease in the body.",
    "Pears are one of the highest-fiber fruits, offering 6 gms per medium-sized fruit, helping you meet 25 Percent of your daily requirement. Most of the fiber in them is a nonsoluble polysaccharide (NSP), which functions as a good bulk laxative in the gut reducing the occurrence of colon polyps and also chances of colon cancer.",
    "Pears contain the natural form of folic acid, folate, and they should be included in a healthy prenatal diet in pregnancy.",
    "Pears also contain boron, which our bodies need in order to retain calcium, so this fruit can aid in the prevention of osteoporosis.",
    "The Chinese considered the pear, which they call “li,” to be a symbol of immortality. The destruction of a pear tree symbolized tragic or untimely death. it is considered bad luck in China to share a pear because it may lead to the separation of friends or lovers.",
    "Pear leaves were used for the preparation of cigarettes before tobacco became popular.",
    "Pearwood is used to make furniture, musical instruments, and wood carvings. It is also used to make wooden kitchen utensils because it doesn't impart any color or odor to the food and because it is tough enough to withstand repeated washings. Architect's rulers are also made from pear wood because it doesn't warp.",
    "The world's most expensive pear is Buddha-shaped pears which may cost nearly $10 each. They have been cultivated to look exactly like a Buddha statue, even down to the facial details.",
    "The heaviest pear ever grown was about 3 Kg in Japan.",
    "In the Odyssey, Homer called the pear a 'gift from the Gods.'",
    "The word pyriform means 'pear-shaped.'",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
]

        #tomato Facts used in the Tomato facts command.
Tomato_Facts = [
    "A tomato is a fruit that is considered a vegetable due to its culinary uses and is also considered a vegetable by nutritionists.",
    "The largest tomato on record weighed 10 lb. 12.7 oz. and was grown by Dan Sutherland in Walla Walla, Washington.",
    "Tomatoes were once considered poisonous due to the lead toxicity from pewter plates that were used to serve them in the 1800s.",
    "La Tomatina is a tomato fight held in Buñol, Spain on the last Wednesday of August with 20,000 participants.",
    "NASA is modifying the tomato plant to speed up photosynthesis for use in space stations.",
    "Tomatoes are rich in lycopene, an antioxidant that is good for the heart and effective against certain cancers, and are packed with vitamins A and C, calcium, and potassium.",
    "Americans eat 22-24 pounds of tomatoes per person, per year, with half of that being in the form of ketchup and tomato sauce according to the USDA.",
    "Tomatoes originated from Peru and the scientific name for the tomato is Lycopersicon lycopersicum, which means “wolf peach”.",
    "Tomato Juice is the official state drink of Ohio.",
    "There are over 10,000 varieties of tomatoes that come in different colors including pink, purple, black, yellow, and white.",
    "A tomato trial took place in Salem, New Jersey on June 28, 1820. Robert Johnson ate a large amount of tomatoes to prove they were not poisonous.",
    "The gene bred into tomatoes by commercial farmers to give them uniform color had the unintended result of preventing internal sugar reactions that give tomatoes flavor, and has been bred into almost all commercial American tomatoes.",
    "In 2013, a UK company perfected the “TomTato”, a plant that grows potatoes under the soil and tomatoes above.",
    "A Japanese company invented a robot that sits on your back and feeds you tomatoes while you run.",
    "An Italian NGO decided to teach Zambians how to grow food and paid locals to grow tomatoes in a fertile valley that lacked agriculture. When the tomatoes grew large and ripe, 200 hippos came out from the river and ate everything.",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
]

        # Monkey Facts used in the monkey facts loop
Monkey_Facts = [
    "Did you know that monkeys can catch and spread diseases just like humans can?",
    "Monkeys are one of the few species that have the ability to recognize themselves in mirrors.",
    "Monkeys are social animals and live in large groups, called troops.",
    "Some species of monkeys can use tools, such as using sticks to get insects out of crevices.",
    "Monkeys are omnivores and eat both plants and animals for their diet.",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
]

        # Help text, used in the help command
help_text = '''
Use `"/credits"` to see who created me. 
Use `"/facts"` to choose a random fact about Bananas, Plantains, Pears, or Tomatos.
Use `"/call"` to display a message on <@953522173157449768> Computer.
Use `"/start-stop"` with the arguments: `"start"` or `"stop"`. This will start sending a monkey fact every hour into the channel it was used in.
Use `"/time_difference"` to find the difference between the current date and a specific date or two specific dates. You can see the format required when using the command.
Use `"/Bug_report"` to submit a bug report related to my operation.
Use `"/recommendation_report"` to submite a recommendation for this bot.


Enjoy using the bot! P.S. Only you can see this message.
'''

####end of variables 



#### Functions

# Bug Report and formating for the text file stored locally.
async def Bug_report_txt(guild_name, guild_id, user_display_name,user_id,bug):
    with open("C:/Users/ADMIN/Desktop/Discord-Bot-BugReport/bug_reports.txt", "a",encoding='utf-8') as file:
        file.write(f"""

#############################################################
Guild Name: {guild_name}  |  Guild ID: {guild_id}
User Display Name: {user_display_name}  |  User ID: {user_id}
------------------------------------------------------------

Bug Report: 
{bug} 

------------------------------------------------------------
End of Report for {user_display_name}

""")
    # await sendDm() # Try testing this inside of this file, im not sure if it will work because its not running under the main file where the bot is hosted. If it doesnt work its not really that big of a deal to impliment


# Recomendation report template for the file on host computer. I could likely merge this function with sendDm() and Bug_report_txt(). Something for a different day though. 
def Recommendation_Report_txt(guild_name, guild_id, user_display_name,user_id,recommendation):
    with open("C:/Users/ADMIN/Desktop/Discord-Bot-BugReport/recommendations.txt", "a",encoding='utf-8') as file:
        file.write(f"""

#############################################################
Guild Name: {guild_name}  |  Guild ID: {guild_id}
User Display Name: {user_display_name}  |  User ID: {user_id}
------------------------------------------------------------

Recommendation: 
{recommendation} 

------------------------------------------------------------
End of Recommendation for {user_display_name}

""")
    
    
# Sends a DM to me so I know that a new bug has been reported. This section needs to be formated better, i need to be able to use this for more situations. Consdier creating varaibles for each response, will make code prettyish.
async def sendDm(guild_name, guild_id, user_display_name=None,user_id=None,bug=None,user=None,choice=None):
    if choice == 1:
        await user.send(f"""Hey, a new bug report has been added! 
UserID= `{user_id}` Display Name= `{user_display_name}`\nGuild ID= `{guild_id}` Guild Name= `{guild_name}`

Their report is as follows:
 ```
{bug}
```
    """)
    elif choice == 2:
        await user.send(f"I have been added to a new server! `{guild_name} {guild_id}`")
    elif choice == 3:
        await user.send(f"A new recommendation has been added by user {user_display_name} id -> {user_id}")



#Checks time based on 1 or two dates. It will use the current date for date2 if not passed to the function.
def discord_time_check(date1, date2=None):
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y", "%Y/%m/%d"]
    date1_obj = None
    date2_obj = None
    
    for format in formats:
        try:
            date1_obj = datetime.strptime(date1, format)
            break
        except ValueError:
            continue
    else:
        return "Invalid date format for date1, please use one of these formats >>> `YYYY-MM-DD, MM/DD/YYYY, MM-DD-YYYY, YYYY/MM/DD`"
    
    if date2:
        for format in formats:
            try:
                date2_obj = datetime.strptime(date2, format)
                break
            except ValueError:
                continue
        else:
            return "Invalid date format for date2, please use one of these formats >>> `YYYY-MM-DD, MM/DD/YYYY, MM-DD-YYYY, YYYY/MM/DD`"
    else:
        date2_obj = datetime.now()
    
    diff = date2_obj - date1_obj
    years = int(diff.days / 365)
    months = int((diff.days % 365) / 30)
    days = int((diff.days % 365) % 30)
    
    return "Time difference between " + date1 + " and " + (date2 if date2 is not None else "current date") + " is about: " + str(years) + " years, " + str(months) + " months, " + str(days) + " days"

# Gets the current time based on the value passed to the function.        
def current_time(choice=5):
    
    if choice == 1:
        return now.strftime("%Y")
    elif choice == 2:
        return now.strftime("%m")
    elif choice == 3:
        return now.strftime("%d")
    elif choice == 4:
        return now.strftime("%H:%M:%S")
    elif choice == 5:
        return now.strftime("%m/%d/%Y, %H:%M:%S")
    
#Displays tkinter gui on screen
def Display():
    obj = Tk()
    obj.title("Discord Banana Bot")
    obj.mainloop()

# Gets a fact from the fact lists
def get_fact(choice):
    if choice == "1":
        choice=banana_facts
    elif choice == "2":
        choice = Plantain_Facts
    elif choice == "3":
        choice = Pear_Facts
    elif choice == "4":
        choice = Tomato_Facts
    else:
        return "There was an issue with your selection, please try again."

# ensures that if the command is run twice, the fact will not be duplicated. This is pretty much a temporary fix as im not sure how to fix it in other ways.
    Main_Fact = random.choice(choice)
    Main_Fact_c = Main_Fact
    if Main_Fact == Main_Fact_c:
        Main_Fact = random.choice(choice)
    return Main_Fact
