# Akane-Bot
Bot template for the *future* Akane Heaven server bot Akane-Bot

Join us here: https://disboard.org/server/1097595817973514302

### Remember to create .env file with the bot_token variable!
.env file requires the following data:

    - bot_token
    - cai_token
    - char_token


The following are optional:

    - activity_type: int
    - bot_token: str
    - guild_id: int
    - log: str
    - owner: str
    - status: str


### The following libraries need to be installed for it to work
#### *These libraries will be also installable using the frozen file*
    - discord.py
    - python-dotenv
    - characterai

### The following code needs to be run after installing the libraries
    playwright install