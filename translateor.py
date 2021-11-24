from os import system
from googletrans import Translator
from pyperclip import paste

text: str = paste()
translator = Translator()
translate = translator.translate(text, "fa")
try:
    if len(text) > 50:
        system(f"notify-send --expire-time=100000 'translate' '{translate.text}'")
    else:
        system(
            f"notify-send --expire-time=10000 'translate' '{text} : {translate.text}'"
        )
except Exception as error:
    system(
        f"notify-send --expire-time=10000 'translate' 'translate failed try again with this error {error}'"
    )
