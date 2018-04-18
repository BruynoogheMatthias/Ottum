import discord
import asyncio
import json
import os
import datetime
import codecs
now = datetime.datetime.now()
client = discord.Client()

# @client.event
# async def wait_until_login():
#     await client.change_presence(game=discord.Game(name='Pokémon Ethereal Gates'))
# discord invite: https://discordapp.com/oauth2/authorize?client_id=357093015975624704&scope=bot&permissions=true


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # changelog = "ottum dev 2.0.1\ntrying to put arrays in files"
    changelog = 'Ottum 2.1 redeployed \n'+'current functions are\n'+'Tell people the release date\n'+'Warn people to not use bad words\n'+"badwords are now in a file\n"+"shutdown command for some roles\n"+'easter eggs'
    botDevChannel = discord.Object(370543539748208643)
    tmp = await client.send_message(botDevChannel, changelog)
    botDevChannel = discord.Object(357090198418620418)
    tmp = await client.send_message(botDevChannel, changelog)

@client.event
async def on_message(message):

    dateTriggerList = ["coming out", 'vaporware', "come out", 'game dead', "comes out", "ded gaem", "dead game"]
    goodRoles = ["mod", "admin","dev", 'bot']
    dateTrigger = False
    goodRole = False
    badWordTrigger = False
    triggerword = ""
    i = 0
    while i<len(dateTriggerList):
        triggered=dateTriggerList[i].lower() in message.content

        dateTrigger = triggered or dateTrigger
        i+=1
    i = 0
    # print (dateTrigger)
    with open('./list/badWordList', 'r',encoding='UTF-8') as List:
        fileLen = file_len("./list/badWordList")

        while i<fileLen:
            word = List.readline()
            word = str(word)
            word = word.rstrip("\n")
            if word != "":

                badWordTrigger =word in message.content or badWordTrigger
                if word in message.content:
                    triggerword = triggerword + " " + word


            i+=1




    # for word in badWordList:
    #     badWordTrigger = badWordTrigger or word in message.content
    i = 0
    if message.server is not None:
        while i<len(message.author.roles):
            triggered=(str(message.author.roles[i]).lower()) in goodRoles
            goodRole = triggered or goodRole
            i+=1
    else:
        goodRole = False

    if dateTrigger  and not goodRole and str(message.author) != "Ottum#9851":
        
        logmsg = (str(message.author)+" on "+str(message.server)+" ("+str(message.channel)+") at "+ str(message.timestamp) +" UTC : "+message.content+'\n')
        print(logmsg)
        logmsg = str(logmsg)
       
        await asyncio.sleep(1)
        tmp = await client.send_message(message.channel, 'The game will come out on November 85th, 2091')

    if badWordTrigger:
        
        logmsg = (str(message.author) + " on " + str(message.server) + " (" + str(message.channel) + ") at " + str(
            message.timestamp) + " UTC : " + message.content +'with the word -'+ triggerword+ '- \n')
        print(logmsg)
        logmsg = str(logmsg)
       
        tmp = await client.send_message(message.channel, 'Please watch your language or face the consequences')
    if "fool" in message.content:
        tmp = await client.send_message(message.channel, 'Keep your mouth shut, whippersnapper!')
    if ("merry" in str(message.content).lower() or  "christmas" in str(message.content).lower()) and (now.month == 12 and (now.day == 25 or now.day == 24 or now.day == 26)) and not goodRole:
        tmp = await client.send_message(message.channel, 'Merry Christmas!! :snowflake:   :confetti_ball: ')
    if "shutdown" in message.content and goodRole and str(message.author) != "Ottum#9851" :
        tmp = await client.send_message(message.channel, 'Shutting down')
        client.logout
        os._exit(0)



def addToTracking(name):
    with open('.\logs\markedLog.json', 'r') as log:
        trackListJson = log.read()
    trackList = trackListJson
    if trackList != "":
        trackList =json.loads(trackList)
    else:
        trackList = {}

    if name in trackList:
        trackList[name] = trackList[name]+1
    else:
        trackList[name] = 1



    trackerlog = name +" is marked for "+ str(trackList[name])+ " times"
    if trackList[name]>2:
        trackerlog = trackerlog + ", maybe you should consider an action"

    trackListJson = json.dumps(trackList)
    with open('.\logs\markedLog.json', 'w') as log:
            log.write(trackListJson)
    print("trackList notice")
    print(trackerlog)


def file_len(fname):
    with open(fname) as f:
        i = 0
        for i, l in enumerate(f):
            pass
    return i + 1

client.run('MzU3MDkzMDE1OTc1NjI0NzA0.DMgGkA.YBfnsk-0L_f0IqdAy9kwaSbqbKQ')
