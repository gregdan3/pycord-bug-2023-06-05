# Pycord documentation fault

## Steps to Reproduce

1. Set up a cog with a task [as the documentation specifies](https://docs.pycord.dev/en/stable/ext/tasks/index.html#recipes)
2. Construct the bot with your own event loop:

```py
LOOP = asyncio.new_event_loop()
BOT = commands.Bot(
    loop=LOOP,
    command_prefix="/",
)
```

3. Run the bot: `pdm run python -m example` or `pdm run python ./src/example/__main__.py `
4. Observe that BrokenCog never logs after it initializes

Also note that removing the user-added event loop fixes the issue, but may not be desirable to some users needing an event loop for other work before they initialize the bot.
