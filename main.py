import discord

from core.client import AkaneBot

# Create Akane bot
client = AkaneBot(',')

client.remove_command('help')


@client.command(pass_context=True)
async def help(ctx):
    user = ctx.message.author
    embed = discord.Embed()

    # Set bot author
    embed.set_author(name="_ccr", url="https://github.com/ccr-x", icon_url="https://avatars.githubusercontent.com/u/32170529?v=4")

    await user.send(user, embed=embed)


@client.command(pass_context=True)
async def bump(ctx):
    await ctx.send("/images waifu ")


if __name__ == "__main__":
    # Run bot
    client.run()
