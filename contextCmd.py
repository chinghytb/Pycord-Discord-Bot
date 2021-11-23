import discord
import os

bot = discord.Bot()

@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

bot.run(os.environ['token']) #or you can just write `bot.run('YOUR TOKEN HERE')`
