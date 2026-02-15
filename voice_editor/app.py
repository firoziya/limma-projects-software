# voice_editor.py
from limma.voice import VoiceAssistant
import os
from datetime import datetime
import keyboard  # pip install keyboard

class VoiceControlledEditor:
    def __init__(self):
        self.va = VoiceAssistant(speech_rate=160, female_voice=True)
        self.current_file = None
        self.content = ""
        self.commands = {
            "new": self.new_file,
            "open": self.open_file,
            "save": self.save_file,
            "save as": self.save_as,
            "read": self.read_content,
            "clear": self.clear_content,
            "add": self.add_text,
            "delete": self.delete_text,
            "find": self.find_text,
            "replace": self.replace_text,
            "word count": self.word_count,
            "time": self.insert_time,
            "date": self.insert_date,
            "help": self.show_help
        }
        
    def new_file(self):
        """Create a new file"""
        if self.content:
            confirm = input("Save current file? (y/n): ")
            if confirm.lower() == 'y':
                self.save_file()
        self.content = ""
        self.current_file = None
        self.va.speak("New file created")
        
    def open_file(self, filename=None):
        """Open a file"""
        if not filename:
            filename = input("Enter filename to open: ")
            
        try:
            with open(filename, 'r') as f:
                self.content = f.read()
            self.current_file = filename
            self.va.speak(f"Opened {filename}")
            print(f"\n--- {filename} ---\n{self.content[:200]}...")
        except Exception as e:
            self.va.speak(f"Error opening file: {e}")
            
    def save_file(self):
        """Save current file"""
        if self.current_file:
            with open(self.current_file, 'w') as f:
                f.write(self.content)
            self.va.speak(f"Saved to {self.current_file}")
        else:
            self.save_as()
            
    def save_as(self):
        """Save as new file"""
        filename = input("Enter filename to save as: ")
        try:
            with open(filename, 'w') as f:
                f.write(self.content)
            self.current_file = filename
            self.va.speak(f"Saved as {filename}")
        except Exception as e:
            self.va.speak(f"Error saving: {e}")
            
    def read_content(self):
        """Read current content aloud"""
        if self.content:
            self.va.speak("Reading content")
            # Read in chunks
            chunk_size = 500
            for i in range(0, len(self.content), chunk_size):
                chunk = self.content[i:i+chunk_size]
                self.va.speak(chunk)
        else:
            self.va.speak("No content to read")
            
    def clear_content(self):
        """Clear all content"""
        confirm = input("Clear all content? (y/n): ")
        if confirm.lower() == 'y':
            self.content = ""
            self.va.speak("Content cleared")
            
    def add_text(self, text=None):
        """Add text to content"""
        if not text:
            self.va.speak("What text would you like to add?")
            text = self.va.listen()
            
        if text:
            self.content += text + "\n"
            self.va.speak("Text added")
            
    def delete_text(self):
        """Delete text (last line or search)"""
        self.va.speak("Delete last line or search for text to delete?")
        choice = self.va.listen()
        
        if "last" in choice.lower():
            lines = self.content.split('\n')
            if lines:
                deleted = lines.pop()
                self.content = '\n'.join(lines)
                self.va.speak(f"Deleted: {deleted}")
        else:
            self.va.speak("What text would you like to delete?")
            text = self.va.listen()
            if text and text in self.content:
                self.content = self.content.replace(text, "")
                self.va.speak(f"Deleted all instances of {text}")
                
    def find_text(self):
        """Find text in content"""
        self.va.speak("What text would you like to find?")
        text = self.va.listen()
        
        if text:
            count = self.content.count(text)
            if count > 0:
                self.va.speak(f"Found {count} occurrences")
                # Show context
                lines = self.content.split('\n')
                for i, line in enumerate(lines, 1):
                    if text in line:
                        print(f"{i}: {line}")
            else:
                self.va.speak("Text not found")
                
    def replace_text(self):
        """Replace text in content"""
        self.va.speak("What text would you like to replace?")
        old = self.va.listen()
        
        if old and old in self.content:
            self.va.speak(f"What should I replace {old} with?")
            new = self.va.listen()
            
            if new:
                self.content = self.content.replace(old, new)
                self.va.speak("Replacement complete")
                
    def word_count(self):
        """Count words and characters"""
        words = len(self.content.split())
        chars = len(self.content)
        lines = len(self.content.split('\n'))
        
        stats = f"Words: {words}, Characters: {chars}, Lines: {lines}"
        print(stats)
        self.va.speak(stats)
        
    def insert_time(self):
        """Insert current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.content += f"\n{current_time}\n"
        self.va.speak(f"Time inserted: {current_time}")
        
    def insert_date(self):
        """Insert current date"""
        current_date = datetime.now().strftime("%B %d, %Y")
        self.content += f"\n{current_date}\n"
        self.va.speak(f"Date inserted: {current_date}")
        
    def show_help(self):
        """Show available commands"""
        help_text = "\nAvailable Voice Commands:\n"
        for cmd in self.commands.keys():
            help_text += f"  • {cmd}\n"
        print(help_text)
        self.va.speak("Available commands listed on screen")
        
    def process_voice_command(self, command):
        """Process voice command"""
        command_lower = command.lower()
        
        for cmd, func in self.commands.items():
            if cmd in command_lower:
                # Extract parameters if any
                params = command_lower.replace(cmd, "").strip()
                if params and cmd in ["open", "add"]:
                    func(params)
                else:
                    func()
                return True
        return False
        
    def run(self):
        """Main editor loop"""
        print("\n🎤 Voice-Controlled Text Editor")
        print("=" * 40)
        print("Commands available: new, open, save, save as, read, clear")
        print("add, delete, find, replace, word count, time, date, help")
        print("Say 'exit' to quit")
        print("-" * 40)
        
        self.va.speak("Voice editor ready. Say a command or start dictation.")
        
        while True:
            try:
                print("\nListening...")
                command = self.va.listen(timeout=5)
                
                if command:
                    print(f"You said: {command}")
                    
                    if "exit" in command.lower():
                        if self.content:
                            save = input("Save before exiting? (y/n): ")
                            if save.lower() == 'y':
                                self.save_file()
                        self.va.speak("Goodbye!")
                        break
                        
                    # Try to process as command
                    if not self.process_voice_command(command):
                        # If not a command, treat as dictation
                        if len(command.split()) > 3:  # Longer phrases are likely dictation
                            self.add_text(command)
                            
                # Show current content (limited)
                if self.content:
                    preview = self.content[-200:] if len(self.content) > 200 else self.content
                    print(f"\n--- Current Content (last {min(200, len(self.content))} chars) ---")
                    print(preview)
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    editor = VoiceControlledEditor()
    editor.run()

if __name__ == "__main__":
    main()