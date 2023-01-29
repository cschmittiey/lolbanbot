import discord
import asyncio
import os

intents = discord.Intents.default()

intents.members = True
intents.guilds = True
intents.guild_messages = True
intents.presences = True

client = discord.Client(intents=intents)

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

async def get_activity():
    for guild in client.guilds:
        for member in guild.members:
            activity = member.activity
            if activity:
                print(f"{member.name} is playing {activity.name}")
                if activity.name.lower() == "league of legends":
                    await member.send("You have been playing League of Legends. You are now banned.")
                    channel = discord.utils.get(client.get_all_channels(), name="under-the-concrete-ceiling")
                    await channel.send(f"banning {member.name} for playing League. see ya 👋")
                    await member.ban(delete_message_days=0, reason="playing league")


    await asyncio.sleep(7200) # run the task every 2 hours.

@client.event

async def on_ready():
    channel = discord.utils.get(client.get_all_channels(), name="under-the-concrete-ceiling")
    while True:
        await get_activity()

client.run(TOKEN)
