# Simple Python Chatbot

A simple rule-based chatbot built with Python. This project demonstrates how to use a JSON file to define conversational intents and a Python script to process user input and generate responses.

---

## Project Files

- **`intents.json`**  
  The "brain" of the chatbot. This file contains a structured list of _intents_, which are categories of user messages. Each intent includes:

  - **`tag`**: A unique name for the intent (e.g., `"greeting"`, `"goodbye"`).
  - **`patterns`**: Example phrases a user might type that correspond to this intent.
  - **`responses`**: Possible replies the chatbot can give for this intent.

- **`chatbot.py`**  
  The main Python script containing the chatbot logic. It loads the intents, processes user input, and selects an appropriate response.

---

## Code Overview

### `chatbot.py` Structure

- **Imports**

  ```python
  import json
  import random
  import re
  ```

  - `json`: Loads and parses the `intents.json` file.
  - `random`: Randomly selects a response from the list of possible responses for a given intent.
  - `re`: Uses regular expressions for robust word matching in user messages.

- **`SimpleChatbot` Class**

  - Encapsulates all chatbot functionality.

  - **`__init__(self, intents_path)`**  
    Loads the intents from the specified JSON file.

  - **`_load_intents(self, filepath)`**  
    Opens and loads the JSON file. Handles:

    - `FileNotFoundError`: If `intents.json` is missing.
    - `json.JSONDecodeError`: If the JSON file has a syntax error.

  - **`get_response(self, user_message)`**  
    Processes user input:
    - Converts the message to lowercase and trims whitespace.
    - Iterates through each intent and its patterns.
    - Uses `re.search()` to check if a pattern exists as a whole word in the user's message (prevents partial matches, e.g., `"hi"` in `"this"`).
    - If a match is found, selects a random response from the intent's responses.
    - If no match is found, returns a default "I don't understand" message.

- **`main()` Function**

  - Entry point for running the chatbot from the command line.
  - Creates a `SimpleChatbot` instance.
  - Prints a welcome message.
  - Enters a loop to continuously listen for user input.
  - If the user types `"quit"`, the loop breaks and the program ends.
  - Otherwise, calls `chatbot.get_response()` and prints the bot's reply.

- **`if __name__ == "__main__":`**
  - Ensures the `main()` function runs only when the script is executed directly (not when imported as a module).

---

## How to Run the Project

1. Make sure you have both `chatbot.py` and `intents.json` in the same directory.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the files.
4. Run the following command:

   ```
   python chatbot.py
   ```

5. Start chatting with the bot!  
   Type `quit` to exit.

---
