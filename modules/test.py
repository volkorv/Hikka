from hikkatl.types import Message
from .. import loader

@loader.tds
class HelloWorld(loader.Module):
    """Hello World module"""
    strings = {"name": "HelloWorld", "hello": "Hello, {}!"}
    strings_ru = {"hello": "Привет, {}!"}
    strings_es = {"hello": "¡Hola, {}!"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "greeting",
                "Hello",
                "Greeting message",
                validator=loader.validators.String(),
            ),
        )

    @loader.command(
        ru_doc="Привет мир!",
        es_doc="¡Hola mundo!",
    )
    async def helloworld(self, message: Message):
        """Hello World"""
        name = self.get("name", "World")
        await utils.answer(message, self.strings("hello").format(name))

    @loader.command(
        ru_doc="Установить имя",
        es_doc="Establecer nombre",
    )
    async def setname(self, message: Message):
        """Set name"""
        args = utils.get_args(message)
        if not args:
            await utils.answer(message, "Please provide a name")
            return
        name = args[0]
        self.set("name", name)
        await utils.answer(message, f"Name set to {name}")
