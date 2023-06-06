from discord.ext import tasks, commands


class BrokenCog(commands.Cog):
    """
    Cog prepared as the docs specify in recipe #1:
    https://docs.pycord.dev/en/stable/ext/tasks/index.html#recipes

    This does not execute past `__init__` because `self.printer.start()` produces an `asyncio.Task`
    """

    def __init__(self):
        self.index = 0
        self.printer.start()
        print("Broken cog initialized")

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print("Broken Cog: %s" % self.index)
        self.index += 1
