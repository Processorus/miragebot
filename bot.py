import discord
import random
import asyncio
from itertools import cycle
from discord.ext import commands
from pyfiglet import figlet_format, FontError, FontNotFound
from pyfiglet import figlet_format, FontError, FontNotFound

client=discord.client
bot = commands.Bot(command_prefix = '.')
status = ["Helping people", ".help for help", "with your heart", "with you", "survival games", "Gta V", "Games", "HoI4, EU4, CK2, Stellaris, Vic2, Civ6"]
bot.remove_command("help")

async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(10)

@bot.command(aliases=['h', 'helps', 'hp'], pass_context=True)
async def help(ctx):
         embed = discord.Embed(title="Hey! My prefix is '.'", color=0x5f0bdd)
         embed.add_field(name='Fun Commands',value="Reaction: 🎮", inline=True)
         embed.add_field(name='Moderation Commands',value="Reaction: 🔍", inline=True)
         embed.add_field(name='Game Links Commands',value="Reaction: 💾", inline=True)
         embed.add_field(name='Help Server',value="https://discord.gg/76kvfeT", inline=True)
         message = await bot.say(embed=embed)
         reaction = await bot.add_reaction(message,'🎮'), await bot.add_reaction(message,'🔍'), await bot.add_reaction(message,'💾')
         reaction = await bot.wait_for_reaction(message=message, user = ctx.message.author)
         if str(reaction.reaction.emoji) == "🔍":
            em = discord.Embed(colour=discord.Colour.magenta())
            em.add_field(name='Moderation Commands',value=".gulag \n.clear \n.ban", inline=True)
            await bot.say(embed=em)
            reaction = await bot.wait_for_reaction(message=message, user = ctx.message.author)
         elif str(reaction.reaction.emoji) == "🎮":
                em = discord.Embed(colour=discord.Colour.magenta())
                em.add_field(name='Fun Commands',value=".communist \n.omgstoppls \n.filth \n.repost \n.facepalm \n.emu \n.hedgehogs \n.cat \n.lewd \n.nolewd \n.triggered \n.what \n.welcome",inline=True)
                message = await bot.say(embed=em)
                reaction = await bot.wait_for_reaction(message=message, user = ctx.message.author)
         elif str(reaction.reaction.emoji) == "💾":
                emb =  discord.Embed(colour=discord.Colour.magenta())
                emb.add_field(name='Game Links Commands',value=".giveck2 \n.givehoi4 \n.givestellaris \n.giveeu4 \n.givevic2 \n.giveciv6 \n.givecoh2", inline=True)
                message = await bot.say(embed=emb)
                reaction = await bot.wait_for_reaction(message=message, user = ctx.message.author)

@bot.event
async def on_ready():
    print('client is ready!')


@bot.command(pass_context = True)
async def clear(ctx, number):
    mgs = []
    number = int(number)
    if ctx.message.author.server_permissions.administrator:
        async for x in bot.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
            await bot.delete_messages(mgs)

@bot.command (pass_context=True)
async def avatar(ctx, user: discord.Member):
    await bot.say(user.avatar_url)


