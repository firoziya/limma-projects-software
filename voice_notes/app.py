# voice_notes.py
from limma.voice import VoiceAssistant
import json
import os
from datetime import datetime
import hashlib

class VoiceNotes:
    def __init__(self):
        self.va = VoiceAssistant(speech_rate=160, female_voice=True)
        self.notes_file = "voice_notes.json"
        self.categories_file = "note_categories.json"
        self.notes = self.load_notes()
        self.categories = self.load_categories()
        
    def load_notes(self):
        """Load notes from file"""
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as f:
                return json.load(f)
        return []
        
    def save_notes(self):
        """Save notes to file"""
        with open(self.notes_file, 'w') as f:
            json.dump(self.notes, f, indent=2)
            
    def load_categories(self):
        """Load categories"""
        if os.path.exists(self.categories_file):
            with open(self.categories_file, 'r') as f:
                return json.load(f)
        return ["Personal", "Work", "Ideas", "Tasks", "Reminders"]
        
    def save_categories(self):
        """Save categories"""
        with open(self.categories_file, 'w') as f:
            json.dump(self.categories, f, indent=2)
            
    def create_note(self):
        """Create a new voice note"""
        self.va.speak("Creating new note. What would you like to write?")
        
        # Listen for note content
        content = self.va.listen(timeout=10)
        
        if content:
            # Select category
            self.va.speak("Select a category")
            print("\nCategories:")
            for i, cat in enumerate(self.categories, 1):
                print(f"{i}. {cat}")
                
            cat_choice = input("Category number (or say it): ")
            try:
                category = self.categories[int(cat_choice)-1]
            except:
                # Try voice input
                cat_voice = self.va.listen(timeout=3)
                if cat_voice and cat_voice in self.categories:
                    category = cat_voice
                else:
                    category = "Personal"
                    
            # Create note
            note = {
                "id": hashlib.md5((content + str(datetime.now())).encode()).hexdigest()[:8],
                "content": content,
                "category": category,
                "created": datetime.now().isoformat(),
                "modified": datetime.now().isoformat(),
                "reminder": None
            }
            
            self.notes.append(note)
            self.save_notes()
            
            self.va.speak(f"Note created in {category} category")
            print(f"\nNote ID: {note['id']}")
            print(f"Content: {content}")
            
    def search_notes(self):
        """Search notes by voice"""
        self.va.speak("What would you like to search for?")
        query = self.va.listen()
        
        if query:
            results = []
            for note in self.notes:
                if query.lower() in note['content'].lower():
                    results.append(note)
                    
            if results:
                self.va.speak(f"Found {len(results)} notes")
                for note in results:
                    print(f"\n[{note['category']}] {note['content'][:100]}...")
                    print(f"Created: {note['created'][:10]}")
                    
                # Option to read a note
                self.va.speak("Would you like me to read any of these notes?")
                response = self.va.listen()
                
                if "yes" in response.lower():
                    self.va.speak("Which note number?")
                    idx = int(self.va.listen()) - 1
                    if 0 <= idx < len(results):
                        self.va.speak(results[idx]['content'])
            else:
                self.va.speak("No notes found")
                
    def read_notes(self):
        """Read notes aloud"""
        if not self.notes:
            self.va.speak("No notes to read")
            return
            
        print("\n=== Your Notes ===")
        for i, note in enumerate(self.notes[-5:], 1):  # Last 5 notes
            print(f"{i}. [{note['category']}] {note['content'][:50]}...")
            
        self.va.speak(f"You have {len(self.notes)} notes. Which one would you like me to read?")
        
        try:
            choice = int(self.va.listen()) - 1
            if 0 <= choice < len(self.notes[-5:]):
                note = self.notes[-5:][choice]
                print(f"\nFull note: {note['content']}")
                self.va.speak(note['content'])
        except:
            self.va.speak("Reading your latest note")
            self.va.speak(self.notes[-1]['content'])
            
    def edit_note(self):
        """Edit an existing note"""
        if not self.notes:
            self.va.speak("No notes to edit")
            return
            
        # List recent notes
        print("\nRecent notes:")
        for i, note in enumerate(self.notes[-5:], 1):
            print(f"{i}. {note['content'][:50]}...")
            
        self.va.speak("Which note would you like to edit?")
        
        try:
            choice = int(self.va.listen()) - 1
            if 0 <= choice < len(self.notes[-5:]):
                note = self.notes[-5:][choice]
                
                print(f"\nCurrent note: {note['content']}")
                self.va.speak(f"Current note: {note['content'][:100]}")
                
                self.va.speak("Say your new note content")
                new_content = self.va.listen()
                
                if new_content:
                    note['content'] = new_content
                    note['modified'] = datetime.now().isoformat()
                    self.save_notes()
                    self.va.speak("Note updated")
                    
        except Exception as e:
            print(f"Error: {e}")
            
    def delete_note(self):
        """Delete a note"""
        if not self.notes:
            self.va.speak("No notes to delete")
            return
            
        print("\nRecent notes:")
        for i, note in enumerate(self.notes[-5:], 1):
            print(f"{i}. {note['content'][:50]}...")
            
        self.va.speak("Which note would you like to delete?")
        
        try:
            choice = int(self.va.listen()) - 1
            if 0 <= choice < len(self.notes[-5:]):
                note = self.notes[-5:][choice]
                
                self.va.speak(f"Are you sure you want to delete: {note['content'][:50]}")
                confirm = self.va.listen()
                
                if "yes" in confirm.lower():
                    self.notes.remove(note)
                    self.save_notes()
                    self.va.speak("Note deleted")
                    
        except Exception as e:
            print(f"Error: {e}")
            
    def set_reminder(self):
        """Set a reminder for a note"""
        if not self.notes:
            self.va.speak("No notes to set reminder for")
            return
            
        print("\nRecent notes:")
        for i, note in enumerate(self.notes[-5:], 1):
            print(f"{i}. {note['content'][:50]}...")
            
        self.va.speak("Which note should I remind you about?")
        
        try:
            choice = int(self.va.listen()) - 1
            if 0 <= choice < len(self.notes[-5:]):
                note = self.notes[-5:][choice]
                
                self.va.speak("When should I remind you?")
                reminder_time = self.va.listen()
                
                note['reminder'] = {
                    "time": reminder_time,
                    "set": datetime.now().isoformat()
                }
                self.save_notes()
                self.va.speak(f"Reminder set for {reminder_time}")
                
        except Exception as e:
            print(f"Error: {e}")
            
    def categorize_notes(self):
        """Categorize or re-categorize notes"""
        self.va.speak("Note categorization")
        
        # Show uncategorized or all notes
        uncategorized = [n for n in self.notes if n['category'] == 'Personal']
        
        if uncategorized:
            self.va.speak(f"You have {len(uncategorized)} notes that might need categorization")
            
            for note in uncategorized[:3]:
                print(f"\nNote: {note['content'][:100]}")
                self.va.speak(f"Note: {note['content'][:100]}")
                
                print("\nAvailable categories:")
                for i, cat in enumerate(self.categories, 1):
                    print(f"{i}. {cat}")
                    
                self.va.speak("Which category should this go in?")
                cat_choice = self.va.listen()
                
                try:
                    cat_idx = int(cat_choice) - 1
                    if 0 <= cat_idx < len(self.categories):
                        note['category'] = self.categories[cat_idx]
                        self.va.speak(f"Moved to {self.categories[cat_idx]}")
                except:
                    # Try matching by voice
                    for cat in self.categories:
                        if cat.lower() in cat_choice.lower():
                            note['category'] = cat
                            self.va.speak(f"Moved to {cat}")
                            break
                            
            self.save_notes()
            
    def get_summary(self):
        """Get summary of notes"""
        total = len(self.notes)
        by_category = {}
        for note in self.notes:
            cat = note['category']
            by_category[cat] = by_category.get(cat, 0) + 1
            
        summary = f"You have {total} notes. "
        for cat, count in by_category.items():
            summary += f"{count} in {cat}. "
            
        print(summary)
        self.va.speak(summary)
        
        # Most recent note
        if self.notes:
            latest = self.notes[-1]
            print(f"\nLatest note: {latest['content'][:100]}...")
            
    def run(self):
        """Main application loop"""
        print("\n📝 Voice-Activated Note-Taking App")
        print("=" * 40)
        print("Available voice commands:")
        print("  • 'create note' - Make a new note")
        print("  • 'search notes' - Find notes")
        print("  • 'read notes' - Listen to notes")
        print("  • 'edit note' - Modify a note")
        print("  • 'delete note' - Remove a note")
        print("  • 'set reminder' - Add reminder")
        print("  • 'categorize' - Organize notes")
        print("  • 'summary' - Note statistics")
        print("  • 'exit' - Quit")
        print("-" * 40)
        
        self.va.speak("Voice notes ready. Say a command.")
        
        while True:
            print("\nListening for command...")
            command = self.va.listen(timeout=5)
            
            if command:
                print(f"Command: {command}")
                cmd_lower = command.lower()
                
                if "exit" in cmd_lower or "quit" in cmd_lower:
                    self.va.speak("Goodbye!")
                    break
                elif "create" in cmd_lower or "new note" in cmd_lower:
                    self.create_note()
                elif "search" in cmd_lower:
                    self.search_notes()
                elif "read" in cmd_lower or "listen" in cmd_lower:
                    self.read_notes()
                elif "edit" in cmd_lower:
                    self.edit_note()
                elif "delete" in cmd_lower or "remove" in cmd_lower:
                    self.delete_note()
                elif "reminder" in cmd_lower:
                    self.set_reminder()
                elif "categorize" in cmd_lower:
                    self.categorize_notes()
                elif "summary" in cmd_lower or "stats" in cmd_lower:
                    self.get_summary()
                elif "help" in cmd_lower:
                    print("\nAvailable commands:")
                    for cmd in ["create note", "search notes", "read notes", 
                               "edit note", "delete note", "set reminder", 
                               "categorize", "summary"]:
                        print(f"  • '{cmd}'")

def main():
    app = VoiceNotes()
    app.run()

if __name__ == "__main__":
    main()