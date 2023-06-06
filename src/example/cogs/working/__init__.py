# LOCAL
from .cog import WorkingCog


def setup(bot):
    bot.add_cog(WorkingCog())
