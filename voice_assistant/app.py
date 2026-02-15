# voice_assistant.py
from limma.voice import VoiceAssistant
from limma.llm import config, generate
import webbrowser
import os
import json
from datetime import datetime

class SmartVoiceAssistant:
    def __init__(self):
        # Initialize voice assistant
        self.va = VoiceAssistant(
            listen_timeout=5,
            speech_rate=150,
            volume=0.8,
            female_voice=True
        )
        
        # Configure LLM (using Gemini free tier as default)
        config(
            provider="gemini",
            api_key=os.getenv("GEMINI_API_KEY", "your-key-here"),
            model="gemini-2.5-flash"
        )
        
        # Load custom commands
        self.commands = self.load_commands()
        self.notes = []
        
    def load_commands(self):
        """Load custom voice commands"""
        return {
            "time": self.tell_time,
            "date": self.tell_date,
            "search": self.web_search,
            "note": self.take_note,
            "notes": self.read_notes,
            "weather": self.get_weather,
            "joke": self.tell_joke,
            "calculate": self.calculate
        }
        
    def tell_time(self):
        """Tell current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.va.speak(f"The current time is {current_time}")
        
    def tell_date(self):
        """Tell current date"""
        current_date = datetime.now().strftime("%B %d, %Y")
        self.va.speak(f"Today's date is {current_date}")
        
    def web_search(self, query):
        """Perform web search"""
        search_query = query.replace("search", "").strip()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            self.va.speak(f"Searching for {search_query}")
        else:
            self.va.speak("What would you like to search for?")
            
    def take_note(self, note_text):
        """Save a note"""
        note = note_text.replace("note", "").strip()
        if note:
            self.notes.append({
                "text": note,
                "timestamp": datetime.now().isoformat()
            })
            self.va.speak("Note saved")
        else:
            self.va.speak("What should I note down?")
            
    def read_notes(self):
        """Read saved notes"""
        if self.notes:
            self.va.speak(f"You have {len(self.notes)} notes")
            for i, note in enumerate(self.notes[-3:], 1):  # Last 3 notes
                self.va.speak(f"Note {i}: {note['text']}")
        else:
            self.va.speak("You have no saved notes")
            
    def get_weather(self, location=None):
        """Get weather information"""
        # This would integrate with a weather API
        self.va.speak("Weather feature coming soon!")
        
    def tell_joke(self):
        """Tell a joke using LLM"""
        joke = generate("Tell me a short, funny joke")
        self.va.speak(joke)
        
    def calculate(self, expression):
        """Perform calculation"""
        try:
            # Extract calculation from voice input
            calc = expression.replace("calculate", "").strip()
            result = eval(calc)
            self.va.speak(f"The result is {result}")
        except:
            self.va.speak("Sorry, I couldn't calculate that")
            
    def process_with_llm(self, command):
        """Use LLM to understand complex commands"""
        prompt = f"""Analyze this voice command and respond appropriately:
        Command: "{command}"
        
        If it's a simple task (time, date, search, etc.), just confirm it.
        If it's a question, provide a brief answer.
        If it's a general statement, respond naturally.
        """
        return generate(prompt)
        
    def run(self):
        """Main assistant loop"""
        self.va.speak("Hello! I'm your smart voice assistant. How can I help you?")
        
        while True:
            try:
                print("\nListening...")
                command = self.va.listen(timeout=5)
                
                if command:
                    print(f"You said: {command}")
                    
                    # Check for exit command
                    if "exit" in command.lower() or "goodbye" in command.lower():
                        self.va.speak("Goodbye! Have a great day!")
                        break
                        
                    # Check for custom commands
                    processed = False
                    for cmd, func in self.commands.items():
                        if cmd in command.lower():
                            if cmd in ["search", "note", "calculate"]:
                                func(command)
                            else:
                                func()
                            processed = True
                            break
                            
                    # If no custom command, use LLM
                    if not processed:
                        response = self.process_with_llm(command)
                        self.va.speak(response)
                        
            except Exception as e:
                print(f"Error: {e}")
                self.va.speak("Sorry, I encountered an error")
                
    def customize_voice(self):
        """Interactive voice customization"""
        print("\n=== Voice Customization ===")
        print("1. Change voice gender")
        print("2. Adjust speech rate")
        print("3. Adjust volume")
        print("4. List available voices")
        
        choice = input("Select option: ")
        
        if choice == "1":
            gender = input("Enter gender (male/female): ")
            if gender.lower() == "female":
                self.va.set_voice(True)
            elif gender.lower() == "male":
                self.va.set_voice(False)
            else:
                print("Invalid choice")
        elif choice == "2":
            rate = int(input("Enter speech rate (100-200): "))
            self.va.set_speech_rate(rate)
        elif choice == "3":
            volume = float(input("Enter volume (0.0-1.0): "))
            self.va.set_volume(volume)

def main():
    assistant = SmartVoiceAssistant()
    
    # Optional: Customize voice first
    customize = input("Would you like to customize voice settings? (y/n): ")
    if customize.lower() == 'y':
        assistant.customize_voice()
    
    # Run assistant
    assistant.run()

if __name__ == "__main__":
    main()