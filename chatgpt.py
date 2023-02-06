# imports
import openai  # for OpenAI API calls
import time  # for measuring time savings
from dotenv import load_dotenv # for load env
import os
from gtts import gTTS # for text to speech
import pygame # for play file mp3

# config
FOLDER_AUDIO = './texttospeech'

# load apenai api key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def text_to_speech(_text, path_folder = FOLDER_AUDIO, lang = 'vi'):
    tts = gTTS(text=_text, lang= lang)
    file_audio = f'{hash(_text)}.mp3'
    path_file_audio = os.path.join(path_folder, file_audio)
    if not os.path.exists(path_file_audio):
        tts.save(path_file_audio)
    
    pygame.mixer.init()
    pygame.mixer.music.load(path_file_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(200)