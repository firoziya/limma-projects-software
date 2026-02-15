# meeting_summarizer.py
from limma.voice import VoiceAssistant
from limma.llm import config, generate
import json
import os
from datetime import datetime
import threading
import time

class MeetingSummarizer:
    def __init__(self):
        self.va = VoiceAssistant()
        
        # Configure LLM for summarization
        config(
            provider="gemini",  # Free tier suitable for summarization
            api_key=os.getenv("GEMINI_API_KEY", "your-key-here"),
            model="gemini-2.5-flash"
        )
        
        self.meetings_file = "meetings.json"
        self.meetings = self.load_meetings()
        self.is_recording = False
        self.transcript = []
        
    def load_meetings(self):
        """Load meeting history"""
        if os.path.exists(self.meetings_file):
            with open(self.meetings_file, 'r') as f:
                return json.load(f)
        return []
        
    def save_meetings(self):
        """Save meetings to file"""
        with open(self.meetings_file, 'w') as f:
            json.dump(self.meetings, f, indent=2)
            
    def start_recording(self):
        """Start meeting recording"""
        self.is_recording = True
        self.transcript = []
        self.recording_start = datetime.now()
        
        print("\n🔴 Recording started...")
        self.va.speak("Meeting recording started")
        
        # Start recording thread
        self.recording_thread = threading.Thread(target=self.record_meeting)
        self.recording_thread.start()
        
    def record_meeting(self):
        """Record meeting in background"""
        while self.is_recording:
            try:
                # Listen for speech
                text = self.va.listen(timeout=10)
                if text:
                    timestamp = datetime.now().isoformat()
                    self.transcript.append({
                        "timestamp": timestamp,
                        "text": text
                    })
                    print(f"\n[{len(self.transcript)}] {text}")
            except:
                pass
                
    def stop_recording(self):
        """Stop meeting recording"""
        self.is_recording = False
        if hasattr(self, 'recording_thread'):
            self.recording_thread.join()
            
        duration = (datetime.now() - self.recording_start).total_seconds()
        
        print(f"\n⏹️ Recording stopped. Duration: {duration:.0f} seconds")
        print(f"Captured {len(self.transcript)} statements")
        
        return self.transcript
        
    def transcribe_meeting(self, audio_file=None):
        """Transcribe meeting audio (if file provided)"""
        if audio_file:
            # This would use speech-to-text on audio file
            # For now, we'll simulate with a placeholder
            print(f"Transcribing {audio_file}...")
            return ["Sample transcription line 1", "Sample transcription line 2"]
        return self.transcript
        
    def summarize_meeting(self, transcript):
        """Generate meeting summary"""
        if not transcript:
            return None
            
        # Prepare transcript text
        transcript_text = "\n".join([f"- {t['text']}" for t in transcript])
        
        prompt = f"""Please provide a comprehensive meeting summary based on this transcript:

TRANSCRIPT:
{transcript_text}

Please include:
1. Meeting Overview (brief summary)
2. Key Discussion Points (bullet points)
3. Decisions Made (bullet points)
4. Action Items (who, what, when)
5. Next Steps
6. Questions Left Unanswered

Format clearly with headers."""
        
        print("\n📝 Generating summary...")
        summary = generate(prompt)
        
        return summary
        
    def extract_action_items(self, transcript):
        """Extract action items from transcript"""
        if not transcript:
            return []
            
        transcript_text = "\n".join([f"- {t['text']}" for t in transcript])
        
        prompt = f"""Extract all action items from this meeting transcript.
        For each action item, identify:
        - Task description
        - Assigned person (if mentioned)
        - Deadline (if mentioned)
        
        Format as JSON list.
        
        Transcript:
        {transcript_text}
        
        Action items:"""
        
        try:
            action_items = generate(prompt)
            return action_items
        except:
            return "Could not extract action items"
            
    def identify_participants(self, transcript):
        """Identify meeting participants"""
        if not transcript:
            return []
            
        transcript_text = "\n".join([f"- {t['text']}" for t in transcript])
        
        prompt = f"""Identify all meeting participants from this transcript.
        List their names and any roles mentioned.
        
        Transcript:
        {transcript_text}
        
        Participants:"""
        
        try:
            participants = generate(prompt)
            return participants
        except:
            return "Could not identify participants"
            
    def save_meeting(self, title, transcript, summary, action_items, participants):
        """Save meeting record"""
        meeting = {
            "id": len(self.meetings) + 1,
            "title": title,
            "date": datetime.now().isoformat(),
            "duration": (datetime.now() - self.recording_start).total_seconds() if hasattr(self, 'recording_start') else 0,
            "transcript": transcript,
            "summary": summary,
            "action_items": action_items,
            "participants": participants,
            "transcript_count": len(transcript)
        }
        
        self.meetings.append(meeting)
        self.save_meetings()
        
        return meeting['id']
        
    def search_meetings(self, query):
        """Search meeting records"""
        results = []
        query = query.lower()
        
        for meeting in self.meetings:
            # Search in title and summary
            if query in meeting['title'].lower() or query in meeting['summary'].lower():
                results.append(meeting)
                continue
                
            # Search in transcript
            for item in meeting['transcript']:
                if query in item['text'].lower():
                    results.append(meeting)
                    break
                    
        return results
        
    def get_meeting_stats(self):
        """Get meeting statistics"""
        if not self.meetings:
            return "No meetings recorded"
            
        total_meetings = len(self.meetings)
        total_duration = sum(m.get('duration', 0) for m in self.meetings)
        total_statements = sum(m.get('transcript_count', 0) for m in self.meetings)
        
        stats = f"""
📊 Meeting Statistics:
- Total meetings: {total_meetings}
- Total meeting time: {total_duration/60:.1f} minutes
- Total statements recorded: {total_statements}
- Average statements per meeting: {total_statements/total_meetings:.1f}
"""
        return stats
        
    def export_meeting(self, meeting_id, format="txt"):
        """Export meeting to file"""
        meeting = next((m for m in self.meetings if m['id'] == meeting_id), None)
        
        if not meeting:
            print(f"Meeting {meeting_id} not found")
            return
            
        filename = f"meeting_{meeting_id}_{datetime.now().strftime('%Y%m%d')}"
        
        if format == "txt":
            filename += ".txt"
            with open(filename, 'w') as f:
                f.write(f"MEETING SUMMARY: {meeting['title']}\n")
                f.write(f"Date: {meeting['date']}\n")
                f.write("="*50 + "\n\n")
                f.write("SUMMARY:\n")
                f.write(meeting['summary'] + "\n\n")
                f.write("ACTION ITEMS:\n")
                f.write(meeting.get('action_items', 'None') + "\n\n")
                f.write("TRANSCRIPT:\n")
                for item in meeting['transcript']:
                    f.write(f"[{item['timestamp']}] {item['text']}\n")
                    
        elif format == "json":
            filename += ".json"
            with open(filename, 'w') as f:
                json.dump(meeting, f, indent=2)
                
        print(f"📄 Meeting exported to {filename}")
        
    def run(self):
        """Main application loop"""
        print("\n🎙️ Automated Meeting Summarizer")
        print("=" * 40)
        print("Commands:")
        print("  • start - Begin meeting recording")
        print("  • stop - End recording and summarize")
        print("  • list - View past meetings")
        print("  • search - Search meetings")
        print("  • stats - View statistics")
        print("  • export - Export meeting")
        print("  • exit - Quit")
        print("-" * 40)
        
        while True:
            command = input("\nCommand: ").lower().strip()
            
            if command == "exit":
                if self.is_recording:
                    self.stop_recording()
                print("Goodbye!")
                break
                
            elif command == "start":
                title = input("Meeting title: ")
                self.current_title = title
                self.start_recording()
                
            elif command == "stop":
                if self.is_recording:
                    transcript = self.stop_recording()
                    
                    # Generate summaries
                    summary = self.summarize_meeting(transcript)
                    print("\n" + "="*50)
                    print("MEETING SUMMARY:")
                    print("="*50)
                    print(summary)
                    
                    action_items = self.extract_action_items(transcript)
                    print("\n" + "="*50)
                    print("ACTION ITEMS:")
                    print("="*50)
                    print(action_items)
                    
                    participants = self.identify_participants(transcript)
                    print("\n" + "="*50)
                    print("PARTICIPANTS:")
                    print("="*50)
                    print(participants)
                    
                    # Save meeting
                    meeting_id = self.save_meeting(
                        self.current_title,
                        transcript,
                        summary,
                        action_items,
                        participants
                    )
                    print(f"\n✅ Meeting saved (ID: {meeting_id})")
                    
            elif command == "list":
                if self.meetings:
                    print("\n=== Past Meetings ===")
                    for meeting in self.meetings[-10:]:
                        print(f"ID: {meeting['id']} | {meeting['title']} | {meeting['date'][:10]} | {meeting['transcript_count']} statements")
                else:
                    print("No meetings recorded")
                    
            elif command == "search":
                query = input("Search query: ")
                results = self.search_meetings(query)
                
                if results:
                    print(f"\nFound {len(results)} meetings:")
                    for meeting in results:
                        print(f"ID: {meeting['id']} | {meeting['title']} | {meeting['date'][:10]}")
                else:
                    print("No matches found")
                    
            elif command == "stats":
                print(self.get_meeting_stats())
                
            elif command == "export":
                if self.meetings:
                    meeting_id = int(input("Meeting ID to export: "))
                    format = input("Format (txt/json): ").lower()
                    self.export_meeting(meeting_id, format)
                else:
                    print("No meetings to export")

def main():
    summarizer = MeetingSummarizer()
    summarizer.run()

if __name__ == "__main__":
    main()