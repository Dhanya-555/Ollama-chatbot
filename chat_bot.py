import ollama

print("Welcome to AI Chatbot!")

while True:
    msg = input("You: ")

    if msg.lower() == "exit":
        print("Bot: Goodbye!")
        break

    result = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": msg}
        ]
    )

    print("Bot:", result.message.content)