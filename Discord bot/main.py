#started on 1st August
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from discord import app_commands
import random
import asyncio
import yt_dlp as youtube_dl

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

#hello
@bot.command()
async def hello(ctx,user_choice: str = None):
    """Says hello :D"""
    await ctx.send(f"Hello {ctx.author.mention}!")

#Direct message
@bot.command()
async def dm(ctx, *, msg, user_choice: str = None):
    """Sends a direct message"""
    await ctx.author.send(f"You said {msg}")

#reply
@bot.command()
async def reply(ctx,user_choice: str = None):
    """Replies to your message"""
    await ctx.reply("This is a reply to your message!")

#Poll
@bot.command()
async def poll(ctx, *, question,user_choice: str = None):
    """Creates a poll"""
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

#coin toss
@bot.command(name="flip", aliases=["coin", "coinflip"])
async def flip(ctx, user_choice: str = None):
    """Does a coinflip, You can also try to guess!"""
    print(f"\n[DEBUG] Received !flip command from {ctx.author}")  
    
    if user_choice:
        user_choice = user_choice.lower()
        print(f"[DEBUG] User choice: {user_choice}") 

    if user_choice and user_choice not in ["heads", "tails"]:
        print("[DEBUG] Invalid choice detected") 
        await ctx.send("Please type `!flip heads` or `!flip tails`")
        return

    result = random.choice(["heads", "tails"])
    print(f"[DEBUG] Coin result: {result}")  

    if not user_choice:
        message = f"🪙 The coin landed on **{result}**!"
    elif user_choice == result:
        message = f"🎉 Correct! It's **{result}**!"
    else:
        message = f"❌ Wrong! It was **{result}**!"

    print(f"[DEBUG] Sending: {message}")
    await ctx.send(message)

#rps
@bot.command(name="rps", aliases=["rockpaperscissors"])
async def rps(ctx, user_choice: str = None):
    """Play Rock-Paper-Scissors against the bot"""
    print(f"\n[DEBUG] RPS command received from {ctx.author}")  
    
    
    choices = ["rock", "paper", "scissors"]
    
    
    if not user_choice:
        print("[DEBUG] No choice provided") 
        await ctx.send("Please choose: `!rps rock`, `!rps paper`, or `!rps scissors`")
        return
        
    user_choice = user_choice.lower()
    print(f"[DEBUG] User chose: {user_choice}")  
    
    if user_choice not in choices:
        print("[DEBUG] Invalid choice")  
        await ctx.send("❌ Please choose **rock**, **paper**, or **scissors**!")
        return

   
    bot_choice = random.choice(choices)
    print(f"[DEBUG] Bot chose: {bot_choice}")

  
    if user_choice == bot_choice:
        result = "It's a tie! 🤝"
    elif ((user_choice == "rock" and bot_choice == "scissors") or
          (user_choice == "paper" and bot_choice == "rock") or
          (user_choice == "scissors" and bot_choice == "paper")):
        result = "You win! 🎉"
    else:
        result = "I win! 😈"

    
    response = (
        f"**You chose:** {user_choice}\n"
        f"**I chose:** {bot_choice}\n"
        f"**Result:** {result}"
    )
    print(f"[DEBUG] Sending response: {response}") 
    await ctx.send(response)

