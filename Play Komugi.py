#я еблан и разраб этой хуйни: телеграм @y9RavenCat
from hikkatl.types import Message
from .. import loader 
from hikka import utils

url = "https://x0.at/0T5N.mp4"

@loader.tds
class PlayKomugiMod(loader.Module):
    """Play with Komugi
    Developer: @y9RavenCat"""
    strings = {"name": "Play Komugi", "caption": "ВЫ ПОИГРАЛИ С КОМУГИ"}
    
    @loader.command(
        ru_doc="Поиграй с Комуги"
        # ...
    )
    async def plkomug(self, message: Message):
        """- Вы поиграете с комуги ;)"""
        await utils.answer_file(message, file=url, caption=self.strings("caption"))