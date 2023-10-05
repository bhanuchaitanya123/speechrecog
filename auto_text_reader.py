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
def c():
  import speech_recognition as sr
  import pyttsx3 as p
  import wikipedia as w
  import pywhatkit 
  #pywhatkit.sendwhatmsg("+91", "Hello", 22, 28)
  #pywhatkit.playonyt("GeeksforGeeks")
  #pywhatkit.search("GeeksforGeeks")
  #pywhatkit.sendwhats_image("+91, "Images/Hello.png")
  engine=p.init()
  voices=engine.getProperty('voices')
  engine.setProperty('voice',voices[1].id)
  r=sr.Recognizer()
  with sr.Microphone() as s:
          aud=r.listen(s)
          text=r.recognize_google(aud)
          text=text.lower()
          if 'alexa' in text:
              text=text.replace('alexa','')
  print(text)
  if 'play' in text:
      song=text.replace('play','')
      engine.say(song)
      engine.runAndWait()
      pywhatkit.playonyt(song)
  elif 'search' or 'open' in text:
   if 'search' in text:
      text=text.replace('search','') 
      pywhatkit.search(text)
   if 'open' in text:
       text=text.replace('open','')
       pywhatkit.search(text)
  elif 'who' in text:
      person=text.replace('who','')
      info=w.summary(person,1)
      engine.say(info)
      engine.runAndWait()
      
t.onkey(c, 'c')
t.listen()
