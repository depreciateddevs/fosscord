import discord
from discord.ext import commands
import psutil
import config
import bot
import datetime
import time
start_time = time.time()

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Shows information about bot instance.')
    async def about(self, ctx):
        em = discord.Embed(title = "About FreeDiscord", description = "This bot is based off of/is the FreeDiscord bot made by SKBotNL, ItsJustLag, recallwhoiam, Quirinus, and antistalker.")
        em.add_field(name = "Website", value = "https://freediscord.ga/")
        em.add_field(name = "Project URL", value = "https://github.com/FreeTechnologies/FreeDiscord/")
        em.add_field(name = "Support server", value = "https://discord.gg/VyNxSt55gj")
        em.add_field(name = "Main bot invite link", value = "https://discord.com/oauth2/authorize?client_id=829158610965495848&permissions=8&scope=bot")
        servers = list(self.bot.guilds)
        serverNumber = len(servers)
        em.add_field(name = "Number of servers this instance is in", value = serverNumber)
        cpuUsage = psutil.cpu_percent()
        em.add_field(name = "CPU usage of host", value = cpuUsage)
        em.add_field(name = "Ping", value = "`"f"{round(self.bot.latency*1000)} ms`")
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        em.add_field(name="Uptime", value=text)
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(General(bot))
