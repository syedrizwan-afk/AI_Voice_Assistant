## About the Project
B2 is a Python-based AI voice assistant that performs a variety of smart tasks using speech recognition, text-to-speech synthesis, and OpenAI’s GPT API.
It can open websites, play songs, fetch the latest news, and even chat with you — all through your voice.

## Features

+ Speech Recognition: Understands your voice commands in real time.

+  AI Conversations: Uses OpenAI GPT for natural, human-like responses.

+  Smart Actions: Opens Google, YouTube, and Facebook on voice request.

+  Music Player: Plays your favorite songs from YouTube.

+ News Reader: Fetches and reads the latest headlines using the GNews API.

+ Dual Voice Modes: Uses pyttsx3 (offline) and gTTS + pygame (online) for speech output.



## Example Commands
Command	Description
“B2 open Google”	Opens Google in your browser
“B2 open YouTube”	Opens YouTube
“B2 play blindfold”	Plays the song “Blindfold” from YouTube
“B2 news”	Reads the latest news headlines
“B2 what is artificial intelligence”	Responds using OpenAI GPT

## Dependencies
Library	            Purpose

speechrecognition	Capture and interpret voice input
pyttsx3	Offline     text-to-speech
gTTS + pygame	    Online text-to-speech
requests	        Fetch data from APIs
openai	            ChatGPT API integration
webbrowser	        Opens websites
os	                Handles file operationss