from groq import Groq 
from datetime import datetime

client = Groq(api_key="your key")
messages = []

while True:
    chat = input("you:")
    if chat == "bye":
        print("bye!")
        break

    if "time" in chat.lower():
        now = datetime.now().strftime("%H:%M")
        reply = f"Abhi {now} baj rahe hai"
        print("Bot:", reply)
        messages.append({"role": "user", "content": chat})
        messages.append({"role": "assistant", "content": reply})
        continue

    messages.append({"role": "user", "content": chat})
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    reply = response.choices[0].message.content
    print("Bot:", reply)
    messages.append({"role": "assistant", "content": reply})