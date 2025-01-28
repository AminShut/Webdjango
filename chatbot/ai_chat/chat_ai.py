from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
  api_key = os.getenv("OPENAI_API_KEY")
)

#creating func----------------------------------------

def chat_bot(message):

    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = message,
    )

    return response.choices[0].message.content