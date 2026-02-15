# docs.md
## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Module Explanation](#module-explanation)
3. [Function Breakdown](#function-breakdown)
4. [Future Improvements](#future-improvements)
5. [Usage Examples](#usage-examples)

## Architecture Overview
The StoryGenerator application is built using a modular design, with the main components being:
*   **StoryGenerator class**: This class encapsulates the core functionality of the application, including story creation, chapter generation, character development, and voice storytelling.
*   **limma.llm module**: This module provides the necessary functionality for interacting with the language model, including generating text and resetting the chat context.
*   **limma.voice module**: This module provides the functionality for voice storytelling, including text-to-speech conversion and speech recognition.

## Module Explanation
The application uses the following modules:
*   **`limma.llm`**: This module provides the functionality for interacting with the language model. It includes functions for generating text, resetting the chat context, and configuring the model.
*   **`limma.voice`**: This module provides the functionality for voice storytelling. It includes functions for text-to-speech conversion and speech recognition.
*   **`json`**: This module provides the functionality for working with JSON data. It is used to load and save stories to a JSON file.
*   **`os`**: This module provides the functionality for interacting with the operating system. It is used to get the current working directory and to check if a file exists.
*   **`datetime`**: This module provides the functionality for working with dates and times. It is used to get the current date and time.

## Function Breakdown
The StoryGenerator class has the following methods:
*   **`__init__`**: This method initializes the StoryGenerator object. It sets up the voice assistant, configures the language model, and loads saved stories.
*   **`load_stories`**: This method loads saved stories from a JSON file.
*   **`save_stories`**: This method saves the current stories to a JSON file.
*   **`generate_story_idea`**: This method generates a random story idea using the language model.
*   **`create_story`**: This method creates a new story. It prompts the user for the story title, premise, and genre, and then generates the first chapter.
*   **`generate_chapter`**: This method generates a new chapter for the current story. It uses the language model to generate the chapter content.
*   **`develop_character`**: This method develops a character for the current story. It prompts the user for the character's name and role, and then generates a character profile using the language model.
*   **`plot_twist`**: This method generates a plot twist for the current story. It uses the language model to generate a twist based on the story's premise and latest chapter summary.
*   **`voice_storytelling`**: This method tells the current story aloud. It uses the voice assistant to read the story chapters.
*   **`continue_story`**: This method continues the current story. It generates the next chapter using the language model.
*   **`save_story`**: This method saves the current story to the JSON file.
*   **`load_story`**: This method loads a saved story from the JSON file.
*   **`run`**: This method runs the main application loop. It prompts the user for commands and executes the corresponding actions.

## Future Improvements
Some potential future improvements for the application include:
*   **Improved language model integration**: The application could benefit from more advanced language model integration, such as using a more sophisticated model or fine-tuning the model for specific genres or styles.
*   **More advanced character development**: The character development feature could be improved by adding more prompts or options for character customization.
*   **More advanced plot twist generation**: The plot twist generation feature could be improved by adding more prompts or options for twist customization.
*   **Multi-story support**: The application could be improved by adding support for multiple stories, allowing users to switch between different stories and continue where they left off.
*   **User authentication**: The application could be improved by adding user authentication, allowing users to save their stories and load them later.

## Usage Examples
Here are some examples of how to use the application:
*   **Create a new story**: Run the application and type "new" to create a new story. Follow the prompts to enter the story title, premise, and genre.
*   **Generate a chapter**: Type "chapter" to generate a new chapter for the current story.
*   **Develop a character**: Type "character" to develop a character for the current story. Follow the prompts to enter the character's name and role.
*   **Generate a plot twist**: Type "twist" to generate a plot twist for the current story.
*   **Tell the story aloud**: Type "tell" to tell the current story aloud. The application will use the voice assistant to read the story chapters.
*   **Save the story**: Type "save" to save the current story to the JSON file.
*   **Load a saved story**: Type "load" to load a saved story from the JSON file. Follow the prompts to enter the story ID.