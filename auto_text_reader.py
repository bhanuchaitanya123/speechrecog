
import googletrans
import googletrans
from tkinter import *
from googletrans import Translator
from gtts import gTTS
import os
import turtle as t
print(googletrans.LANGUAGES)
print("press a to give the file '\n'or press b to listen the voice and translate")
def a():
 translator=Translator()
 file="C:\\Users\\munab\\OneDrive\\python\\helo.txt"
 with open(file,'rb') as f:
  p=f.read()
  translation = translator.translate(p, dest='te')
  print(translation.text)
  to_lang='te'
  myob=gTTS(text=translation.text,tld='co.in',lang=to_lang,slow=False)
  myob.save("audpy.mp3")
  os.system('start audpy.mp3')
t.onkey(a, 'a')
t.listen()

def b():
 import speech_recognition as sr
 r=sr.Recognizer()
 with sr.Microphone() as s:
    print("speak")
    audio=r.listen(s)
    textl=r.recognize_google(audio)
    print(textl)
    import os
    translator = Translator()
    translation = translator.translate(textl, dest='te')
    print(translation.text)
    to_lang='te'
    myob=gTTS(text=translation.text,tld='co.in',lang=to_lang,slow=False)
    myob.save("audpy.mp3")
    os.system("start audpy.mp3")
t.onkey(b, 'b')
t.listen()



