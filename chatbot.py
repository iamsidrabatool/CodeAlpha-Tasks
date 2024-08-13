"""A basic text-based chatbot that can have conversations with users, using natural language processing libraries like NLTK to make the chatbot more conversational
This script implements a simple chatbot using the NLTK library. The chatbot responds to user inputs based on predefined patterns and responses.
It supports basic conversational elements such as greetings, asking for the chatbot's name, and simple questions about the chatbot's creator
and location. Type 'quit' to exit the chat.
"""
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('wordnet')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you! How can I assist you today?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries!",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Good to hear that!", "How can I help you today?",]
    ],
    [
        r"where are you located?",
        ["I'm based in the digital world.",]
    ],
    [
        r"how (.*) work",
        ["I use natural language processing techniques to understand and respond to your queries.",]
    ],
    [
        r"(.*) (created|made) (.*)",
        ["I was created by the developers at OpenAI.",]
    ],
    [
        r"Ask about weather",
        ["I'm not sure about the weather, but you can check online for the latest updates.",]
    ],
    [
        r"quit",
        ["Bye for now. Have a great day!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you please rephrase?",]
    ],
]
def chatbot():
    print("Hi! I am a chatbot created by OpenAI. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot
if __name__ == "__main__":
    chatbot()