#MCQ
Medquizzes = { 
    "Following are increased during moderate isotonic exercise EXCEPT": {
        "options": ["A.heart rate","B.cardiac output", "C.systolic blood pressure", "D.peripheral vascular resistance"],
        "answer": "D",
        "Explanation": "None",
    },
    "Isotonic exercise results in ___": {
        "options": ["A.decreased stroke volume", "B.decreased cardiac output", "C.fall in systolic blood pressure", "D.fall in total peripheral resistance"],
        "answer": "D",
        "Explanation": "None",
    },
    "Immediate source of energy for muscle contraction is ___": {
        "options": ["A.CAMP", "B.ATP", "C.ADP", "D.Glycogen"],
        "answer": "B",
        "Explanation": "None",
    },
    "One of the following is decreased during isotonic whole body exercise like swimming?": {
        "options": ["A.respiratory rate", "B.heart rate", "C.total peripheral resistance", "D.systolic blood pressure"],
        "answer": "C",
        "Explanation": "None",
    },
    "Time duration for phosphagen system to provide energy during endurance exercise is": {
        "options": ["A.1.3-1.6 min", "B.8-10 seconds", "C.1.3-1.6 hours", "D.As long as the nutrients last"],
        "answer": "C",
        "Explanation": "None",
    },
    "The type of muscle fibers that fatigue most rapidly is": {
        "options": ["A.slow oxidative fibers", "B.fast oxidative fibers", "C.fast glycolytic fibers", "D.none of the above"],
        "answer": "C",
        "Explanation": "None",
    },
    "Initial Hyperpnoea in exercise is because of": {
        "options": ["A.Hypercapnoea", "B.Hypoxemia", "C.Lactic acidosis", "D.Stimulation of cortex and proprioceptors"],
        "answer": "D",
        "Explanation": "None",
    },
    "Which of the following is not increased during exercise?": {
        "options": ["A.respiratory rate", "B.stroke volume", "C.total peripheral resistance", "D.systolic blood pressure"],
        "answer": "C",
        "Explanation": "None",
    },
    "Integration of the temperature information by the nervous system occurs mainly in the": {
        "options": ["A.Spinal cord", "B.Hypothalamus", "C.Amygdala", "D.Peripheral receptors"],
        "answer": "B",
        "Explanation": "None",
    },
    "Heat sensitive neurons are situated in": {
        "options": ["A.Anterior hypothalamic nuclei", "B.Amygdala", "C.Hippocampus", "D.Anterior thalamic nuclei"],
        "answer": "A",
        "Explanation": "None",
    },
    "Only mechanism of heat loss when surrounding temperature is more than body temperature is": {
        "options": ["A.Conduction", "B.Convection", "C.Radiation", "D.Evaporation"],
        "answer": "D",
        "Explanation": "None",
    },
    "Temperature - Increasing mechanisms when the body is too cold are all EXCEPT": {
        "options": ["A.Skin vasoconstriction", "B.Shivering", "C.Piloerection", "D.Sweating"],
        "answer": "D",
        "Explanation": "None",
    },
    "The temperature of body tissue determines the response of the ___": {
        "options": ["A.Brain", "B.Deep", "C.cutaneous", "D.subcutaneous"],
        "answer": "C",
        "Explanation": "None",
    },
    "Sweat glands are innervated by": {
        "options": ["A.sympathetic adrenergic nerve", "B.sympathetic cholinergic nerve", "C.parasympathetic cholinergic nerve", "D.somatic nerve"],
        "answer": "B",
        "Explanation": "None",
    },
    "In infants, major source of heat production is": {
        "options": ["A.increased muscular activity", "B.brown fat", "C.increased sympathetic activity", "D.feeding"],
        "answer": "B",
        "Explanation": "None",
    },
    "An individual sitting with minimal clothing in a room with air temperature of 21°C and humidity of 80%, the greatest amount of heat is lost by": {
        "options": ["A.Elevated metabolism", "B.Radiation and conduction", "C.Vaporization of sweat", "D.Respiration"],
        "answer": "B",
        "Explanation": "None",
    },
    "Primary motor center for shivering is located in": {
        "options": ["A.Dorsomedial part of posterior hypothalamus", "B.Preoptic area", "C.Anterior hypothalamus", "D.Supraoptic nucleus"],
        "answer": "A",
        "Explanation": "None",
    },
    "When person is suddenly exposed to a heat following mechanism gets activated ": {
        "options": ["A.Cutaneous vasodilation", "B.Cutaneous vasoconstriction", "C.Increased secretion of epinephrin", "D.Increased voluntary activity"],
        "answer": "A",
        "Explanation": "None",
    },
    "The temperature regulating center is located in": {
        "options": ["A.Hypothalamus", "B.Pons", "C.Medulla", "D.Cerebal cortex"],
        "answer": "A",
        "Explanation": "None",
    },
    "Maximum percentage of body heat is lost by which of the following ways?": {
        "options": ["A.radiation and conduction", "B.vaporisation of sweat", "C.respiration", "D.urination and defecation"],
        "answer": "A",
        "Explanation": "None",
    },
    "The shivering centre in humans is located in ": {
        "options": ["A.Posterior hypothalamus", "B.Anterior hypothalamus", "C.Pontine reticular formation", "D.Primary motor cortex"],
        "answer": "A",
        "Explanation": "None",
    },
}

quizzes = {
    "What is the largest planet in our solar system?": {
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
        "answer": "B",
        "Explanation": "Jupiter is more than twice as massive as all other planets combined.",
    },
    "Which country gifted the Statue of Liberty to the United States?": {
        "options": ["A. England", "B. Canada", "C. France", "D. Spain"],
        "answer": "C",
        "Explanation": "France gifted the statue in 1886 to commemorate the alliance during the American Revolution.",
    },
    "What year did World War II end?": {
        "options": ["A. 1943", "B. 1945", "C. 1950", "D. 1939"],
        "answer": "B",
        "Explanation": "The war ended on September 2, 1945, when Japan formally surrendered.",
    },
    "Which element has the chemical symbol 'O'?": {
        "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Oganesson"],
        "answer": "B",
        "Explanation": "Oxygen is essential for human respiration and has atomic number 8.",
    },
    "Who painted the Mona Lisa?": {
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C",
        "Explanation": "Da Vinci painted it between 1503-1519, and it's now displayed in the Louvre.",
    },
    "What is the capital of Australia?": {
        "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
        "answer": "C",
        "Explanation": "Canberra was specially designed as the capital in 1908, located between Sydney and Melbourne.",
    },
    "Which planet is known as the 'Red Planet'?": {
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B",
        "Explanation": "Mars appears red due to iron oxide (rust) on its surface.",
    },
    "Who wrote 'Romeo and Juliet'?": {
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B",
        "Explanation": "Shakespeare wrote this tragic play in the late 16th century.",
    },
    "What is the hardest natural substance on Earth?": {
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Quartz"],
        "answer": "C",
        "Explanation": "Diamond scores 10 on the Mohs hardness scale, the highest possible rating.",
    },
    "Which animal is known as the 'King of the Jungle'?": {
        "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Gorilla"],
        "answer": "C",
        "Explanation": "Lions hold this title despite primarily living in savannas, not jungles.",
    }
}

