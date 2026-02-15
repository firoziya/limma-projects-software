# Automated Meeting Summarizer
==========================

## Description
The Automated Meeting Summarizer is a Python application designed to record, transcribe, and summarize meetings. It utilizes a voice assistant and a large language model to generate meeting summaries, extract action items, and identify participants.

## Installation
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```
Make sure to replace `requirements.txt` with the actual file containing the dependencies.

## Usage
1. Run the application using `python meeting_summarizer.py`.
2. Follow the on-screen instructions to start a new meeting, stop the recording, and view past meetings.
3. Use the `start` command to begin a new meeting recording.
4. Use the `stop` command to end the recording and generate a meeting summary.
5. Use the `list` command to view past meetings.
6. Use the `search` command to search for meetings by keyword.
7. Use the `stats` command to view meeting statistics.
8. Use the `export` command to export a meeting to a file.

## Example
Here's an example of how to use the application:
```
$ python meeting_summarizer.py

🎙️ Automated Meeting Summarizer
================================
Commands:
  • start - Begin meeting recording
  • stop - End recording and summarize
  • list - View past meetings
  • search - Search meetings
  • stats - View statistics
  • export - Export meeting
  • exit - Quit
--------------------------------
Command: start
Meeting title: Example Meeting
🔴 Recording started...
```
After the meeting, use the `stop` command to generate a summary:
```
Command: stop
⏹️ Recording stopped. Duration: 300 seconds
Captured 10 statements

MEETING SUMMARY:
=================
...
ACTION ITEMS:
=================
...
PARTICIPANTS:
=================
...
✅ Meeting saved (ID: 1)
```
## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author
firoziya

Note: This README is a basic example and may need to be modified to fit the specific needs of your project. Additionally, you will need to create a `requirements.txt` file and a `LICENSE` file to complete the installation and licensing sections.