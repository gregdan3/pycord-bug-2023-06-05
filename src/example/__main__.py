import asyncio
from discord.ext import commands

TOKEN = "YOUR_TOKEN"
LOOP = asyncio.new_event_loop()
BOT = commands.Bot(loop=LOOP)


def main():
    BOT.load_extension(f"example.cogs.working")
    BOT.load_extension(f"example.cogs.broken")
    BOT.run(TOKEN)


if __name__ == "__main__":
    main()
