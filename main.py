import random
import discord
import secreto
from discord.ext import commands

client = commands.Bot(command_prefix='?')
TOKEN = secreto.seu_token()


@client.command(name='reaction_create_post')
async def reaction_create_post(context):
    myEmbed = discord.Embed(title='')



@client.command(name='versao')
async def versao(context):
    await context.message.channel.send('Versão v0.1-Alpha')


@client.command(name='redes')
async def redes(context):
    myEmbed = discord.Embed(title='Redes Sociais IL Viana do Castelo',color=0x00AEEF)
    myEmbed.add_field(name='Facebook: ', value='[VianaLiberal](https://www.facebook.com/VianaLiberal)')
    myEmbed.add_field(name='Twitter: ', value='[@LiberalViana](https://twitter.com/LiberalViana)')
    myEmbed.add_field(name='Instagram: ', value='[@VianaLiberal](https://www.instagram.com/vianaliberal/)')
    myEmbed.set_author(name='IL Viana do Castelo')
    myEmbed.set_thumbnail(url='https://i.imgur.com/m3FX7FF.png')
    #await context.message.channel.send('Facebook: https://www.facebook.com/VianaLiberal')
    #await context.message.channel.send('Twitter: https://twitter.com/LiberalViana')
    #await context.message.channel.send('Instagram: https://www.instagram.com/vianaliberal/')
    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('------------')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name='por um #PortugalMaisLiberal'))


@client.event
async def on_message(message):
    if message.content.lower().startswith('?testeEmojis'):
        moeda = random.randint(1, 2)
        if moeda == 1:
            await message.add_reaction('😀')
        else:
            await message.add_reaction('👑')

    await client.process_commands(message)

client.run(TOKEN)
