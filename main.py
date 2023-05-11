import selfcord
import requests
import json
from random import choice as rchoice
import os
import sys

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
  """Stops The Bot"""
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.on("ready")
async def ball(time):
    print(f"Connected To {bot.user}\n Startup took {time:0.2f} seconds")

@bot.cmd(description="furry porn")
async def furry(ctx):
    cTag = ["furry"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="gay porn :skull:")
async def gay(ctx):
    cTag = ["gay"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="femboy rule34")
async def fem(ctx):
    cTag = ["femboy"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="jojo rule34")
async def jojo(ctx):
    cTag = ["jojo's_bizarre_adventure"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="b a l l s")
async def balls(ctx):
    cTag = ["balls"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="male cmd but better ig")
async def jmale(ctx):
    cTag = ["male_only"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="rule34 of males")
async def male(ctx):
    cTag = ["male"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="catboy rule34")
async def catboy(ctx):
    cTag = ["catboy"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="male furry rule34")
async def mfurry(ctx):
    cTag = ["furry_male"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="mario rule34")
async def mario(ctx):
    cTag = ["mario"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="my hero rule34")
async def mha(ctx):
    cTag = ["my_hero_academia"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="hentai")
async def hentai(ctx):
    cTag = ["hentai"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="shit rule34 (why does this even exist)")
async def shit(ctx):
    cTag = ["shit"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="goku rule34")
async def goku(ctx):
    cTag = ["goku"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="genshin rule34")
async def genshin(ctx):
    cTag = ["genshin_impact"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="amongus rule34")
async def amongus(ctx):
    cTag = ["among_us"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="one piece rule34")
async def onepiece(ctx):
    cTag = ["one_piece"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="roblox rule34")
async def roblox(ctx):
    cTag = ["roblox"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="gets random rule34 from the rule34.xxx homepage")
async def random(ctx):
    cTag = [""]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="minecraft rule34")
async def minecraft(ctx):
    cTag = ["minecraft"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="villager rule34")
async def villager(ctx):
    cTag = ["villager"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="military rule34 ig")
async def military(ctx):
    cTag = ["military"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="vegeta rule34")
async def vegeta(ctx):
    cTag = ["vegeta"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="pokemon rule34")
async def pokemon(ctx):
    cTag = ["pokemon"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="gay sex")
async def gsex(ctx):
    cTag = ["gay_sex"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="ayo?")
async def cum(ctx):
    cTag = ["cum"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="god of war rule34")
async def gow(ctx):
    cTag = ["god_of_war"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="santa rule34")
async def santa(ctx):
    cTag = ["santa_hat"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="feet i guess")
async def feet(ctx):
    cTag = ["feet"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="harry potter r34")
async def harrypotter(ctx):
    cTag = ["harry_potter"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="r34 of lesbians")
async def lesbian(ctx):
    cTag = ["lesbian"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="jujutsu kaisen r34")
async def gojo(ctx):
    cTag = ["jujutsu_kaisen"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="naruto r34")
async def naruto(ctx):
    cTag = ["naruto"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="demon slayer r34")
async def demonslayer(ctx):
    cTag = ["demon_slayer"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="footjob ig")
async def footjob(ctx):
    cTag = ["footjob"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="undertale r34")
async def undertale(ctx):
    cTag = ["undertale"]
    response = request_handler(formatTags([*tags_list, *cTag]), 1)
    if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
    else:
                print("Error: Invalid response")

@bot.cmd(description="something u dont have lmao")
async def bigpp(ctx):
        cTag = ["big_penis"]
        response = request_handler(formatTags([*tags_list, *cTag]), 1)
        if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
        else:
            print("Error: Invalid response")

@bot.cmd(description="subway surfers r34")
async def subway(ctx):
        cTag = ["subway_surfers"]
        response = request_handler(formatTags([*tags_list, *cTag]), 1)
        if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
        else:
            print("Error: Invalid response")

@bot.cmd(description="helluva boss r34")
async def helluva(ctx):
        cTag = ["helluva_boss"]
        response = request_handler(formatTags([*tags_list, *cTag]), 1)
        if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
        else:
            print("Error: Invalid response")

@bot.cmd(description="one punch man r34")
async def opm(ctx):
        cTag = ["saitama"]
        response = request_handler(formatTags([*tags_list, *cTag]), 1)
        if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
        else:
            print("Error: Invalid response")

@bot.cmd(description="looney tunes r34")
async def looney(ctx):
        cTag = ["looney_tunes"]
        response = request_handler(formatTags([*tags_list, *cTag]), 1)
        if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
        else:
            print("Error: Invalid response")

@bot.cmd(description="gravity falls r34")
async def gfalls(ctx):
        cTag = ["gravity_falls"]
        response = request_handler(formatTags([*tags_list, *cTag]), 1)
        if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
        else:
            print("Error: Invalid response")

@bot.cmd(description="disney r34 (pls dont sue me disney)")
async def disney(ctx):
        cTag = ["disney"]
        response = request_handler(formatTags([*tags_list, *cTag]), 1)
        if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
        else:
            print("Error: Invalid response")

@bot.cmd(description="nintedo r34 (pls dont sue me nintendo)")
async def nintendo(ctx):
        cTag = ["nintendo"]
        response = request_handler(formatTags([*tags_list, *cTag]), 1)
        if response:
            while True:
                await ctx.send(rchoice(response)['file_url'])
        else:
            print("Error: Invalid response")

################################### UTILITY COMMANDS ################################################

@bot.cmd(description="gives the bots latency")
async def ping(ctx):
    await ctx.channel.send(f"The bots ping is **{round(bot.latency)}** ms!")

@bot.cmd(description="spams text (not rule34)")
async def spam(ctx, *, text:str):
    while True:
        await ctx.send(text)

@bot.cmd(description="Purges the rule34 images (large num=slower)")
async def purge(ctx, amount: int=None):
        await ctx.purge(amount)

@bot.cmd(description="stops the bot from sending rule34")
async def stop(ctx):
        await ctx.send('Stopping...')
        stop_bot()

@bot.cmd(description="hides the rule34 but doesnt delete it")
async def hide(ctx):
    await ctx.send("E\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE")

TOKEN = "YOUR TOKEN HERE"

bot.run(TOKEN)
