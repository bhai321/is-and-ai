import random
# Define possible chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hi!"],
    "how are you": ["I'm doing well, thank you!", "Great, thanks for asking!", "I'm fine, how are you?"],
    "what's your name": ["My name is Chatbot!", "I'm Chatbot, nice to meet you!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm sorry, I didn't understand that.", "Could you please repeat that?"]
}

# Define function to generate chatbot response
def generate_response(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Define main function to handle user input and chatbot response
def main():
    print("Hello! I'm a chatbot. What's your name?")
    name = input()
    print(f"Nice to meet you, {name}! How can I assist you today?")

    while True:
        message = input()
        if message.lower() == "bye":
            print(generate_response("bye"))
            break
        print(generate_response(message))

if __name__ == '__main__':
    main()
