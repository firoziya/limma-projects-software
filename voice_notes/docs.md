# docs.md
## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Module Explanation](#module-explanation)
3. [Function Breakdown](#function-breakdown)
4. [Future Improvements](#future-improvements)
5. [Usage Examples](#usage-examples)

## Architecture Overview
The Voice Notes application is designed as a simple, voice-activated note-taking system. The architecture consists of the following components:

*   **VoiceAssistant**: A class from the `limma.voice` module that provides the functionality for speech recognition and text-to-speech conversion.
*   **VoiceNotes**: The main class of the application, responsible for managing notes, handling voice commands, and interacting with the user.

## Module Explanation
The application is structured into the following modules:

*   **voice_notes.py**: The main module containing the VoiceNotes class and the application's entry point.
*   **limma.voice**: An external module providing the VoiceAssistant class for speech recognition and text-to-speech conversion.

## Function Breakdown
The VoiceNotes class contains the following methods:

*   **`__init__`**: Initializes the VoiceNotes object, setting up the VoiceAssistant instance and loading notes and categories from files.
*   **`load_notes`**: Loads notes from the "voice_notes.json" file.
*   **`save_notes`**: Saves notes to the "voice_notes.json" file.
*   **`load_categories`**: Loads categories from the "note_categories.json" file.
*   **`save_categories`**: Saves categories to the "note_categories.json" file.
*   **`create_note`**: Creates a new note based on user input.
*   **`search_notes`**: Searches notes based on a user-provided query.
*   **`read_notes`**: Reads notes aloud to the user.
*   **`edit_note`**: Edits an existing note based on user input.
*   **`delete_note`**: Deletes a note based on user input.
*   **`set_reminder`**: Sets a reminder for a note.
*   **`categorize_notes`**: Categorizes or re-categorizes notes.
*   **`get_summary`**: Provides a summary of notes.
*   **`run`**: The main application loop, handling user voice commands.

## Future Improvements
Some potential improvements to the application include:

*   **Note tagging**: Allowing users to assign tags to notes for easier searching and organization.
*   **Note prioritization**: Allowing users to prioritize notes based on importance or urgency.
*   **Reminder notifications**: Implementing a system to send notifications to the user when a reminder is due.
*   **Cloud synchronization**: Allowing users to synchronize their notes across multiple devices.

## Usage Examples
To use the Voice Notes application, follow these steps:

1.  Run the application using the `main.py` script.
2.  The application will prompt the user to say a command. Available commands include:
    *   "create note" - Create a new note.
    *   "search notes" - Search notes based on a query.
    *   "read notes" - Read notes aloud.
    *   "edit note" - Edit an existing note.
    *   "delete note" - Delete a note.
    *   "set reminder" - Set a reminder for a note.
    *   "categorize" - Categorize or re-categorize notes.
    *   "summary" - Get a summary of notes.
    *   "exit" - Quit the application.
3.  Follow the prompts and provide the necessary input to complete the desired action.

Example use cases:

*   Creating a new note: Say "create note" and follow the prompts to create a new note.
*   Searching notes: Say "search notes" and provide a query to search for notes.
*   Reading notes: Say "read notes" to hear the latest notes read aloud.