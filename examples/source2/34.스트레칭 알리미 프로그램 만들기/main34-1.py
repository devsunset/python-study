from gtts import gTTS
from playsound import playsound
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "스트레칭 시간입니다. 자리에서 일어나 스트레칭 하세요"
tts = gTTS(text=text, lang='ko')
tts.save("tts.mp3")

playsound("tts.mp3")