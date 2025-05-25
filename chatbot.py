import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Predefined responses
responses = {
    "greeting": "Hello! How can I assist you today?",
    "weather": "I can check the weather for you. What city are you interested in?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that. Can you try asking something else?"
}

# Function to process user input
def process_input(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Simple intent detection based on keywords
    if any(word in lemmatized for word in ["hi", "hello", "hey"]):
        return responses["greeting"]
    elif "weather" in lemmatized:
        return responses["weather"]
    elif any(word in lemmatized for word in ["bye", "goodbye", "exit"]):
        return responses["bye"]
    else:
        return responses["default"]

# Main chat loop
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot:", responses["bye"])
            break
        response = process_input(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()