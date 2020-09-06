import pyttsx3 
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")
    except Exception as e:
        speak("Pardon Please")
        print("Pardon Please")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aishuajali18@gmail.com', 'aishu@anjali')
    server.sendmail('aishuajali18@gmail.com', to, content)
    server.close()



    

if __name__ == "__main__":
    speak("hello snigdha! how are you? hope everything is good")

    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query :
            speak('Searching Wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackover flow")
            webbrowser.open("stackoverflow.com")

        elif 'how are you' in query:
            speak('I am good . What about you?') 
        elif 'who are you' in query or 'Hello' in query or 'Hi' in query:
            speak("Hello!I am your assistant.How can I help you")
            
        elif 'play music' in query:
            music_dir = 'F:\\songs'
            songs = os.listdir(music_dir)
            speak("Playing music")
            print("Playing music")    
            print(songs[0])
            os.startfile(os.path.join(music_dir, songs[0]))
            break
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "snigdha.anjali18@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Mail not sent") 


        elif "where is" in query:
            query = query.split(" ")
            location_url = "https://www.google.com/maps/place/" + str(query[2])
            speak("Hold on, I will show you where " + query[2] + " is.")
            maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
            os.system(maps_arg)

        elif 'open code' in query: 
            codePath="C:\\Users\\SNIGDHA ANJALI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")
            print(strTime)
          

        elif "exit" in query or "bye" in query or "sleep" in query: 
            speak("Ok bye bye, See you later") 
            break


            