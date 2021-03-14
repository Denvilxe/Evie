from Luna import ubot, abot, CMD_HELP
from Luna.events import register
import asyncio, os

@register(pattern="^/au (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/au {ok}")
          await asyncio.sleep(12)
          response = await bot_conv.get_response()
          await event.reply(response)
time = "69"
@register(pattern="^/key (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/key {ok}")
          await asyncio.sleep(8)
          response = await bot_conv.get_response()
          await event.delete()
          await event.reply(response)
          if "Invalid" in response.text:
                reply = f"SK Key : {ok}\n"
                reply += "Result: Invalid API Key"
                reply += "RESPONSE: ❌Invalid Key❌"
                reply += f"Time: {time}"
                reply += f"Checked By **{fname}**"
          else:
                reply = f"SK Key :{ok}"
          await event.reply(reply)        


@register(pattern="^/ss (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/ss {ok}")
          await asyncio.sleep(15)
          response = await bot_conv.get_response()
          await event.reply(response)

@register(pattern="^/pp (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/pp {ok}")
          await asyncio.sleep(14)
          response = await bot_conv.get_response()
          await event.reply(response)

@register(pattern="^/ch (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/ch {ok}")
          k = await event.reply("**Wait for Result.**")
          await asyncio.sleep(18)
          response = await bot_conv.get_response()
          await event.reply(response)

@register(pattern="^/bin (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/bin {ok}")
          await asyncio.sleep(5)
          response = await bot_conv.get_response()
          await event.reply(response)

@register(pattern="^/c3 (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with abot.conversation("@Gayroebot") as bot_conv:
          await bot_conv.send_message(f"/c3 {ok}")
          response = await bot_conv.get_response()
          await event.reply(response)


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /au <cc>: Stripe Auth given CC
 - /pp <cc>: Paypal 1$ Guest Charge
 - /ss <cc>: Speedy Stripe Auth
 - /ch <cc>: Check If CC is Live
 - /C3 <bin>: Check If Bin Is 3D Redirect
 - /bin <bin>: Gather's Info About the bin
 - /key <sk>: Checks if Sk_Key is Live
More Gates Soon...

**Note:** Format of cc is ccnum|mm|yy|cvv
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
