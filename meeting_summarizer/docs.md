# docs.md
## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Module Explanation](#module-explanation)
3. [Function Breakdown](#function-breakdown)
4. [Future Improvements](#future-improvements)
5. [Usage Examples](#usage-examples)

## Architecture Overview
The Meeting Summarizer is designed as a single class, `MeetingSummarizer`, which encapsulates all the functionality. It utilizes the `limma` library for voice assistant and language model capabilities. The program runs in a command-line interface, allowing users to interact with it through text-based commands.

The architecture can be broken down into the following components:

* **Voice Assistant**: Utilizes the `limma.voice` module to handle speech-to-text and text-to-speech functionality.
* **Language Model**: Configured using the `limma.llm` module to generate meeting summaries, extract action items, and identify participants.
* **Meeting Management**: Handles meeting recording, transcription, summary generation, and storage.

## Module Explanation
The `MeetingSummarizer` class is the core of the application. It includes the following modules:

* **`__init__`**: Initializes the voice assistant, configures the language model, and sets up the meeting file.
* **`load_meetings`**: Loads the meeting history from the file.
* **`save_meetings`**: Saves the meeting history to the file.
* **`start_recording`**: Starts a new meeting recording.
* **`record_meeting`**: Records the meeting in the background.
* **`stop_recording`**: Stops the meeting recording and returns the transcript.
* **`transcribe_meeting`**: Transcribes the meeting audio (currently simulated).
* **`summarize_meeting`**: Generates a meeting summary using the language model.
* **`extract_action_items`**: Extracts action items from the meeting transcript.
* **`identify_participants`**: Identifies meeting participants from the transcript.
* **`save_meeting`**: Saves a meeting record.
* **`search_meetings`**: Searches meeting records based on a query.
* **`get_meeting_stats`**: Retrieves meeting statistics.
* **`export_meeting`**: Exports a meeting record to a file.
* **`run`**: The main application loop.

## Function Breakdown
The following functions are used in the `MeetingSummarizer` class:

### Meeting Management
* **`start_recording`**: Starts a new meeting recording.
	+ Parameters: None
	+ Returns: None
* **`stop_recording`**: Stops the meeting recording and returns the transcript.
	+ Parameters: None
	+ Returns: Transcript (list of dictionaries)
* **`save_meeting`**: Saves a meeting record.
	+ Parameters: `title`, `transcript`, `summary`, `action_items`, `participants`
	+ Returns: Meeting ID (integer)

### Meeting Summarization
* **`summarize_meeting`**: Generates a meeting summary using the language model.
	+ Parameters: `transcript` (list of dictionaries)
	+ Returns: Summary (string)
* **`extract_action_items`**: Extracts action items from the meeting transcript.
	+ Parameters: `transcript` (list of dictionaries)
	+ Returns: Action items (list of dictionaries)
* **`identify_participants`**: Identifies meeting participants from the transcript.
	+ Parameters: `transcript` (list of dictionaries)
	+ Returns: Participants (list of dictionaries)

### Meeting Search and Export
* **`search_meetings`**: Searches meeting records based on a query.
	+ Parameters: `query` (string)
	+ Returns: Meeting records (list of dictionaries)
* **`export_meeting`**: Exports a meeting record to a file.
	+ Parameters: `meeting_id`, `format` (string)
	+ Returns: None

## Future Improvements
The following features can be added to enhance the Meeting Summarizer:

* **Speech-to-Text Integration**: Integrate a speech-to-text library to transcribe meeting audio.
* **Natural Language Processing**: Improve the language model to better understand meeting conversations.
* **Meeting Scheduling**: Integrate with calendar APIs to schedule meetings and send reminders.
* **User Authentication**: Add user authentication to secure meeting records and access.
* **Web Interface**: Develop a web interface for users to interact with the Meeting Summarizer.

## Usage Examples
The following examples demonstrate how to use the Meeting Summarizer:

### Starting a Meeting
```
Command: start
Meeting title: Team Meeting
```
This will start a new meeting recording.

### Stopping a Meeting
```
Command: stop
```
This will stop the meeting recording and generate a summary.

### Searching Meetings
```
Command: search
Search query: team
```
This will search meeting records for the query "team".

### Exporting a Meeting
```
Command: export
Meeting ID to export: 1
Format: txt
```
This will export the meeting record with ID 1 to a text file.