from discord.ext import tasks, commands


class WorkingCog(commands.Cog):
    """
    Cog created with a pattern not specified by the docs
    """

    def __init__(self):
        self.index = 0

    def cog_unload(self):
        self.printer.cancel()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.printer.start()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print("Working Cog: %s" % self.index)
        self.index += 1
