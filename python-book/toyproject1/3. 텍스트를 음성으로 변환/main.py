# pip install gtts
from gtts import gTTS
# pip install playsound
from playsound import playsound
import os

# read_file = "hello world"

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = 'readme.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')

tts.save("readme.mp3")

# error check
playsound("readme.mp3")
