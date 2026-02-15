# Context Aware Chatbot
=======================

## Project Title
Context Aware Chatbot is a Python-based chatbot that utilizes natural language processing to provide personalized conversations. It remembers previous discussions and adapts to the user's communication style.

## Description
This project implements a context-aware chatbot using the LLaMA (Large Language Model Application) framework. The chatbot is designed to engage in conversations, remember previous interactions, and learn about the user over time. It uses a simple keyword-based approach to extract facts about the user and update its knowledge base.

## Installation
To install the required dependencies, run the following command:

```bash
pip install limma
```

Additionally, you need to set up your Gemini API key as an environment variable. You can do this by running:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Replace `"your-api-key-here"` with your actual Gemini API key.

## Usage
To start the chatbot, simply run the `memory_chatbot.py` script:

```bash
python memory_chatbot.py
```

You will be prompted to enter a user ID (or press Enter for the default user). The chatbot will then engage in a conversation with you, remembering previous interactions and adapting to your communication style.

## Example
Here's an example conversation with the chatbot:

```
You: Hello, my name is John
Bot: Hello John! It's nice to meet you.
You: I like playing tennis
Bot: Tennis is a great sport! Do you have a favorite tennis player?
You: Yes, I like Rafael Nadal
Bot: Nadal is an amazing player! I'll remember that you like tennis and Nadal.
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Note: This README.md is based on the provided code and may need to be adjusted according to the actual project structure and requirements.