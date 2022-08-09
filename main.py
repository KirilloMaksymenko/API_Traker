import config
import fortnite_stats
import steam_stats
import crypto
import leboncoin

import discord 
from discord.ext import commands
#from discord.commands import Option


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot load succes")


#username:commands.Option(discord.Member,"Enter the person")
@bot.slash_command(guild_ids = [config.guild_id], description = "fortnite stats")
async def fort(ctx,username:str):
    await ctx.respond(f"This>>{fortnite_stats.sort_data_fortnite(username)}")

@bot.slash_command(guild_ids = [config.guild_id], description = "CsGo stats")
async def csgo(ctx,user_id:str):
    await ctx.respond(f"This>>{steam_stats.request_contr_strike_api(user_id)}")

@bot.slash_command(guild_ids = [config.guild_id], description = "Crypto stats")
async def crypt(ctx,name:str):
    data = crypto.request_crypto_api(name)
    name = data["name"]
    price = data["price"]
    await ctx.respond(f"Name - {name} \nPrice - {price}")

@bot.slash_command(guild_ids = [config.guild_id], description = "Leboncoin stats")
async def lebon(ctx,name:str,limit:int):
    ads, shippable_ads = leboncoin.request_leboncoin(name,limit)
    for ad in ads():
        await ctx.respond(f"Name - {ad.subject} Price - {ad.price}")
        print(ad.subject, ad.price)
    print("\n")

    for ad in shippable_ads():
        await ctx.respond(f"Name - {ad.subject} \nPrice - {ad.body}")
        print(ad.subject)
        print(ad.body)
        print("\n")
    
    

bot.run(config.discord_token)