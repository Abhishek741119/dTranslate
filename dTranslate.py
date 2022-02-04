import discord
import os
from keep_alive import keep_alive
import translate


def interprete(msg, to_lang):
    obj = translate.Translator(to_lang)
    text = obj.translate(msg)
    return text


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as ')


@client.event
async def on_message(message):
    _msg = message.content
    user = os.environ['_user']
    if message.author == user:
        return
    if _msg.startswith("?"):
        data = _msg[1:]
        _content = data.split()
        lang = _content[-1]
        _content = " ".join(_content[:-1])
        text = interprete(_content, lang)

        embed = discord.Embed(title="Translator", color=0xFF5733)
        embed.set_author(name=message.author.display_name,
                         icon_url=message.author.avatar_url)
        embed.add_field(name="English", value=_content, inline=False)
        embed.add_field(name=lang, value=text, inline=False)
        embed.set_footer(text="translated by dTranslate")
        await message.channel.send(embed=embed)


keep_alive()
client.run(os.environ['Token'])
