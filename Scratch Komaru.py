#я еблан и разраб этой хуйни: телеграм @y9RavenCat
from hikkatl.types import Message
from .. import loader 
from hikka import utils

url = "https://x0.at/OLui.mp4"

@loader.tds
class ScrKomMod(loader.Module):
    """Scratch Komaru
    Developer: @RavenModules"""
    strings = {"name": "Scratch Komaru", "caption": "ВЫ ПОЧЕСАЛИ КОМАРУ"}
    
    @loader.command(
        ru_doc="Почеши Комару"
        # ...
    )
    async def scrkom(self, message: Message):
        """- Вы почешите Комару ;)"""
        await utils.answer_file(message, file=url, caption=self.strings("caption"))