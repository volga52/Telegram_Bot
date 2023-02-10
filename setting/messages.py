HELP_PREVIEW = 'Я могу ответить на следующие команды:'
HELP_COMMAND_LIST = ['/voice', '/photo', '/group', '/note', '/file', '/test',
                     '/testpre', '/info', '/play', '/hikb1', '/hikb2',
                     '/hikb3', '/hikb4', '/hikb5', '/hikb6', '/hikb7',
                     '/rmkbs', '/firstbtn', '/secondbtn', '/Описание',
                     '/animal']

TESTPRE = """@dp.message_handler(commands=['testpre'])
    async def process_testpre_command(message: types.Message):
        message_text = pre(emojize('Ха! Не в этот раз \N{Smirking Face}'))
        await bot.send_message(message.from_user.id, message_text)"""
UNKNOWN = 'Я не знаю, что с этим делать :astonished:'
DESCRIPTION = 'Этот бот - Мой персональный, учебный бот.\nНе слишком пафосно? Нет?'

CAT_BIG_EYES = 'AgACAgIAAxkDAAMvY9ljutWlHQpQSY0G1zKUyUfMExIAAg_HMRtdPMlKoV2pgOTsuh0BAAMCAAN4AAMtBA'
KITTENS = [
    'AgACAgIAAxkDAAMzY9lju8hedMaDRyvmwkzKNSyLwFAAAhDHMRtdPMlKIBv1pfTPdqUBAAMCAAN3AAMtBA',
    'AgACAgIAAxkDAAM0Y9ljuzaR4190U8flhsVouHYbGRsAAhHHMRtdPMlK-OnsufPfooQBAAMCAAN4AAMtBA',
    'AgACAgIAAxkDAAM1Y9ljvMrDL_Zq-Kxmg-qdOlM7qMQAAhLHMRtdPMlKgii2JWFXPwoBAAMCAANtAAMtBA',]
VOICE = 'AwACAgIAAxkDAAMwY9ljulPmgkLh7HQQGJBmC49bQZQAAr8kAAJdPMlK4lDf-4C6UUktBA'
VIDEO = 'BAACAgIAAxkDAAMyY9ljulT3ymV89O7cTy14luH9lbYAAsEkAAJdPMlKZdpKQ5ddTzwtBA'
TEXT_FILE = 'BQACAgIAAxkDAAMuY9ljt5VDyPvAcvSDyQABuWRSdH13AAK-JAACXTzJStnUdlxn4dR1LQQ'
VIDEO_NOTE = 'DQACAgIAAxkDAAMxY9ljupaVFHGTCFx4hXIf0Jid6IYAAsAkAAJdPMlKK2I6jZr-jYgtBA'
