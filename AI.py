import cv2
import os
import speech_recognition as sr

from gtts import gTTS
from playsound import playsound
z=1




 
while True:
#def main():
    mytext = 'Hello How can I help you?'
  
    language = 'EN'
  

    myobj = gTTS(text=mytext, slow=False)

    myobj.save("AI.mp3")
    playsound('AI.mp3')
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
 
 
        # recognize speech using google
 
        try:
          #a=r.recognize_google(audio)
           a=r.recognize_google(audio)
           print("Audio Recorded Successfully \n ")
           res="Search for\n" + r.recognize_google(audio)
           print("Search for\n" + r.recognize_google(audio))
           mytext = res
  
           language = 'EN'
  

           myobj = gTTS(text=mytext, slow=False)

           myobj.save("AI.mp3")
           playsound('AI.mp3')
 
           r = sr.Recognizer()
 
        
        except Exception as e:
            #print("Error :  " + str(e))
            print("Sorry,I didn't understand")
            z=0
     
        
        
        if z==1:
 
          print("The Result")
          try:
             from googlesearch import search
          except ImportError:
             print("No module named 'google' found")
 
          query = a
 
          for j in search(query, tld="co.in", num=3, stop=3, pause=2):
                print(j)
          mytext = 'Here is the result'
  
          language = 'EN'
  

          myobj = gTTS(text=mytext, slow=False)

          myobj.save("AI.mp3")
          playsound('AI.mp3')
          
        z=1
        input("Press Enter to continue...")