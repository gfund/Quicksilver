import os #used to access .env file 
#DISCORD IMPORTS
###########################
import discord

import discord.ext
from discord.ext import commands
###############################


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='~',intents=intents)
#--------------------EVENTS--------------------------




async def buffersender(ctx,arr,delim):
  buffer=""
  i=1
  for item in arr:
    if delim not in ["nl","nb"]:
      if arr.index(item) != len(arr):
       buffer=buffer+str(item)+delim
      else:
        buffer=buffer+str(item)

    elif delim == "nb":
     
      if arr.index(item) != len(arr):
        buffer=buffer+str(i)+". "+str(item)+"\n"
      else:
        buffer=buffer+str(item)
        
    i+=1
   

  await ctx.send(buffer)

async def targetparse(ctx,user):
  user=user.strip()

  #text 
  if((user.replace(" ","").isalpha())):
   
 
 
   for member in ctx.guild.members:
     
     
     if((user==(member.display_name)) or(user==(member.nick)) or (user==(member.name))):
      
       return member
    
      
    
  elif( "@" in user):
        
      
        memid=int(user.replace("<@!"," ").replace(">"," "))
        member = await bot.fetch_user(memid)
        return member
  elif(user.isdigit()):
     member = await bot.fetch_user(user)
     return member


global suituser
suituser=763003385384271893
global weapons
weapons=False
global weplist
weplist=[("repulsor","https://cdn.discordapp.com/attachments/816650862365376562/816692899126444083/Iron_Man_Mark_5_Suit_Up_Scene_-_Iron_Man_2_2010_Open_Matte_M.gif","fire"),("melee","https://cdn.discordapp.com/attachments/830988894308139039/862774112718946323/Iron_Man_2__Iron_Man_vs_Vanko__Suitcase_suit_Scene__2010_.gif","melee")]
global wepnum
wepnum=0
async def usersend(messagetext,mode):
    global suituser
    #uituser=0
    
    user=await bot.fetch_user(suituser)
   # print(user.name)
    if(mode=="text"):
     
     await user.send(messagetext)
    if(mode=="file"):
        await user.send(file=discord.File(messagetext))
@bot.event
async def on_ready():
  #Statements that execute when  the bot boots.
  print("Booted") # do nothing but enough not to cause an error
  await usersend("Booted Systems","text")

@bot.event
async def on_message(message):
 await bot.process_commands(message)
@bot.event
async def on_member_join(member):
  #Statements that execute when someone joins a server the bot is in
  print(str(member))


#--------------------COMMANDS--------------------------  
@bot.command()
async def fireat(ctx,*,user):
       
 
      
      
      
     
          import asyncio
          global weapons
          global weplist
          global wepnum

          if weapons:

            target=await targetparse(ctx,user)
            msg = await ctx.send("Systems activating: ")
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: :arrow_forward:')
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: :arrow_forward: :arrow_forward:')
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: :arrow_forward: :arrow_forward: :arrow_forward:')
            await asyncio.sleep(0.1)
            if weplist[wepnum][2]=="fire":
             await ctx.send("_Firing {0} at  {1} _".format(weplist[wepnum][0],str(target)))
            else:
              await ctx.send("Attacking {0} with {1}".format(str(target),weplist[wepnum][0]))
            await ctx.send(weplist[wepnum][1])
          else:
           await ctx.send("Safety is On")
@bot.command()
async def ban(ctx,member:discord.Member):
    global weapons
    if weapons:
     await ctx.guild.ban(member,reason="ban",delete_message_days=0)
     await ctx.send("banned " + member.mention)
    else: 
      await ctx.send("Safety On")

@bot.command()
async def wepswitch(ctx,*,text):
 # await ctx.send(text)
  channel=ctx.channel
  uid=ctx.author.id
  def check(m):
            return m.channel == channel and m.author.id== uid
  
  
  global weplist
  global wepnum

  wepnames=[]
  
  for i in weplist:
   wepnames.append(i[0])
   if text==i[0]:
    wepnum=weplist.index(i) 
    await ctx.send(weplist[weplist.index(i)][0]+" selected")
    return
  
  if text=="list":
   await buffersender(ctx,wepnames,"nb")
 
   await ctx.send("Which weapon # do you want")
   wepn=await bot.wait_for("message",check=check)
   wepnum=int(wepn.content)-1
  
  await ctx.send(weplist[wepnum][0]+" selected")

@bot.command()
async def weptoggle(ctx):
  global weapons
  weapons= not weapons
  if not weapons:
    await ctx.send("Safety On")
  else:
    await ctx.send("Safety Off")
  
  
 
@bot.event 
async def on_guild_join(guild):
    
 if guild.system_channel: 
        await guild.system_channel.send("https://tenor.com/view/iron-man-tony-stark-robert-downey-jr-wear-suit-iron-man2suit-gif-11924598")      



#----------------------RUN BOT CODE-------------------------


       

#get the token from .env 
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
