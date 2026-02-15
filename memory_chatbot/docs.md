# Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Module Explanation](#module-explanation)
3. [Function Breakdown](#function-breakdown)
4. [Future Improvements](#future-improvements)
5. [Usage Examples](#usage-examples)

## Architecture Overview
The Context Aware Chatbot is designed as a modular system, with the main class `ContextAwareChatbot` encapsulating the core functionality. The chatbot utilizes the `limma.llm` library for natural language processing and generation. The system consists of the following components:
- **Memory Management**: The chatbot stores user-specific data in JSON files, including memory (name, preferences, facts, topics discussed) and conversation history.
- **Natural Language Processing (NLP)**: The chatbot uses simple keyword-based extraction for demo purposes, but can be extended to use more sophisticated NLP techniques.
- **Conversation Generation**: The chatbot generates responses based on user input and context, using the `limma.llm` library.

## Module Explanation
The chatbot is implemented in a single Python file, `memory_chatbot.py`, with the following modules:
- **`__init__`**: Initializes the chatbot with a user ID, loads or initializes memory, and configures the LLM library.
- **`load_memory`** and **`save_memory`**: Load and save user memory from/to JSON files.
- **`load_conversations`** and **`save_conversation`**: Load and save conversation history from/to JSON files.
- **`extract_facts`**: Extracts potential facts about the user from their input.
- **`update_system_prompt`**: Updates the system prompt with user context.
- **`process_message`**: Processes user messages with context awareness.
- **`get_summary`**: Generates a summary of user context.
- **`interactive_chat`**: Runs the main chat loop.

## Function Breakdown
The following functions are used in the chatbot:
- **`load_memory`**: Loads user memory from a JSON file.
- **`save_memory`**: Saves user memory to a JSON file.
- **`load_conversations`**: Loads conversation history from a JSON file.
- **`save_conversation`**: Saves a conversation turn to a JSON file.
- **`extract_facts`**: Extracts potential facts about the user from their input.
- **`update_system_prompt`**: Updates the system prompt with user context.
- **`process_message`**: Processes user messages with context awareness.
- **`get_summary`**: Generates a summary of user context.
- **`interactive_chat`**: Runs the main chat loop.

## Future Improvements
To further enhance the chatbot, the following improvements can be made:
- **Implement more sophisticated NLP techniques**: Use machine learning models or libraries like NLTK or spaCy to improve fact extraction and context understanding.
- **Integrate with external knowledge bases**: Use external knowledge bases like Wikipedia or Wikidata to provide more accurate and up-to-date information.
- **Improve conversation generation**: Use more advanced conversation generation techniques, such as sequence-to-sequence models or reinforcement learning.
- **Add support for multiple users**: Store user-specific data in a database or use a more robust memory management system.

## Usage Examples
To use the chatbot, simply run the `memory_chatbot.py` file and follow the prompts:
```bash
python memory_chatbot.py
```
Example conversation:
```
You: Hello
Bot: Hello! I'm your context-aware chatbot.
You: My name is John
Bot: Nice to meet you, John! I'll remember that.
You: summary
Bot: Context Summary for John
...
You: exit
Bot: Goodbye! I'll remember our conversation next time.
```