import discord
from discord.ext import commands
from discord_slash import SlashCommand

# bot token here
TOKEN = "BOT_TOKEN_HERE"

# Create an instance of the Discord client
bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)  # Add this line

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")
    # Set status (example: playing a game)
    activity = discord.Game(name="Watching for e/info")
    await bot.change_presence(activity=activity)

@slash.slash(name="send_dm", description="Send a message to a mentioned user")
async def send_dm(ctx, member: discord.Member, *, message: str):
    try:
    # Send message to the mentioned user
        await member.send(message)
        await ctx.send(f"Message sent to {member.display_name}!")
    except discord.NotFound:
        await ctx.send("User not found.")
    except discord.Forbidden:
        await ctx.send(f"I do not have permission to send a message to {member.display_name}.")

from discord import Embed

# help command
@slash.slash(name="help", description="Shows all Commands in the Bot")
async def _eingebettet(ctx): 
    # Embed for Help command
    embed = Embed(title="🔰Commands", description="**/dm** Send a message to a mentioned user", color=0x00ff00)
    embed.add_field(name="Feldname", value="Feldwert", inline=False)
    await ctx.send(embed=embed)



# Start the bot
bot.run(TOKEN)
