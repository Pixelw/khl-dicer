import random

from khl import Bot, Message

import dicer
import secret

bot = Bot(token=secret.khl_token)


def run():
    bot.run()


@bot.command()
async def ra(msg: Message, skill: str, p_max: int):
    result = dicer.ra(msg.author.username, skill, p_max)
    await msg.reply(result)


async def r(msg: Message, count: int, dice: int):
    result = dicer.r(msg.author.username, count, dice)
    await msg.ctx.channel.send(result)
