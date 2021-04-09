import pyttsx3 
#pyttsx3 is a text-to-speech conversion library in Python . also works in offline
import speech_recognition as sr
#recognizes the speech from user and also converts speech into String
import datetime
# wishing Good Morning, Good Afternoon
import wikipedia
# for reading summary from wikipedia
import webbrowser
# to search web 
import os
#grabbing any files

engine = pyttsx3.init('sapi5')          # can use the inbuild voice 
voices = engine.getProperty('voices')

print(voices[0].id)                     # in this we only have one voice thats why it will show index out of range for voices[1].id
engine.setProperty('voices',voices[0].id)   #setting the voice 

'''
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 115)     #setting the pace
'''
def speak(audio): # it will speak whatever the argument is given (pronounce)
    engine.say(audio)
    engine.runAndWait()

def Wishme():     # greeting the user
    hour = int(datetime.datetime.now().hour)   # will return hour from 0 - 24 hrs
    if hour>=0 and hour<12:
        speak("Good morning! ")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening! ")                  
    #after wishing it wil speak about itself
    speak("I am Ziri, Please tell me How may i help you ")


def takeCommand():              
    # WORKING -- > It will take input from microphone and returns the string output   will return None if not recognized

    r = sr.Recognizer()    # it is an class which will recognize the voice
    with sr.Microphone() as source:  # with statement is used to open the file.
        print("Listening...  ")
        r.pause_threshold = 0.8        # ctrl + left click 
        audio = r.listen(source)     # Records a single phrase from ``source`` and also checks for engery is higher and pasue_threshold

    try:
        print("Recognizing... ")
        query = r.recognize_google(audio , language='en-in')   # whatever listened will in audio will passed as parameter in this
        print(f"User Said {query} \n")
        speak(query)
        
    
    except Exception as e:
        # print(e) # if want to say what was the exception then print
        print("Say That Again Plzz.....")
        return "None"

    return query
    

if __name__== "__main__":     
    # speak(" well done boy!!!!!!" )
    Wishme()
    # while True:   #it will keep asking for commands

    if 1:
        query = takeCommand().lower()         #converting all the comands taken from user into lower String format to avoid any error with case sensitivity
        #Logic for executing different tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")  #replacing query with blank for new query to be searched
            results = wikipedia.summary(query, sentences=3)  # will return the summary fro wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        # websites
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening Youtube...") 

        elif 'open google' in query:
            webbrowser.open('https://google.com/?#q=')
            speak("opening Google...")
        
        elif 'open stack overflow' in query:
             webbrowser.open('https://stackoverflow.com/')
        
        # applications
        elif 'play vlc' in query:
            videos_dir = 'K:\\Death Note'        #location 
            player = os.listdir(videos_dir)   
            print(player)
            speak("opening Death Note....")
            os.startfile(os.path.join(videos_dir,player[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        
