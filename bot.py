import discord
from discord.ext import commands

#   PowerShell Commands to Run
#   Stop-Process -Name "pythonw"
#   pythonw bot.py

# Bot token
TOKEN = 'NOPE'

# Prefix for bot commands
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# List of trigger words and corresponding responses
trigger_responses = {
    "binary": "[Halt!](https://tenor.com/view/hammer-gif-23464742) Criminal Scum! No B*nary Hacking Allowed.",
    "team aqua" : "Expand the Sea!",
    "team magma" : "Blasphemy! Never speak that name here.",
    "Groudon" : "A False god!",
    "Kyogre"  : "Kyogre, Praise be!",
    "Rayquaza"  : "Stupid Snake...",
    "Kanto" : "Ugh...",
    "Hoenn" : "\"7/10 Not Enough Water.\"",
    "just rectangles" : "Kanto man, smh",
    "Expand the Sea" : "<:expandingthesea:1161012421138325645>",
    "Expanding the Sea" : "<:expandingthesea:1161012421138325645>",
}

# Event: Bot is ready
@bot.event
async def on_ready():
    await load_cog()
    print(f'Logged in as {bot.user}')

# Event: Message received
@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore messages from the bot itself
        return
    
    # Check if any trigger word is present in the message
    for trigger, response in trigger_responses.items():
        if trigger.lower() in message.content.lower():
            await message.channel.send(response)
            break  # Exit loop after sending one response

    await bot.process_commands(message)  # Process other commands

async def load_cog():
    try:
        await bot.load_extension('aqua_commands')
        print("Cog loaded successfully!")
    except Exception as e:
        print(f"Failed to load cog: {e}")

# Run the bot
bot.run(TOKEN)
