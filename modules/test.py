from hikka import Hikka, Message
from hikka.utils import edit_or_reply
from hikka.patterns import patterns

@Hikka.on_message(patterns("hello"))
async def hello(_, message: Message):
    await edit_or_reply(message, "Hello! How are you today?")