@bot.command (pass_context=True)
async def communist(ctx):
    communist = ["https://cdn.discordapp.com/attachments/512543644557770752/518377646007123968/6167DsxZ1dL._SY679_.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377648137830411/104630.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377654907305984/icon00000000018.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377657323487232/indeks.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377661463003136/A1IN8hVcxYL.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377660741582858/jpg.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377667259793419/Lenin.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377669482643487/lenina.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377675069325322/leninaa.jpeg", "https://cdn.discordapp.com/attachments/512543644557770752/518377688415731715/tumblr_m2vwf0nmn51qcx7vyo1_400.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377701443108874/vladimir-lenin-9379007-1-402.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377723182448640/vladimir-lenin-portrait.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377727171100682/3d6c28f9f9afc5271c2fa0f2f7ebb8e9_w750_h563.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377735459176448/05-vladimir-lenin-20080101_gaf_u66_63433_b.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377740617908255/220px-Bundesarchiv_Bild_183-71043-0003_Wladimir_Iljitsch_Lenin.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377746234212352/220px-Lenin-1895-mugshot.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377800084750347/http__a.amz.mshcdn.com_wp-content_uploads_2016_03_stalin-14.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377806070284310/joseph-stalin-2.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377810134302720/joseph-stalin-9491723-1-402.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377816128094208/stalin.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377814433464336/LeninEnSuizaMarzo1916--barbaroussovietr00mcbr.png", "https://cdn.discordapp.com/attachments/512543644557770752/518377823120130059/stalin_1878541c.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377836755681280/Stalin_Joseph-570842793df78c7d9eca7584.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377836243845150/Stalin_in_July_1941.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377847207886859/STALIN2.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377847392567296/Stalin_Meme.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377853042032670/tyfeu1xhm6wte7ruvftm.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377859576758293/81eRo6Xo4ZL.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377864345944065/200px-Stalin_in_exile_1915.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377878744858634/220px-Stalin_Full_Image.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377885489299456/0502putinstalin01.jpg", "https://cdn.discordapp.com/attachments/512543644557770752/518377892259037184/be2f01bd30ec4ae38c00095dc37de27b.jpg"]
    communist = random.choice(communist)
    embed = discord.Embed(title="<:SU:439524372089274368>", color=0xc60808)
    embed.set_image(url=communist)
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command (pass_context=True)
async def dab(ctx):
    dab = ["https://cdn.discordapp.com/attachments/521685227048009728/521685265656446986/ap550x55012x121transparentt.u2.png", "https://cdn.discordapp.com/attachments/521685227048009728/521685282639314965/a3b6774cd215e9293387a116568538a5.jpeg", "https://cdn.discordapp.com/attachments/521685227048009728/521685301308162122/images.jpeg", "https://cdn.discordapp.com/attachments/521685227048009728/521685321080111114/s-l300.jpg", "https://cdn.discordapp.com/attachments/521685227048009728/521685364994342913/DAB.png", "https://cdn.discordapp.com/attachments/521685227048009728/521685377623261211/530-90_58655f3e96e2e.jpg", "https://cdn.discordapp.com/attachments/521685227048009728/521685397017985034/Dab-Mod.jpg", "https://cdn.discordapp.com/attachments/521685227048009728/521685670511771661/1_Q1y22__F34ulWs372a2B0Q.jpeg", "https://cdn.discordapp.com/attachments/521685227048009728/521685715919306752/FB_IMG_1543757879675.jpg"]
    dab = random.choice(dab)
    embed = discord.Embed(title="dab", color=0xff0000)
    embed.set_image(url=dab)
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)



