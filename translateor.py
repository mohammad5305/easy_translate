from subprocess import getoutput
from googletrans import Translator
from os import system

text = getoutput("xclip -out -selection primary")
translator = Translator()
translate = translator.translate(text, "fa")
try:
    if len(text) > 50:
        system(f"notify-send 'translate' '{translate.text}'")
    else:
        system(f"notify-send 'translate' '{text} : {translate.text}'")
except Exception as error:
    system(f"notify-send 'translate' 'translate failed try again'")
