import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
from gtts import gTTS
from openai import OpenAI
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
gnewsapi = "<yout key here>"

def speak_1(text):
    engine.say(text)
    engine.runAndWait()

def speak_2(text):
    tts = gTTS(text) 
    tts.save('temp.mp3')

    # initialize pygame mixer
    pygame.mixer.init()
    # load mp3 file
    pygame.mixer.music.load('temp.mp3')
    # play mp3 file
    pygame.mixer.music.play()

    # keep prog run until music stops
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
def aiProcess(command):
    client = OpenAI(api_key="<your key here>",
    )
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        message = [
             {"role": "system", "content": "You are a virtual assistant named B2 skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=in&max=10&apikey={gnewsapi}")
        if r.status_code == 200:
            # parse the json
            data = r.json()
            # extract the article
            articles = data.get('articles', [])
            # print the headlines
            for article in articles:
                speak_2(article['title'])
    
        # let open ai handle req
    else:
        output = aiProcess(c)
        speak_2(output)

        


if __name__ == "__main__":
    speak_2("Initializing B2....")
    # print (sr.Microphone.list_microphone_names())
    while True:
        # Listen 4 wake word "B2"
        # obtain audio from the mcrophone
        r = sr.Recognizer()
      
    # recognize speech using Sphinx
        print("recognising...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "B2"):
                speak_2("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("B2 Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
      