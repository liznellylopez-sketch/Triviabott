import discord
from discord.ext import commands
from discord import app_commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

trivia_questions = [
    {"q": "What game is Mario from?", "a": "super mario"},
    {"q": "Who made Xbox?", "a": "microsoft"},
    {"q": "What game is Link from?", "a": "zelda"}
]
cool_factss =["In the 1830's, ketchup was sold as medicine.","In Switerland, it is illegal to own just one guinea pig, since they haate being alone.","The shortest war in history lasted 38 minutes.","Orcas wear other dead animals as hats"]

weired_factss =["a drunk man threw a bommerang and it hit him in the face so he sued his drunkself and won","Kangaroos can't jump backwards","A man from japan finshed a marathon after 54 years 8 months 6 days 5 hours 32 minuets and 20.3 seconds, "]

Bad_words =["Shit","Fuck","Bitich",]

True_fan_testt =[]
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="trivia_bot", description="Start a trivia question")
async def trivia(interaction: discord.Interaction):
    question = random.choice(trivia_questions)

    await interaction.response.send_message(f"🧠 {question['q']}")

    def check(m):
        return m.author == interaction.user and m.channel == interaction.channel

    try:
        msg = await bot.wait_for("message", check=check, timeout=15)

        if msg.content.lower() == question["a"]:
            await interaction.followup.send("✅ Correct!")
        else:
            await interaction.followup.send(f"❌ Wrong! Answer was: {question['a']}")

    except:
        await interaction.followup.send("⏰ Time's up!")

@bot.tree.command(name="cool_facts")
async def cool_facts(ctx):
    fact=random.choice(cool_factss)
    await ctx.send(f"**Cool Fact:** {fact}")

@bot.tree.command(name="weired_facts")
async def weired_facts(ctx):
    fact=random.choice(weired_factss)
    await ctx.send(f"**Weired Fact:** {fact}")

@bot.event
async def on_message(message):


bot.run(DISCORD_TOKEN)
