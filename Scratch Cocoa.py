#я еблан и разраб этой хуйни: телеграм @y9RavenCat
from hikkatl.types import Message
from .. import loader 
from hikka import utils

url = "https://x0.at/urag.mp4"

@loader.tds
class ScratchCocoaMod(loader.Module):
    """Scratch Cocoa
    Developer: @RavenModules"""
    strings = {"name": "Scratch Cocoa", "caption": "ВЫ ПОЧЕСАЛИ КОКОА"}
    
    @loader.command(
        ru_doc="- Вы почешите Кокоа ;)"
        # ...
    )
    async def scrcocoa(self, message: Message):
        """- Вы почешите Кокоа ;)"""
        await utils.answer_file(message, file=url, caption=self.strings("caption"))