import os
from openai import OpenAI

models = ["deepseek-reasoner", "deepseek-chat"]

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model=models[0],
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Who are you?"},
    ],
    stream=False
)

print(response.choices[0].message.content)