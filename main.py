from core.client import AkaneBot

# Create Akane bot
client = AkaneBot('/')

client.remove_command('help')


if __name__ == "__main__":
    # Run bot
    client.run()

