import pytz
import datetime
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
#voices is a list of voices on your computer
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 150)
def time_in_india():
         indian_time = pytz.timezone("Asia/Calcutta")
         dt_India = datetime.datetime.now(indian_time)
         if hour>=0 and hour<12:
                  print(dt_India, "am")
                  engine.say(dt_India)
                  engine.say("am")
                  engine.runAndWait()
         elif hour>=12 and hour<18:
                  print(dt_India, "pm")
                  engine.say(dt_India)
                  engine.say("pm")
                  engine.runAndWait()
def time_in_uk():
         uk_time = pytz.timezone("GMT")
         dt_uk = datetime.datetime.now(uk_time)
         hour = int(datetime.datetime.now().hour)
         if hour>=0 and hour<12:
                  print(dt_uk, "am")
                  engine.say(dt_uk)
                  engine.say("am")
                  engine.runAndWait()
         elif hour>=12 and hour<18:
                  print(dt_uk, "pm")
                  engine.say(dt_uk)
                  engine.say("pm")
                  engine.runAndWait()

