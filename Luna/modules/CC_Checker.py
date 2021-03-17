from Luna import ubot, CMD_HELP, abot
from Luna.events import register
import asyncio, os
import datetime

@register(pattern="^/gen (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with abot.conversation("@ccgen_robot") as bot_conv:
          await bot_conv.send_message("/generate")
          await bot_conv.send_message("💳Credit Card Generator💳")
          await asyncio.sleep(2)
          await bot_conv.send_message(ok)
          await asyncio.sleep(1)
          response = await bot_conv.get_response()
          await asyncio.sleep(1)
          await response.click(text='✅Generate✅')
          await asyncio.sleep(2)
          text = "**Generated Cards**"
          gen = await bot_conv.get_response()
          k = gen.split(sep=' ')
          for cc in k:
              text += f"{cc}"
          await tbot.send_message(event.chat_id, text)
@register(pattern="^/key (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      ok = event.pattern_match.group(1)
      start_time = datetime.datetime.now()
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/key {ok}")
          await asyncio.sleep(6)
          response = await bot_conv.get_response()
          await event.delete()
          end_time = datetime.datetime.now()
          pingtime = end_time - start_time
          time = str(round(pingtime.total_seconds(), 2)) + "s"
          if "Invalid" in response.text:
                reply = f"SK Key : {ok}\n"
                reply += "Result: Invalid API Key\n"
                reply += "RESPONSE: ❌Invalid Key❌\n"
                reply += f"Time: {time}\n"
                reply += f"Checked By **{fname}**"
          elif "Test" in response.text:
                reply = f"SK Key : sk_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                reply += "Result: Test mode Key\n"
                reply += "RESPONSE: ❌Test Mode Key❌\n"
                reply += f"Time: {time}\n"
                reply += f"Checked By **{fname}**"
          elif "Valid" in response.text:
                reply = f"SK Key : sk_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                reply += "Result: LIVE\n"
                reply += "RESPONSE: ✅Valid Key\n"
                reply += f"Time: {time}\n"
                reply += f"Checked By **{fname}**"
          else:
                reply = "Error, Report @LunaBotSupport"
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
