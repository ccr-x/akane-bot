import discord
from main import client


@client.command(name="help", description="Displays all commands that you can use *WIP*", pass_context=True)
async def help(ctx):
    user = ctx.message.author
    embed = discord.Embed()

    # Set bot author
    embed.set_author(name="_ccr", url="https://github.com/ccr-x", icon_url="https://avatars.githubusercontent.com/u/32170529?v=4")

    await user.send(user, embed=embed)


@client.command(name="hello", description="Say Hi to our one and only beloved", pass_context=True)
async def hello(ctx):
    await ctx.send("Hi")


@client.command(name="talk", description="Talks with Akane herself", pass_context=True)
async def talk(ctx):
    message = ctx.message.content
    message = message.replace("/talk ", ctx.message.author.name + ": ")
    data = ""
    async with ctx.typing():
        data = await client.ai_client.chat.send_message('D8tGHd25fa20HnyaQYqMjPQr46hpqFyR8dwmQnL4wiA', message)

    message = data['replies'][0]['text']

    await ctx.send(message)