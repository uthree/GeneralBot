import asyncio
import traceback

import discord
import discord.ext.commands as cmd

COGS = [
]

class Bot(cmd.Bot):
    def __init__(self, prefix):
        super().__init__(command_prefix=prefix)

        for cog in COGS:
            try:
                self.load_extension(cog)
            except Exception as e:
                print(f'Failed to load extension {cog}.', file=sys.stderr)
                traceback.print_exc()

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')

    
