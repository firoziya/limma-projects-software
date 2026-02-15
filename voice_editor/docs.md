# docs.md
## Introduction
The Voice-Controlled Text Editor is a Python-based application that allows users to create, edit, and manage text files using voice commands. This documentation provides an overview of the application's architecture, modules, functions, and usage examples.

## Architecture Overview
The Voice-Controlled Text Editor consists of the following components:

*   **Voice Assistant**: The `VoiceAssistant` class from the `limma.voice` module is used to handle voice recognition and text-to-speech functionality.
*   **Editor**: The `VoiceControlledEditor` class is the core of the application, responsible for managing text files, processing voice commands, and interacting with the user.
*   **Main Loop**: The `run` method of the `VoiceControlledEditor` class contains the main loop of the application, where it continuously listens for voice commands and responds accordingly.

## Module Explanation
The application consists of a single module, `voice_editor.py`, which contains the following classes and functions:

*   **`VoiceControlledEditor` Class**: This class represents the voice-controlled text editor and contains methods for creating, opening, saving, and editing text files, as well as processing voice commands.
*   **`process_voice_command` Method**: This method takes a voice command as input and attempts to match it with a predefined set of commands. If a match is found, the corresponding action is performed.
*   **`run` Method**: This method contains the main loop of the application, where it continuously listens for voice commands and responds accordingly.

## Function Breakdown
The following functions are used in the application:

*   **`new_file`**: Creates a new text file and clears the current content.
*   **`open_file`**: Opens an existing text file and reads its content.
*   **`save_file`**: Saves the current content to the current file or prompts the user to save as a new file.
*   **`save_as`**: Saves the current content to a new file.
*   **`read_content`**: Reads the current content aloud.
*   **`clear_content`**: Clears the current content.
*   **`add_text`**: Adds text to the current content.
*   **`delete_text`**: Deletes text from the current content.
*   **`find_text`**: Finds text in the current content.
*   **`replace_text`**: Replaces text in the current content.
*   **`word_count`**: Counts the number of words and characters in the current content.
*   **`insert_time`**: Inserts the current time into the current content.
*   **`insert_date`**: Inserts the current date into the current content.
*   **`show_help`**: Displays a list of available voice commands.

## Future Improvements
The following features can be added to improve the application:

*   **Improved Voice Recognition**: Implementing more advanced voice recognition algorithms to improve accuracy and reduce errors.
*   **Multi-File Support**: Allowing users to work with multiple files simultaneously.
*   **File Management**: Providing features for managing files, such as renaming, deleting, and organizing them into folders.
*   **Collaboration**: Enabling multiple users to collaborate on a single file in real-time.
*   **Customization**: Allowing users to customize the application's settings, such as speech rate, voice, and commands.

## Usage Examples
To use the Voice-Controlled Text Editor, follow these steps:

1.  Run the application by executing the `voice_editor.py` script.
2.  Say a voice command to perform an action, such as "new" to create a new file or "open" to open an existing file.
3.  Use voice commands to edit the file, such as "add" to add text or "delete" to delete text.
4.  Say "save" to save the file or "save as" to save it as a new file.
5.  Use the "read" command to hear the current content aloud.
6.  Say "exit" to quit the application.

Some example voice commands include:

*   "New"
*   "Open filename"
*   "Save"
*   "Save as filename"
*   "Read"
*   "Clear"
*   "Add text"
*   "Delete text"
*   "Find text"
*   "Replace text"
*   "Word count"
*   "Time"
*   "Date"
*   "Help"