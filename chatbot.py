import random
from datetime import datetime

class ConversationHistory:
    def __init__(self, size=5):
        self.history = []
        self.max_size = size

    def add(self, message):
        self.history.append(message)
        if len(self.history) > self.max_size:
            self.history.pop(0)

    def get_last_message(self):
        if self.history:
            return self.history[-1]
        else:
            return None

def greet(time_of_day):
    if time_of_day < 12:
        return "Good morning!"
    elif 12 <= time_of_day < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def chatbot():
    conversation_history = ConversationHistory()

    while True:
        user_input = input("You: ").strip().lower()
        conversation_history.add(user_input)

        now = datetime.now()
        current_hour = now.hour

        if user_input in ("hi", "hello", "hey"):
            response = f"{greet(current_hour)} How can I help you today?"

        elif user_input == "help":
            response = "I'm here to assist you! Feel free to ask me anything."

        elif user_input == "tell me a joke":
            jokes = [
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "What do you call a fish with no eyes? Fsh!",
                "Why don't scientists trust atoms? Because they make up everything!"
            ]
            response = random.choice(jokes)

        elif user_input == "what is the time" or user_input == "what date is it":
            now = datetime.now()
            response = f"The current date and time is {now.strftime('%A, %B %d %I:%M %p')}"

        elif user_input == "what is your name":
            response = "I'm your friendly chatbot! You can call me ChatGPT."

        elif user_input == "who created you":
            response = "I was created by a team of developers at OpenAI."

        elif "how are you" in user_input:
            response = random.choice(["I'm doing well, thanks for asking!", "I'm here and ready to assist you!"])

        elif "thank" in user_input:
            response = random.choice(["You're welcome!", "Glad I could help!"])

        elif "bye" in user_input:
            response = random.choice(["Goodbye! Have a great day!", "See you later!", "Take care!"])

        else:
            # Respond with a prompt to encourage further interaction
            response = "I'm not sure I understand. Let's talk about something else. What else would you like to know?"

        print(f"Chatbot: {response}")
        conversation_history.add(response)

# Run the chatbot
chatbot()
