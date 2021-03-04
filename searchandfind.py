import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
#Text To Speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)
def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning i am virtual assistent jarvis")
    elif hour>=12 and hour<18:
        speak("good afternoon i am virtual assistent jarvis") 
    else:
        speak("good evening i am virtual assistent jarvis")  

#now convert audio to text
# 
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-US')
        print(text)
    except Exception:                #For Error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return text

#for main function                               
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "search" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")         
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"the time is {strTime}")
            
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okay..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        elif 'who made you' in query or ' who created you' in query or 'who developed you' in query:
            ans_m = " For your information Acrowbatics100 or Arkrainian developed me."
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you !"
            print(about)
            speak(about)
        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello!"
            print(hel)
            speak(hel)
        elif "your name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)
        elif "your feelings" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 
        elif query == 'none':
            continue 
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()    
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i cant understand but i can search from the internet to give your answer !'
            print(res_g)
            speak(res_g)
            res_g2 = input('should i proceed? type yes or no: ')

            if res_g2 == "yes":
                    webbrowser.open(g_url+temp)
            elif res_g2 == "no":
                    continue
            else:
                    print("Sorry, couldn't understand")
                    speak("Sorry, couldn't understand")
                    speak("Continuing to search it up")
                    print("Continuing to search it up")
                    webbrowser.open(g_url+temp)
                    
