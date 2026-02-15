# Multi-Provider AI Chat
==========================

## Description
A Python-based chat application that allows users to interact with multiple AI providers, including OpenAI, Gemini, Groq, and Mistral. The application provides an interactive interface for setting up providers, selecting models, and engaging in conversations.

## Installation
To use this application, you will need to have Python installed on your system. Additionally, you will need to install the required libraries by running the following command:
```bash
pip install limma
```
## Usage
To start the application, simply run the `chat_app.py` script:
```bash
python chat_app.py
```
Follow the interactive prompts to set up a provider, select a model, and start chatting.

## Example
Here's an example of how to use the application:
1. Run the application and select a provider (e.g., OpenAI).
2. Choose a model (e.g., gpt-3.5-turbo).
3. Enter your API key for the selected provider.
4. Start chatting by typing a message.
5. Type 'exit' to quit, 'switch' to change providers, or 'new' to start a new conversation.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Author
firoziya

Note: The `save_conversation` method is currently not implemented, as it requires capturing the chat history. You can modify this method to suit your needs.