import os
import json
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

FILE_NAME = "memory.json"

# Load old conversation if it exists
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        messages = json.load(file)
else:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI tutor. Explain answers simply and briefly."
        }
    ]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    messages.append(
        {"role": "user", "content": user_input}
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )

    ai_reply = response.choices[0].message.content

    messages.append(
        {"role": "assistant", "content": ai_reply}
    )

    # Save conversation
    with open(FILE_NAME, "w") as file:
        json.dump(messages, file)

    print("AI:", ai_reply)