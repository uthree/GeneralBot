from discord.ext import commands
import discord as discord
import random

# Fun(ネタコマンド系) cog

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["sintyoku"])
    async def sinchoku(self,ctx):
            links = [
                "https://cdn.discordapp.com/attachments/708828790796845189/787409537883439134/alicedoudesuka-300x168.jpg",
                "https://cdn.discordapp.com/attachments/787413181277798400/787413202958417920/images-6.jpeg",
                "https://cdn.discordapp.com/attachments/787413181277798400/787413219085647872/images-5.jpeg",
                "https://cdn.discordapp.com/attachments/787413181277798400/787413268872429568/images.jpeg",
                "https://cdn.discordapp.com/attachments/787413181277798400/787413301776089118/main.pngcompresstrue.png",
                "https://cdn.discordapp.com/attachments/787413181277798400/787413247686737930/images-3.jpeg"
                ]
            await ctx.send(random.choice(links))

    @commands.command(aliases=["sintyoku_dame"])
    async def sinchoku_dame(self,ctx):
            links = [
                "https://ghippos.net/image/blog/20131008_1.jpg",
                "https://livedoor.blogimg.jp/tank_make/imgs/a/9/a996bd7c.jpg",
                "https://d2dcan0armyq93.cloudfront.net/photo/odai/400/8a1b02cea77695724af97b596cbc5acc_400.jpg"
                ]
            await ctx.send(random.choice(links))

    @commands.command()
    async def krsw(self,ctx):
        images = [
                "https://cdn.discordapp.com/attachments/859753134729199666/875924516616957982/KRSW.png", # 無能弁護士
                "https://cdn.discordapp.com/attachments/859753134729199666/875927011154088016/HSGW.png", # 長谷川亮太
                "https://cdn.discordapp.com/attachments/859753134729199666/875926898838999050/JEX.jpg"   # ペルソナメガネ
                ]
        await ctx.send(random.choice(images))

    @commands.command()
    async def pakason(self,ctx):
        pakasong_txt  = open('./cogs/pakason.txt', 'r')

        pakasong_list = pakasong_txt.readlines()

        pakasong      = [
                        pakasong_list[0],
                        pakasong_list[1],
                        pakasong_list[2],
                        pakasong_list[3]
                        ]
        await ctx.send(random.choice(pakasong))
        pakasong_txt.close()

def setup(bot):
    bot.add_cog(Fun(bot))
