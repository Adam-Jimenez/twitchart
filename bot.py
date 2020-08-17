from twitchbot.bots import BaseBot
from twitchbot import Command
from message_queue import message_queue

def valid_hex_color(s):
    valid=set("0123456789abcdefABCDEF")
    return len(s)==7 and s[0]=="#" and all(c in valid for c in s[1:])

def hex_to_rgb(hex):
    h=hex.lstrip("#")
    h=tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return h

@Command('paint')
async def cmd_function(msg, *args):
    if len(args)==3 and args[0].isdigit() and args[1].isdigit() and valid_hex_color(args[2]):
        x=int(args[0])
        y=int(args[1])
        color=hex_to_rgb(args[2])
        print(x,y,color) # validate coordinates and color
        message_queue.put((x,y,color))
        await msg.reply("Success!")
    else:
        await msg.reply("Invalid params")

def run_bot():
    BaseBot().run()