@bot.command(pass_context=True)
async def hedgehogs(ctx):
    hedgehogs = ["https://i.pinimg.com/originals/ef/a8/f2/efa8f2dcfb868214f2bf1358fe154187.png", "https://i.pinimg.com/originals/53/a0/38/53a038a08b2b6687aa22553651d6a8b2.jpg", "https://i.pinimg.com/originals/ef/a8/f2/efa8f2dcfb868214f2bf1358fe154187.png", "https://i.pinimg.com/originals/bd/22/7b/bd227b3db2194d5019b7264120014f8b.jpg", "https://i.pinimg.com/originals/80/dd/c5/80ddc587f0dadb6fde3cdda3c891d577.jpg", "https://i.pinimg.com/564x/48/44/a6/4844a6c2cc18da33571ef8c09337fb0f.jpg", "https://i.pinimg.com/originals/17/6c/ed/176ced87b63f0aa412c1bfcc6920a7af.jpg", "https://i.pinimg.com/564x/ad/98/63/ad9863b18b8c2c9381881a4397faa008.jpg", "https://i.pinimg.com/564x/de/dd/0f/dedd0f2c2a17d43bca1c7bb2b018e835.jpg", "https://i.pinimg.com/originals/3f/d6/3f/3fd63f0d84ba22279838c694ab79b1ce.jpg", "https://i.pinimg.com/564x/ad/98/63/ad9863b18b8c2c9381881a4397faa008.jpg", "https://i.pinimg.com/564x/fa/32/2c/fa322cffb6ef187ff105eb5b2681e55a.jpg", "https://i.pinimg.com/originals/1d/65/03/1d650368a85e82fdb15bd42ab415f9da.jpg", "https://i.pinimg.com/originals/9e/e4/9d/9ee49dae54cba763155fff0840ca6ffd.jpg", "https://i.pinimg.com/originals/70/e5/ba/70e5bab3e47af70b9f0cf7bf3c75326f.jpg", "https://i.pinimg.com/236x/25/c1/20/25c120bed8e6f401c6e6005fcb29a2e1.jpg", "https://i.pinimg.com/originals/43/f6/a5/43f6a55f2f4ba5b20ff3b21bd095c497.jpg", "https://i.pinimg.com/originals/27/53/22/2753227371e30b6bc60c6536ca47c149.jpg", "https://i.pinimg.com/564x/90/16/8a/90168a19cecb160e2a80b81b46fd9a6d.jpg", "https://i.pinimg.com/564x/54/ce/40/54ce4031b1ccd6bf2a2251caf52fcb89.jpg", "https://i.pinimg.com/564x/3f/b3/1d/3fb31dcd9d12df97fe2c04b843c6a2da.jpg", "https://i.pinimg.com/564x/43/b6/98/43b698f7897374049adcc8b0c68451db.jpg", "https://i.pinimg.com/564x/22/1b/4b/221b4b3abbd3ed799d34049137107557.jpg", "https://i.pinimg.com/564x/29/7b/7e/297b7e21f66f4e2dbcc589f911154e90.jpg", "https://i.pinimg.com/564x/2f/a9/6e/2fa96eb608d636899e700387f12250e0.jpg", "https://i.pinimg.com/564x/70/e5/ba/70e5bab3e47af70b9f0cf7bf3c75326f.jpg", "https://i.pinimg.com/564x/27/53/22/2753227371e30b6bc60c6536ca47c149.jpg"]
    hedgehogs = random.choice(hedgehogs)
    embed = discord.Embed(title="Cute hedgehogs! ", color=0xc109a6)
    embed.set_image(url=hedgehogs)
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def emu(ctx):
    emu = ["https://cdn.pixabay.com/photo/2018/06/16/20/57/emu-australia-3479506_960_720.jpg", "https://cdn.pixabay.com/photo/2018/06/16/20/59/emu-3479510_960_720.jpg", "https://cdn.pixabay.com/photo/2018/09/10/21/02/bouquet-3668046_960_720.jpg", "https://cdn.pixabay.com/photo/2016/04/15/22/44/emu-1332143_960_720.jpg", "https://cdn.pixabay.com/photo/2017/08/17/19/55/emus-2652641_960_720.jpg", "https://cdn.pixabay.com/photo/2018/10/03/10/32/emu-3720998_960_720.jpg", "https://cdn.pixabay.com/photo/2014/01/31/08/58/animal-255324_960_720.jpg", "https://cdn.pixabay.com/photo/2013/07/16/16/33/emus-163028_960_720.jpg", "https://cdn.pixabay.com/photo/2018/07/27/19/12/emu-3566667_960_720.jpg", "https://cdn.pixabay.com/photo/2014/04/05/11/39/emu-316483_960_720.jpg", "https://cdn.pixabay.com/photo/2017/09/27/06/26/emu-2791107_960_720.jpg", "https://cdn.pixabay.com/photo/2017/08/15/20/57/emu-2645526_960_720.jpg", "https://cdn.pixabay.com/photo/2018/05/16/20/37/emu-3406982_960_720.jpg", "https://cdn.pixabay.com/photo/2015/06/12/22/32/strauss-807585_960_720.jpg"]
    emu = random.choice(emu)
    embed = discord.Embed(title="Cute emu! ", color=0xc109a6)
    embed.set_image(url=emu)
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def repost(ctx):
    embed = discord.Embed(title="BAN <:banhammer:447426814424645632>", color=0xc109a6)
    embed.set_image(url="https://media.giphy.com/media/5h7nCjw5TENTusXDQX/giphy.gif")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def facepalm(ctx):
    embed = discord.Embed(title="🤦", color=0xc109a6)
    embed.set_image(url="https://media.giphy.com/media/wsUw19t8HpzRrEzoCY/giphy.gif")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def filth(ctx):
    embed = discord.Embed(title="Filth", color=0xc109a6)
    embed.set_image(url="https://media.giphy.com/media/5eFSGjMPuIKOVNBYqY/giphy.gif")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def lewd(ctx):
    embed = discord.Embed(title="<:lewd:452945991038140456>", color=0xc109a6)
    embed.set_image(url="https://media.giphy.com/media/2fLhy2f7I4sAPg7IZk/giphy.gif")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def nolewd(ctx):
    embed = discord.Embed(title="<:lewd:452945991038140456> ⛔", color=0xc109a6)
    embed.set_image(url="https://i.imgur.com/ZQezptY.jpg")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def triggered(ctx):
    embed = discord.Embed(title="REEEEEEEEEEEEEEEEEEEE", color=0xc109a6)
    embed.set_image(url="https://media.giphy.com/media/65D9gpyfs7QH3B46kM/giphy.gif")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def what(ctx):
    embed = discord.Embed(title="what lol", color=0xc109a6)
    embed.set_image(url="https://media.giphy.com/media/U8l9EW4yDG2X9C593d/giphy.gif")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)




