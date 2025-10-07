import json
import random
import re

class SimpleChatbot:
    def __init__(self, intents_path):
        """
        Initializes the chatbot by loading the intents file.
        """
        self.intents = self._load_intents(intents_path)

    def _load_intents(self, filepath):
        """
        Loads the intents from a JSON file.
        """
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: The file {filepath} is not a valid JSON.")
            return None

    def get_response(self, user_message):
        """
        Finds a matching intent for the user's message and returns a response.
        """
        if not self.intents:
            return "I'm sorry, I am not configured correctly."

        # Preprocess the user's message
        user_message = user_message.lower().strip()

        # Find the best matching intent
        best_match_score = 0
        best_intent = None

        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                # Using simple regex for whole word matching
                if re.search(r'\b' + re.escape(pattern.lower()) + r'\b', user_message):
                    # For this simple bot, the first direct match is good enough.
                    # A more complex bot might score based on match quality.
                    score = 1 # Simple match score
                    if score > best_match_score:
                        best_match_score = score
                        best_intent = intent
                        break # Move to next intent once a pattern matches
            if best_intent and best_intent == intent:
                break # Exit outer loop if a good match is found

        if best_intent:
            return random.choice(best_intent['responses'])
        else:
            return "I'm not sure how to respond to that. Can you ask me something else?"

def main():
    """
    Main function to run the chatbot in the console.
    """
    # Create an instance of the chatbot
    chatbot = SimpleChatbot('intents.json')

    print("Chatbot is ready! Type 'quit' to exit.")
    print("You: ", end="")

    # Interaction loop
    while True:
        user_input = input()
        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")
        print("You: ", end="")

if __name__ == "__main__":
    main()
