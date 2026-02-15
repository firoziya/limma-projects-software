# docs.md
## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Module Explanation](#module-explanation)
3. [Function Breakdown](#function-breakdown)
4. [Future Improvements](#future-improvements)
5. [Usage Examples](#usage-examples)

## Architecture Overview
The Smart Voice Assistant is designed as a modular system with the following components:
- **Voice Assistant**: Handles voice input and output using the `limma.voice` library.
- **LLM (Large Language Model)**: Utilizes the `limma.llm` library for natural language processing and understanding complex commands.
- **Custom Commands**: A dictionary of predefined voice commands that trigger specific actions.
- **Main Loop**: The core of the assistant that listens for voice input, processes commands, and responds accordingly.

## Module Explanation
The project consists of the following modules:
- `voice_assistant.py`: The main module containing the `SmartVoiceAssistant` class.
- `limma.voice`: A library for voice input and output.
- `limma.llm`: A library for natural language processing using large language models.

## Function Breakdown
The `SmartVoiceAssistant` class has the following key functions:
- `__init__`: Initializes the voice assistant with default settings and loads custom commands.
- `load_commands`: Loads a dictionary of custom voice commands.
- `tell_time`, `tell_date`, `web_search`, `take_note`, `read_notes`, `get_weather`, `tell_joke`, `calculate`: Implement custom commands.
- `process_with_llm`: Uses the LLM to understand complex commands.
- `run`: The main loop of the assistant that listens for voice input and processes commands.
- `customize_voice`: Allows interactive customization of voice settings.

## Future Improvements
- **Integrate Weather API**: Complete the implementation of the `get_weather` function by integrating with a weather API.
- **Expand Custom Commands**: Add more custom commands to enhance the assistant's functionality.
- **Improve Error Handling**: Enhance error handling to provide more informative error messages and prevent the assistant from crashing due to unexpected errors.
- **Support for Multiple LLMs**: Allow the user to choose from different LLMs or providers.

## Usage Examples
To use the Smart Voice Assistant:
1. Run the `voice_assistant.py` script.
2. Optional: Customize voice settings by choosing 'y' when prompted.
3. Interact with the assistant using voice commands, such as:
	* "What's the time?" or "Tell me the date"
	* "Search for [topic]"
	* "Note [message]"
	* "Read my notes"
	* "Tell me a joke"
	* "Calculate [expression]"
4. Exit the assistant by saying "exit" or "goodbye".

Example command-line interaction:
```
Would you like to customize voice settings? (y/n): y
=== Voice Customization ===
1. Change voice gender
2. Adjust speech rate
3. Adjust volume
4. List available voices
Select option: 2
Enter speech rate (100-200): 120
```
Note: Make sure to install the required libraries and set up the environment variables (e.g., `GEMINI_API_KEY`) before running the script.