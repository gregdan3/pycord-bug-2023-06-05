# STL
import os
import asyncio

# PDM
from discord.ext import commands

TOKEN = "YOUR_TOKEN"
LOOP = asyncio.new_event_loop()
BOT = commands.Bot(
    loop=LOOP,
    command_prefix="/",
)


@BOT.event
async def on_ready():
    for index, guild in enumerate(BOT.guilds):
        print("{}. {}".format(index + 1, guild.name))


def load_extensions():
    cogs_path = os.path.dirname(__file__) + "/cogs/"
    for cogname in sorted(os.listdir(cogs_path), key=len):
        path = cogs_path + cogname
        if not os.path.isdir(path):
            continue
        if not ("__init__.py" in os.listdir(path)):
            continue
        print("Loading cog %s" % cogname)
        BOT.load_extension(f"example.cogs.{cogname}")


def main():
    load_extensions()
    BOT.run(TOKEN, reconnect=True)


if __name__ == "__main__":
    main()
