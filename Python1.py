def chatbot_response(user_input):
    user_input = user_input.lower()  # Normalize user input to lowercase for easier matching

    # Predefined rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    elif "your name" in user_input:
        return "I am a simple chatbot created to assist you."
    elif "what can you do" in user_input:
        return "I can respond to your queries based on predefined rules. Try asking me something!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop to interact with the user
def main():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()
