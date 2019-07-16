import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Changelog(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def changelog(self,ctx): 
        e = discord.Embed(title=f"A beta update! This has been changed at 14/07/2019. Version: {conf.version}",description='''
```

-Commands that required the user to have "admin" has been changed to "manage_messages"
```
''', color=conf.norm)
        e.set_author(name=f"The Changelog for {conf.name}.",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
