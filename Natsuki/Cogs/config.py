import discord
from discord.ext import commands

class conf(commands.Cog):
    def __init__(self, bot):
         self.b = bot

    token = "token"
    prefix = "n_"
    name = "Natsuki"
    version = "1.0a"
    sharding = False
    cogd = "Cogs"
    type_speed = 2
    playing_msg = ["Type 'n_help' for help!","Doki Doki Literature Club","Don't Starve","Cooking Mama"]


    ''' Just wanted to clear out that these hex codes bellow are for embed colours so i don't have to keep changing them in every single fucking file '''
    err = 0xff42e2 # The Error Embed Colour
    norm = 0xff42e2 # The Normal or Yeah sure i did this command heres an embed color Embed Colour
    warn = 0xff42e2 # The Warning Embed Colour
    suc = 0xff42e2 # The Success i did a thing Embed Colour

    ''' These are just some error quotes so i can change them really quickly instead of doing the same quote for each error in every file '''
    everyone_tag = "Nice try to ping everyone, Baka."
    econfused = "Uh... What?"


    ''' Doki Bot's ID'S '''
    natsuki_id = 531555963908653076
    monika_id = 531556928732528670 
    sayori_id = 531554745337249792
    yuri_id = 531556397746356224



def setup(bot):
    bot.add_cog(conf(bot))
