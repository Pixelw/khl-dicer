from khl import Bot, Message

import dicer
import secret
from logger import set_logger

bot = Bot(token=secret.khl_token)

set_logger('khl', log_path='bot_logs/')
d_log = set_logger('dialog', log_path='dialog_logs/', log_pattern='%(asctime)s\t%(message)s', timed_rotate='W0')


def run():
    bot.run()


@bot.command(prefixes=['.', '。', '/'])
async def ra(msg: Message, skill: str, p_max: int):
    result = dicer.ra(msg.author.username, skill, p_max)
    if len(result) > 0:
        await msg.reply(result)
        d_log.info(f'[{msg.author.username}] [{skill}] {result}')


@bot.command(regex=r'\.r(\d{1,2})d(\d{1,2})$')
async def r(msg: Message, _: Bot, count: int, dice: int):
    result = dicer.r(msg.author.username, count, dice)
    if len(result) > 0:
        await msg.reply(result)
        d_log.info(f'[{msg.author.username}] {result}')


@bot.command(regex=r'\.rh(\d{1,2})d(\d{1,2})$')
async def rh(msg: Message, _: Bot, count: int, dice: int):
    result = dicer.r(msg.author.username, count, dice)
    if len(result) > 0:
        await msg.author.send(result)
        await msg.reply("命运正在低语！")
        d_log.info(f'[{msg.author.username}] rh {result}')