@bot.command(pass_context=True)
async def welcome(ctx):
    embed = discord.Embed(title="RICEEEEE", color=0xc109a6)
    embed.set_image(url="https://media.giphy.com/media/1lAIzaL1UTSYiBKFNB/giphy.gif")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def omgstoppls(ctx):
    embed = discord.Embed(title="STOP IT BOI", color=0xc109a6)
    embed.set_image(url="https://media.giphy.com/media/3FoxtmYmTZhKQqd2GC/giphy.gif")
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cat(ctx):
    cat = ["https://i.pinimg.com/564x/0d/11/6c/0d116c8e58fa9a039115ee55fa57027d.jpg", "https://i.pinimg.com/564x/eb/92/d9/eb92d9ce8485a137a9946443c054913d.jpg", "https://i.pinimg.com/564x/36/47/f6/3647f6339f0d7acc9b4348cb27b9ed1b.jpg", "https://i.pinimg.com/564x/89/4b/81/894b813dffb6484734091af5910487c6.jpg", "https://i.pinimg.com/564x/36/01/31/3601311295c515abf1232ff70a77477e.jpg", "https://i.pinimg.com/564x/ec/76/ed/ec76ed0f05260a370a087d8bba2efbd1.jpg", "https://i.pinimg.com/564x/46/0c/5c/460c5c7dc40d4ef1191eb974ef4f8afb.jpg", "https://i.pinimg.com/564x/bf/c5/49/bfc54910fa33ea6914822dbc607be853.jpg", "https://i.pinimg.com/564x/ce/ba/e8/cebae8b23eb2b1c3c808f8727d842db1.jpg", "https://i.pinimg.com/564x/69/7a/e3/697ae31579bb6a4d326964c1b19008bc.jpg", "https://i.pinimg.com/564x/43/f2/c6/43f2c6dadc9708a3ea8f63f9ee253506.jpg", "https://i.pinimg.com/564x/7c/7e/c3/7c7ec3c8ec43faa8c944a1da9a8a416c.jpg", "https://i.pinimg.com/564x/b2/3e/1a/b23e1a203d704e77025acaf157612c16.jpg", "https://i.pinimg.com/564x/dd/90/60/dd90608f2941f2d6d7dcb36a509719ff.jpg", "https://i.pinimg.com/564x/22/a1/7b/22a17bceee3c5c30a53360946c18073c.jpg", "https://i.pinimg.com/564x/43/94/02/4394028c97f4e7d9fb66e02062834e51.jpg", "https://i.pinimg.com/564x/88/63/9f/88639f36e583b6d3db9ecc07a5dd18c8.jpg", "https://i.pinimg.com/564x/9a/f1/b6/9af1b6b966ef5e4ba0edacdb61658380.jpg", "https://i.pinimg.com/564x/75/29/b0/7529b0868666c34fb3103bb4bc894185.jpg", "https://i.pinimg.com/564x/f6/46/34/f64634c6bc11e6c17f9db0e66fba0d0d.jpg"]
    cat = random.choice(cat)
    embed = discord.Embed(title="Cute cats! ", color=0xc109a6)
    embed.set_image(url=cat)
    embed.set_footer(text='asked it', icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)


