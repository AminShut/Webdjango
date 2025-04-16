from openai import OpenAI

import os




client = OpenAI(
  api_key = "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"
)

#creating func----------------------------------------

def chat_bot(message):

    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = message,
    )

    return response.choices[0].message.content