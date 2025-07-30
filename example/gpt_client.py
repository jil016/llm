import os
from openai import OpenAI

models = ["gpt-4o", "gpt-o1", "gpt-4.5-preview"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    model=models[2],
    messages=[
        {
            "role": "user",
            "content": "Who are you?",
        }
    ],
)

print(chat_completion.choices[0].message.content)