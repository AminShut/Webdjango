from openai import OpenAI

import os




# client = OpenAI(
#   api_key = ''
# )

#creating func----------------------------------------

def chat_bot(message):

    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = message,
    )

    return response.choices[0].message.content