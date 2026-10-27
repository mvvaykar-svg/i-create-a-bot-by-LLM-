from groq import Groq

# put your groq api key here
client=Groq(api_key="gsk_your_key_here")

print("My LLM Agent Started")
print("Type bye to exit")

file=open("chat.txt","a")

while True:
    msg=input("You:")
    file.write("You:"+msg+"\n")

    if msg=="bye":
        print("Bot: Bye")
        file.write("Bot: Bye\n")
        break

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":msg}]
    )

    ans=response.choices[0].message.content
    print("Bot:"+ans)
    file.write("Bot:"+ans+"\n")

file.close()