@bot.command(name="Medquiz ", aliases=["medquiz","medQuiz","MEDQUIZ"])
async def Medquiz(ctx,user_choice: str = None):
    """Asks Medical questions"""
    score = 0
    
    await ctx.send(f"How many questions would you like? (choose between 1-{len(Medquizzes)})")

    def check_num(m):
        return(
            m.author == ctx.author and
            m.channel == ctx.channel and
            m.content.isdigit() and
            1 <= int(m.content) <= len(Medquizzes)
        )
    try:
        num_msg = await bot.wait_for("message", check=check_num, timeout=30.0)
        num_questions = int(num_msg.content)
    except asyncio.TimeoutError:
        await ctx.send("⏰ You took too long to respond!")
        return
    except ValueError:
        await ctx.send(f"❌ Please enter a number between 1-{len(Medquizzes)}!")
        return
        
    
    Random_questions = random.sample(list(Medquizzes.items()), num_questions)
    
    for question, data in Random_questions: 

        options = "\n".join(data["options"])
        message = await ctx.send(
        f"**{question}**\n{options}\n\n"
        "Reply with A, B, C, or D!"
    )
        def check(m):
            return (
                m.author == ctx.author
                and m.channel == ctx.channel
                and m.content.upper() in ["A", "B", "C", "D"]
            )

        try:
            reply = await bot.wait_for("message", check=check, timeout=30.0)
            user_answer = reply.content.upper()

            if user_answer == data["answer"]:
                await ctx.send("✅ Correct!")
                score += 1
            else:
                await ctx.send(f"❌ Wrong! The answer was {data['answer']}")
                await ctx.send(f"The explanation for the answer is: {data['Explanation']}")

        except asyncio.TimeoutError:
            await ctx.send("⏰ Time's up!")
            await ctx.send(f"The answer was {data['answer']}")
            break

    await ctx.send(f"🎯 Quiz complete! Your score: {score}/{len(Random_questions)}")

@bot.command(name="quiz")
async def quiz(ctx,user_choice: str = None):
    """Asks General questions"""
    score = 0
    
    await ctx.send(f"How many questions would you like? (choose between 1-{len(quizzes)})")

    def check_num(m):
        return(
            m.author == ctx.author and
            m.channel == ctx.channel and
            m.content.isdigit() and
            1 <= int(m.content) <= len(quizzes)
        )
    try:
        num_msg = await bot.wait_for("message", check=check_num, timeout=30.0)
        num_questions = int(num_msg.content)
    except asyncio.TimeoutError:
        await ctx.send("⏰ You took too long to respond!")
        return
    except ValueError:
        await ctx.send(f"❌ Please enter a number between 1-{len(quizzes)}!")
        return
        
    
    Random_questions = random.sample(list(quizzes.items()), num_questions)
    
    for question, data in Random_questions: 

        options = "\n".join(data["options"])
        message = await ctx.send(
        f"**{question}**\n{options}\n\n"
        "Reply with A, B, C, or D!"
    )   

        def check(m):
            return (
                m.author == ctx.author
                and m.channel == ctx.channel
                and m.content.upper() in ["A", "B", "C", "D"]
            )

        try:
            reply = await bot.wait_for("message", check=check, timeout=30.0)
            user_answer = reply.content.upper()

            if user_answer == data["answer"]:
                await ctx.send("✅ Correct!")
                score += 1
            else:
                await ctx.send(f"❌ Wrong! The answer was {data['answer']}")
                await ctx.send(f"The explanation for the answer is: {data['Explanation']}")

        except asyncio.TimeoutError:
            await ctx.send("⏰ Time's up!")
            await ctx.send(f"The answer was {data['answer']}")
            break

    await ctx.send(f"🎯 Quiz complete! Your score: {score}/{len(Random_questions)}")

#yt search
yt_search_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'extract_flat': True,
    'default_search': 'ytsearch3',
    'noplaylist': True
}

@bot.command(name="yt", aliases=["youtube", "search"])
async def youtube_search(ctx, *, query):
    """Search YouTube and return links"""
    try:
        async with ctx.typing():
            with youtube_dl.YoutubeDL(yt_search_opts) as ydl:
                info = ydl.extract_info(f"ytsearch3:{query}", download=False)
                
                if not info or 'entries' not in info:
                    return await ctx.send("🔍 No results found!")
                
                results = info['entries']
                if not results:
                    return await ctx.send("🔍 No videos found!")
                
                message = "**YouTube Search Results:**\n"
                for i, video in enumerate(results, 1):
                    message += f"{i}. [{video['title']}](https://youtu.be/{video['id']})\n"
                
                await ctx.send(message)
                
    except Exception as e:
        await ctx.send(f"❌ Error: {str(e)}")
        print(f"Search error: {e}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)