from Luna import ubot, CMD_HELP
from Luna.events import bot as register
import asyncio, os
import datetime

@register(pattern="^/gen (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      m = await event.reply('Generating CC...Pls Weit.')
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
          text = "****Generated Cards:****\n"
          gen = await bot_conv.get_response()
          card = gen.text
          text = f'{card.splitlines()[0]}\n'
          text += f'{card.splitlines()[1]}\n'
          text += f'{card.splitlines()[2]}\n'
          text += f'{card.splitlines()[3]}\n'
          text += f'{card.splitlines()[4]}\n'
          text += f'{card.splitlines()[5]}\n'
          text += f'\nGenerated By: **{fname}**'
          await m.edit(text)

@register(pattern="^/key (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      ok = event.pattern_match.group(1)
      k = await event.reply("**Wait for Result.**")
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
                reply = "Error, Report @Aniebotsupports"
          await k.edit(reply)        


@register(pattern="^/ss (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      ok = event.pattern_match.group(1)
      k = await event.reply("**Wait for Result.**")
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/ss {ok}")
          await asyncio.sleep(9)
          response = await bot_conv.get_response()
          if "Try again after" in response.text:
                 await k.edit(response)
                 return
          if "Your date is invalid" in response.text:
                 await k.edit('Format Wrong or invalid cc.')
                 return
          res = response.text
          text = f'{res.splitlines()[0]}\n'
          text += f'{res.splitlines()[1]}\n'
          text += f'{res.splitlines()[2]}\n'
          text += f'{res.splitlines()[3]}\n'
          text += f'{res.splitlines()[4]}\n'
          text += f'{res.splitlines()[5]}\n'
          text += f'{res.splitlines()[6]}\n'
          text += f'Checked By **{fname}**'
          await k.edit(text)

@register(pattern="^/pp (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      ok = event.pattern_match.group(1)
      k = await event.reply("**Wait for Result.**")
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/pp {ok}")
          await asyncio.sleep(14)
          response = await bot_conv.get_response()
          if "Try again after" in response.text:
                 await k.edit(response)
                 return
          if "Your date is invalid" in response.text:
                 await k.edit('Format Wrong or invalid cc.')
                 return
          res = response.text
          text = f'{res.splitlines()[0]}\n'
          text += f'{res.splitlines()[1]}\n'
          text += f'{res.splitlines()[2]}\n'
          text += f'{res.splitlines()[3]}\n'
          text += f'{res.splitlines()[4]}\n'
          text += f'{res.splitlines()[5]}\n'
          text += f'{res.splitlines()[6]}\n'
          text += f'Checked By **{fname}**'
          await k.edit(text)

@register(pattern="^/ch (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/ch {ok}")
          k = await event.reply("**Wait for Result.**")
          await asyncio.sleep(18)
          response = await bot_conv.get_response()
          if "Try again after" in response.text:
                 await k.edit(response)
                 return
          if "Your date is invalid" in response.text:
                 await k.edit('Format Wrong or invalid cc.')
                 return
          res = response.text
          text = f'{res.splitlines()[0]}\n'
          text += f'{res.splitlines()[1]}\n'
          text += f'{res.splitlines()[2]}\n'
          text += f'{res.splitlines()[3]}\n'
          text += f'{res.splitlines()[4]}\n'
          text += f'{res.splitlines()[5]}\n'
          text += f'{res.splitlines()[6]}\n'
          text += f'Checked By **{fname}**'
          await k.edit(text)

@register(pattern="^/au (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/au {ok}")
          k = await event.reply("**Wait for Result.**")
          await asyncio.sleep(18)
          response = await bot_conv.get_response()
          if "Try again after" in response.text:
                 await event.reply(response)
                 return
          if "Your date is invalid" in response.text:
                 await event.reply('Format Wrong or invalid cc.')
                 return
          res = response.text
          text = f'{res.splitlines()[0]}\n'
          text += f'{res.splitlines()[1]}\n'
          text += f'{res.splitlines()[2]}\n'
          text += f'{res.splitlines()[3]}\n'
          text += f'{res.splitlines()[4]}\n'
          text += f'{res.splitlines()[5]}\n'
          text += f'{res.splitlines()[6]}\n'
          text += f'Checked By **{fname}**'
          await k.edit(text)


@register(pattern="^/bin (.*)")
async def alive(event):
      sender = await event.get_sender()
      fname = sender.first_name
      k = await event.reply("**Wait for Result.**")
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/bin {ok}")
          await asyncio.sleep(5)
          response = await bot_conv.get_response()
          res = response.text
          if "❌" in res:
               text = '🤬❌ INVALID BIN ❌🤬\n'
               text += f'Checked By **{fname}**'
               await k.edit(text)
          else:
               text = f'{res.splitlines()[0]}\n'
               text += f'{res.splitlines()[1]}\n'
               text += f'{res.splitlines()[2]}\n'
               text += f'{res.splitlines()[3]}\n'
               text += f'{res.splitlines()[4]}\n'
               text += f'{res.splitlines()[5]}\n'
               text += f'{res.splitlines()[6]}\n'
               text += f'Checked By **{fname}**'
               await k.edit(text)


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /au <cc>: Stripe Auth given CC
 - /pp <cc>: Paypal 1$ Guest Charge
 - /ss <cc>: Speedy Stripe Auth
 - /ch <cc>: Check If CC is Live
 - /bin <bin>: Gather's Info About the bin
 - /gen <bin>: Generates CC with given bin
 - /key <sk>: Checks if Stripe key is Live
More Gates Soon...

**Note:** Format of cc is ccnum|mm|yy|cvv
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
