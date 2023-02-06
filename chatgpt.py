# imports
import openai  # for OpenAI API calls
import time  # for measuring time savings
from dotenv import load_dotenv # for load env
import os

# load apenai api key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")