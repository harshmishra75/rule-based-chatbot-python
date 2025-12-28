print("Bot: Hey! I'm a simple chatbot. Type 'bye' anytime to exit.")

while True:
    user_message = input("You: ").lower()

    if "bye" in user_message:
        print("Bot: Alright, take care. See you soon!")
        break
    elif "hello" in user_message:
        print("Bot: Hey there! Nice to meet you.")
    elif "motivate" in user_message:
        print("Bot: Keep going. Progress comes from consistency, not perfection.")
    elif "python" in user_message:
        print("Bot: Python is a clean and beginner-friendly language, widely used in AI, data science, and web development.")
    else:
        print("Bot: I'm not sure how to respond to that yet, but I'm learning.")
