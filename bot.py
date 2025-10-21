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
    "binary hacking": "[Halt!](https://media.discordapp.net/attachments/991938041314803752/1265005540996681768/yoshi-hammer-slow.gif?ex=669fefb7&is=669e9e37&hm=8999ceec15712dd7775ff3ea10d2420bfdf9b27403d957b8629d1e744f39fa4f&=) Criminal Scum! No B*nary Hacking Allowed.",
    "binary hack": "[Halt!](https://media.discordapp.net/attachments/991938041314803752/1265005540996681768/yoshi-hammer-slow.gif?ex=669fefb7&is=669e9e37&hm=8999ceec15712dd7775ff3ea10d2420bfdf9b27403d957b8629d1e744f39fa4f&=) Criminal Scum! No B*nary Hacking Allowed.",
    "team magma" : "Blasphemy! Never speak that name here.",
    "kanto" : "Ugh... ",
    "Groudon" : "A false god!",
    "Kyogre"  : "Kyogre, Praise be!",
    "Rayquaza"  : "Stupid Snake...",
    "Wallace" : "#NotMyChampion",
    "Radical Red" : "<:hmmsuda:1066946331937087518>",
    "just rectangles" : "Kanto man, smh",
    "Mt Moon" : "Turd blocks, shit bricks",
    "Wally" : "Who?",
    "Mt. Moon" : "Turd blocks, shit bricks",
    "Expand the Sea" : "<:expandingthesea:1161012421138325645>",
    "Expanding the Sea" : "<:expandingthesea:1161012421138325645>",
    "1226444053739208774" : "Who dares summon me?!\nInsolent fools...",
    "VGC" : "https://discord.com/channels/976252009114140682/1201226013716250694",
    "smogon" : "https://discord.com/channels/976252009114140682/1201226013716250694",
    "pokemon showdown" : "https://discord.com/channels/976252009114140682/1201226013716250694",
    "showdown" : "https://discord.com/channels/976252009114140682/1201226013716250694",
    "/r/PokemonROMhacks" : "Completely Normal Grunt wants to make sure that this discussion really needs to be had here. If this subreddit link is drama related, at least move the conversation to https://discord.com/channels/976252009114140682/1186086211815735356.",
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
    if not message.channel.name in ["pokemon", "memes", "battle-workshop"]:
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
