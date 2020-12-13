import discord
from redbot.core import commands
from redbot.core.utils import AsyncIter
from datetime import datetime, timedelta

class FancyUptime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

async def setup(bot):
  fu = FancyUptime(bot)
  global _old_uptime
  _old_uptime = bot.get_command("uptime")
  if _old_uptime:
      bot.remove_command(_old_ping.name)
  bot.add_cog(fu)
       
  def cog_unload(self):
    global _old_uptime
    if _old_uptime:
      try:
        self.bot.remove_command("uptime")
      except Exception as error:
        log.info(error)
      self.bot.add_command(_old_uptime)
      return

  @commands.command()
  async def uptime(self, ctx: commands.Context):
      """Shows [botname]'s uptime."""
      since = ctx.bot.uptime.strftime("%A the %d of %B, %Y")
      delta = datetime.datetime.utcnow() - self.bot.uptime
      uptime_str = humanize_timedelta(timedelta=delta) or _("Less than one second")
      bot = ctx.bot.user.name
      e = discord.Embed(title=f"{bot}'s Uptime",
                        description=(
                          f"{bot} has been up since **{timestamp}**\n",
                          f"Therefore, it's been online for **{time_quantity}**."
                        ).format(timestamp=since, time_quantity=uptime_str),
                        colour=discord.Colour.Red())
      await ctx.send(embed=e)