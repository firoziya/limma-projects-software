# docs.md
## Introduction
This project is a multi-provider AI chat application built using Python. It allows users to interact with different AI providers and models, switch between them, and save conversation history.

## Architecture Overview
The application is designed as a single class `LLMChatApp` with several methods that handle different aspects of the chat functionality. The main components of the application are:

* Provider setup: Allows users to select a provider and configure the API key and model.
* Chat loop: Handles the main chat interaction, including user input, AI responses, and conversation management.
* Conversation saving: Saves the chat history to a file.

The application uses the `limma.llm` library to interact with the AI providers and models.

## Module Explanation
The application consists of a single module `chat_app.py` with the following sections:

* Importing libraries: The application imports the necessary libraries, including `limma.llm` for AI interactions, `os` for file operations, and `datetime` for timestamping conversation history files.
* Class definition: The `LLMChatApp` class is defined with several methods that handle the chat functionality.
* Main function: The `main` function creates an instance of the `LLMChatApp` class and starts the chat application.

## Function Breakdown
The following functions are defined in the `LLMChatApp` class:

* `__init__`: Initializes the application with a dictionary of available providers and their corresponding models.
* `setup_provider`: Allows users to select a provider and configure the API key and model.
* `chat_loop`: Handles the main chat interaction, including user input, AI responses, and conversation management.
* `save_conversation`: Saves the chat history to a file.

The following functions are defined in the `limma.llm` library:

* `config`: Configures the AI provider and model.
* `chat`: Sends a message to the AI provider and returns the response.
* `reset_chat`: Resets the chat conversation.

## Future Improvements
The following improvements can be made to the application:

* Implement chat history capture and saving to a file.
* Add error handling for API key and model configuration.
* Improve the user interface and experience.
* Add support for multiple conversation sessions.
* Implement a more robust provider and model selection system.

## Usage Examples
To use the application, follow these steps:

1. Run the `chat_app.py` script.
2. Select a provider from the list of available providers.
3. Configure the API key and model for the selected provider.
4. Start the chat conversation by typing a message.
5. Type 'exit' to quit the conversation, 'switch' to change providers, or 'new' to start a new conversation.
6. Save the conversation history to a file by typing 'save'.

Example output:
```
🌟 Welcome to Multi-Provider AI Chat!
=== Available AI Providers ===
1. OpenAI
2. Gemini
3. Groq
4. Mistral
Select provider (1-4): 1
Available models for OpenAI:
1. gpt-5
2. gpt-3.5-turbo
Select model: 1
Enter your openai API key: <API_KEY>
✅ Configured OpenAI with gpt-5
=== Chat Session Started (Provider: openai, Model: gpt-5) ===
Type 'exit' to quit, 'switch' to change provider, 'new' to start new conversation
--------------------------------------------------
You: Hello!
AI: Hello! How can I assist you today?
You: What is the weather like today?
AI: I'm not sure, but I can provide you with general information about the weather.
```
Note: The actual output will vary depending on the user input and the AI provider's response.