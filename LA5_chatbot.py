import re
import random

# Define the chatbot's responses
responses = {
    r"hi|hello|hey": ["Hello!", "Hi there!", "Hey!"],
    r"how are you?": ["I'm doing well, thanks for asking!", "Doing good, how about you?"],
    r"what is your name\??": ["My name is Chatbot, nice to meet you!"],
    r"thank you": ["You're welcome!", "No problem!"],
    r"goodbye|bye": ["Goodbye!", "Take care!", "See you later!"],
    r"default": ["I'm afraid I don't understand. Could you please rephrase your question?"]
}

def respond(user_input):
    """
    Respond to the user's input based on the defined responses.
    """
    for pattern, responses_list in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses_list)
    return responses["default"][0]

def main():
    print("Welcome to the Customer Interaction Chatbot!")
    print("You can start chatting with me. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
