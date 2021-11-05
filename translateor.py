from subprocess import getoutput
from googletrans import Translator
from os import system

text = getoutput("xclip -out -selection primary")
translator = Translator()
translate = translator.translate(text, "fa")
try:
    if len(text) > 50:
        system(f"notify-send --expire-time=100000 'translate' '{translate.text}'")
    else:
        system(f"notify-send --expire-time=10000 'translate' '{text} : {translate.text}'")
except Exception as error:
    system("notify-send --expire-time=10000 'translate' 'translate failed try again'")
