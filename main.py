import selfcord
import requests
import json
from random import choice as rchoice
import os
import sys
import time

endpoint_url = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags=%s&json=1&limit=1000&pid=%s"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
error_message = '<?xml version="1.0" encoding="UTF-8"?>'

tags_list = [
    "-loli",
    "-rape"
]

shadowBackup = {

}

# Create a string with all the tags with either "+" or "-" for rule34 api
def formatTags(tags):
    return "".join("+" + i for i in tags)

def response_handler(response_item):
    # Check if the status code is not 200 (invalid)
    if response_item.status_code != 200:
        return False

    # Check if it has an error or not due to the lack of content
    if error_message in response_item.content.decode() or response_item.content.decode() == "":
        return False

    # Returns the formatted json content
    return json.loads(response_item.content.decode())


# Handles the request
def request_handler(tag, page):
    if (tag + str(page)) in shadowBackup.keys():
        return shadowBackup[tag + str(page)]

    # Formats the url so it works I guess
    formed_url = endpoint_url % (tag, page)

    # Makes a request to the endpoint url
    endpoint_request = requests.get(formed_url, headers=headers)

    # Returns the response from "response_handler()"
    response = response_handler(endpoint_request)

    shadowBackup[tag + str(page)] = response

    return response

bot = selfcord.Bot(prefixes="?")

#cmdname = ["amongus","balls","catboy","fem","fp","gay","genshin","goku","help","hentai","jmale","jojo","male","mario","mfurry","mha","minecraft","onepiece","random","roblox","shit"]

def stop_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.on("message")
async def on_message(message):
    if message.author.id in whitelist:
        await message.channel.send("?"+message.content)

@bot.on("ready")
async def ball(time):
    print(f"Connected To {bot.user}\n Startup took {time:0.2f} seconds")

@bot.cmd(description="furry porn")
async def furry(ctx):
    cTag = ["furry"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="gay porn :skull:")
async def gay(ctx):
    cTag = ["gay"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="femboy rule34")
async def fem(ctx):
    cTag = ["femboy"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="jojo rule34")
async def jojo(ctx):
    cTag = ["jojo's_bizarre_adventure"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="b a l l s")
async def balls(ctx):
    cTag = ["balls"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="male cmd but better ig")
async def jmale(ctx):
    cTag = ["male_only"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="rule34 of males")
async def male(ctx):
    cTag = ["male"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="catboy rule34")
async def catboy(ctx):
    cTag = ["catboy"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="male furry rule34")
async def mfurry(ctx):
    cTag = ["furry_male"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="mario rule34")
async def mario(ctx):
    cTag = ["mario"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="my hero rule34")
async def mha(ctx):
    cTag = ["my_hero_academia"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="hentai")
async def hentai(ctx):
    cTag = ["hentai"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="shit rule34 (why does this even exist)")
async def shit(ctx):
    cTag = ["shit"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="goku rule34")
async def goku(ctx):
    cTag = ["goku"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="genshin rule34")
async def genshin(ctx):
    cTag = ["genshin_impact"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="amongus rule34")
async def amongus(ctx):
    cTag = ["among_us"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="one piece rule34")
async def onepiece(ctx):
    cTag = ["one_piece"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="roblox rule34")
async def roblox(ctx):
    cTag = ["roblox"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="gets random rule34 from the rule34.xxx homepage")
async def random(ctx):
    cTag = [""]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="minecraft rule34")
async def minecraft(ctx):
    cTag = ["minecraft"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="villager rule34")
async def villager(ctx):
    cTag = ["villager"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="military rule34 ig")
async def military(ctx):
    cTag = ["military"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="vegeta rule34")
async def vegeta(ctx):
    cTag = ["vegeta"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="pokemon rule34")
async def pokemon(ctx):
    cTag = ["pokemon"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="gay sex")
async def gsex(ctx):
    cTag = ["gay_sex"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="ayo?")
async def cum(ctx):
    cTag = ["cum"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="god of war rule34")
async def gow(ctx):
    cTag = ["god_of_war"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="santa rule34")
async def santa(ctx):
    cTag = ["santa_hat"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="feet i guess")
async def feet(ctx):
    cTag = ["feet"]
    while True:
        await ctx.send(rchoice(request_handler(formatTags([*tags_list, *cTag]), 1))['file_url'])

@bot.cmd(description="gives the bots latency")
async def ping(ctx):
    await ctx.channel.send(f"The bots ping is **{round(bot.latency)}** ms!")

@bot.cmd(description="spams text (not rule34)")
async def spam(ctx, *, text:str):
    while True:
        await ctx.send(text)

@bot.cmd(description="Purges the rule34 images")
async def purge(ctx, amount: int=None):
        await ctx.purge(amount)

@bot.cmd(description="stops the bot from sending rule34")
async def stop(ctx):
        await ctx.send('Stopping...')
        stop_bot()

@bot.cmd(description="hides the rule34 but doesnt delete it")
async def hide(ctx):
    time.sleep(1)
    await ctx.send("E\nE\nE\nE\nE\nE\nE\nE")
    time.sleep(1)
    await ctx.send("E\nE\nE\nE\nE\nE\nE\nE")
    time.sleep(1)
    await ctx.send("E\nE\nE\nE\nE\nE\nE\nE")
    time.sleep(1)
    await ctx.send("E\nE\nE\nE\nE\nE\nE\nE")
    
TOKEN = "YOUR TOKEN HERE"

bot.run(TOKEN)