@bot.command (pass_context=True)
async def ascii(ctx, *, msg):
		'Convert text to ascii art'
		if ctx.invoked_subcommand is None:
			if msg:
				msg = str(figlet_format(msg.strip(), font='big'))
				if len(msg) > 2000:
					await bot.say('**Message too long, RIP.**')
				else:
					try:
						await bot.say('```fix\n{}\n```'.format(msg))
					except:
						pass
		else:
			await bot.say('**Please input text to convert to ascii art. Ex: ``-ascii stuff``**')


@bot.command (pass_context=True)
async def gulag(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(user.server.roles, name="Gulag of shame")
        await bot.say("He sent to gulag! <:gulag:442095745596915713>")
        await bot.add_roles(user, role)
    else:
       embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
       await bot.say(embed=embed)


@bot.command(pass_context=True)
async def giveck2(ctx, user: discord.User):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed = discord.Embed(title="**CK2 - Holy fury**",description="[CK2 Full game](link here)\n [CK2 3.0.1 Patch](link here) \n[Steamfix+CreamAPI](link here) \n[DLC only](link here) \n[Instructions](link here)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="link here")
        embed.set_thumbnail(url="link here")
        embed.set_image(url="link here")
        embed.set_footer(text="© Mirage 2018",icon_url="link here")
        await bot.send_message(user, "```You don't want to pay money for Paradox Interactive games but you want to play multiplayer with other people? Here's your place :smiley: Download game, install it, apply crack and start playing! Have fun and share your best moments with us! Over 4500+ members in our community, you can easily find people who want to play a game with you! Every evening we are playing big sessions, feel free to join them!```")
        await bot.send_message(user, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command. :cry:", color=0xff00f6)
        await bot.say(embed=embed)



@bot.command(pass_context=True)
async def givehoi4(ctx, user: discord.User):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed = discord.Embed(title="**HOI4- Waking The Tiger**",description="[HOI4 1.5.0](link here)\n[HOI4 1.5.1 patch](link here)\n[HOI4 1.5.2 patch](link here)\n[HOI4 1.5.3 patch](link here)\n[HOI4 1.5.4 patch](link here) \n[Steamfix+CreamAPI](link here) \n[DLC only part 1](link here) \n[DLC only part 2](link here) \n[Instructions](link here)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="https://cdn.discordapp.com/attachments/428326060531253248/452250323726368769/8w7qtwnf.png")
        embed.set_thumbnail(url="link here")
        embed.set_image(url="link here")
        embed.set_footer(text="© Mirage 2018",icon_url="link here")
        await bot.send_message(user, "```You don't want to pay money for Paradox Interactive games but you want to play multiplayer with other people? Here's your place :smiley: Download game, install it, apply crack and start playing! Have fun and share your best moments with us! Over 4500+ members in our community, you can easily find people who want to play a game with you! Every evening we are playing big sessions, feel free to join them!```")
        await bot.send_message(user, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command. :cry:", color=0xff00f6)
        await bot.say(embed=embed)



@bot.command(pass_context=True)
async def givestellaris(ctx, user: discord.User):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed = discord.Embed(title="*Stellaris- MegaCorp**",description="[**Stellaris 2.2 Direct Download**](link here) \n[**Stellaris 2.2 Torrent**](link here) \n[**Stellaris Steamfix**](link here) \n[**Stellaris CreamAPI**](link here) \nStellaris 2.1 to 2.2 patch (**PENDING**) \n[**Stellaris MegaCorp DLC only**](link here)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="link here")
        embed.set_thumbnail(url="link here")
        embed.set_image(url="link here")
        embed.set_footer(text="© Mirage 2018",icon_url="link here")
        await bot.send_message(user, "```You don't want to pay money for Paradox Interactive games but you want to play multiplayer with other people? Here's your place :smiley: Download game, install it, apply crack and start playing! Have fun and share your best moments with us! Over 4500+ members in our community, you can easily find people who want to play a game with you! Every evening we are playing big sessions, feel free to join them!```")
        await bot.send_message(user, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command. :cry:", color=0xff00f6)
        await bot.say(embed=embed)


@bot.command(pass_context=True)
async def giveeu4(ctx, user: discord.User):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed = discord.Embed(title="EU4- Golden Century",description="[EU4 1.28 Full game](link here) \n[1.28.2 Hotfix](link here) \n[Only 1.28 DLCs](link here) \n[Steamfix](link here) \n[CreamAPI](link here) \n[DLC only](link here) \n[Instructions](link here)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="link here")
        embed.set_thumbnail(url="link here")
        embed.set_image(url="link here")
        embed.set_footer(text="© Mirage 2018",icon_url="link here")
        await bot.send_message(user, "```You don't want to pay money for Paradox Interactive games but you want to play multiplayer with other people? Here's your place :smiley: Download game, install it, apply crack and start playing! Have fun and share your best moments with us! Over 4500+ members in our community, you can easily find people who want to play a game with you! Every evening we are playing big sessions, feel free to join them!```")
        await bot.send_message(user, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command. :cry:", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def giveciv6(ctx, user: discord.User):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed = discord.Embed(title="*Civilization VI**",description="[CIV6 Full game](link here) \n[Steamfix](link here) \n[Instructions](link here)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="link here")
        embed.set_thumbnail(url="link here")
        embed.set_image(url="link here")
        embed.set_footer(text="© Mirage 2018",icon_url="link here")
        await bot.send_message(user, "```You don't want to pay money for games but you want to play multiplayer with other people? Here your place :) Download game, install it, apply crack and start playing! Have fun and share your best moments with us! Over 4500+ members on community, you can easily find people who wants play game with you! Every evening we are playing big sessions, feel free to join them!```")
        await bot.send_message(user, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command. :cry:", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def givevic2(ctx, user: discord.User):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed = discord.Embed(title="*Victoria 2- Hearts of Darkness**",description="[Vic2 Full game](link here)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="link here")
        embed.set_thumbnail(url="link here")
        embed.set_image(url="link here")
        embed.set_footer(text="© Mirage 2018",icon_url="link here")
        await bot.send_message(user, "```You don't want to pay money for Paradox Interactive games but you want to play multiplayer with other people? Here's your place :smiley: Download game, install it, apply crack and start playing! Have fun and share your best moments with us! Over 4500+ members in our community, you can easily find people who want to play a game with you! Every evening we are playing big sessions, feel free to join them!```")
        await bot.send_message(user, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command. :cry:", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def givecoh2(ctx, user: discord.User):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed = discord.Embed(title="*Company of Heroes 2 DLC unlocker**",description="[CreamAPI](link here)",color=0xe6aadf)
        embed.set_author(name="Mirage Helper", url="",icon_url="link here")
        embed.set_thumbnail(url="link here")
        embed.set_image(url="link here")
        embed.set_footer(text="© Mirage 2018",icon_url="link here")
        await bot.send_message(user, "```You don't want to pay money for Paradox Interactive games but you want to play multiplayer with other people? Here's your place :smiley: Download game, install it, apply crack and start playing! Have fun and share your best moments with us! Over 4500+ members in our community, you can easily find people who want to play a game with you! Every evening we are playing big sessions, feel free to join them!```")
        await bot.send_message(user, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command. :cry:", color=0xff00f6)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hoi4(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Hoi4")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def eu4(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="EU4")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def ck2(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="CK2")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def stellaris(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Stellaris")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def civ6(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Civ 6")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def coh2(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="COH2")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)



@bot.command(pass_context=True)
async def vic2(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Vic2")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def tos(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="ToS")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def eu4daily(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Who wants to play EU4")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def hoi4daily(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Who wants to play HOI4")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def ck2daily(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Who wants to play CK2")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def vic2daily(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Who wants to play VIC")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def stellarisdaily(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Who wants to play Stellaris")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def civ6daily(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Who wants to play CIV 6")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def offtopic(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Offtopic")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def anime(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Anime")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)



@bot.command(pass_context=True)
async def political(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Political")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def artwork(ctx):
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="Artwork")
    await bot.add_roles(user, role)
    msg = await bot.say("Role added successfully!")
    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def givehoi4steamfix(ctx, user: discord.User):
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed=discord.Embed(title="HoI4 Steamfix", url="https://mega.nz/#!pgB2xKZC!UCYeNPY5mkC0nEzTU0YPRj0gns9lPf-i9F8gP3upd9Y", description="Extract and put into game folder! (Press to 'HoI4 Steamfix' to see link!)", color=0xb317a3)
        await bot.send_message(user, embed=embed)



@bot.command(pass_context=True)
async def eu4season(ctx):
        await bot.say("Check direct messages <a:okedokey:518350515726319635>")
        embed=discord.Embed(title="Europa Universalis IV.", description="Interested in playing mp Europa Universalis 4 with others , make sure to check out eu4 league weekend campaign , we play every weekend without fail", color=0xff00f6)
        await bot.send_message(ctx.message.author, embed=embed)
@bot.event
async def on_message(message):
    print(f"{message.channel}:  {message.author}: {message.author.name}: {message.content}")
    await bot.process_commands(message)


@bot.command(pass_context=True)
async def hack(ctx, member: discord.Member):
    a = await bot.say(f'Searching {member.name}s location..')
    await asyncio.sleep(2)
    locat = ["Lithuania", "Romania", "Croatia", "Serbia", "Canada", "USA", "Mexico", "Egypt", "United Kingdom", "Turkey", "Brasil", "İndia", "Azerbaijan", "France", "Germany", "China", "Russia"]
    location = random.choice(locat)
    await bot.edit_message(a, new_content=f'Location: {location}')
    await asyncio.sleep(2)
    await bot.edit_message(a, new_content=f'`` gmail: {member.name}****@gmail.com \npassword: ********``')
    await asyncio.sleep(2)
    await bot.edit_message(a, new_content=f'Searching IP..')
    await asyncio.sleep(2)
    ip = ["192.**5.*2.11", "1*7.**3.56.55", "123.67*.**.11", "127.***.78.98", "179.*56.**.12"]
    ipler = random.choice(ip)
    await bot.edit_message(a, new_content=f'IP: {ipler}')
    await asyncio.sleep(2)
    await bot.edit_message(a, new_content=f'Hacking Discord account..')
    await asyncio.sleep(2)
    lo = ["None.", "Hacked ✓."]
    loi = random.choice(lo)
    await bot.edit_message(a, new_content=f'{loi}')
    await asyncio.sleep(2)
    await bot.edit_message(a, new_content=f'Searching other accounts..')
    await asyncio.sleep(2)
    await bot.edit_message(a, new_content=f'All accounts were hacked.')
    await asyncio.sleep(2)
    await bot.edit_message(a, new_content=f'{member.name} has been hacked!')


@bot.command()
async def logout(ctx):
    if ctx.message.author.server_permissions.administrator:
        await bot.logout()

bot.loop.create_task(change_status())
bot.run(TOKEN)
