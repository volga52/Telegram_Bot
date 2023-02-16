from aiogram import types
# from aiogram.dispatcher import Dispatcher
from hashlib import md5
from handlers.handler import Handler


class HandlerInlineMode(Handler):
    # def __init__(self, dispatcher: Dispatcher):
    #     super().__init__(dispatcher)

    def inline_mode(self):
        dp = self.dp

        @dp.inline_handler()
        async def inline_handler(query: types.InlineQuery):
            text = query.query or 'echo'
            link = 'https://www.wikipedia.org/wiki/'+text
            result_id: str = md5(text.encode()).hexdigest()

            article = [types.InlineQueryResultArticle(
                id=result_id,
                title='Статья Wikipedia',
                url=link,
                input_message_content=types.InputTextMessageContent(
                    message_text=link
                )
            )]
            await query.answer(article, cache_time=1, is_personal=True)

    def handler(self):
        self.inline_mode()
