import discord

from core.client import AkaneBot

# Create Akane bot
client = AkaneBot('/')

client.remove_command('help')


@client.command(pass_context=True)
async def help(ctx):
    user = ctx.message.author
    embed = discord.Embed()

    # Set bot author
    embed.set_author(name="_ccr", url="https://github.com/ccr-x", icon_url="https://avatars.githubusercontent.com/u/32170529?v=4")

    await user.send(user, embed=embed)


@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hi")


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send("pong")


@client.command(pass_context=True)
async def finale(ctx):
    await ctx.send("Hey there! Now that a command has been ran, you should be able to get your Active Developer badge on https://discord.com/developers/active-developer. \n"
                   "If it doesn't let you get your badge, check again in 24 hours.")

if __name__ == "__main__":
    # Run bot
    client.run()
