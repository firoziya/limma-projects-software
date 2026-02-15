# story_generator.py
from limma.llm import config, generate, chat, reset_chat
from limma.voice import VoiceAssistant
import json
import os
from datetime import datetime

class StoryGenerator:
    def __init__(self):
        self.va = VoiceAssistant(speech_rate=160)
        
        # Configure LLM
        config(
            provider="gemini",  # Free tier for story generation
            api_key=os.getenv("GEMINI_API_KEY", "your-key-here"),
            model="gemini-2.5-flash"
        )
        
        self.genres = {
            "1": "Fantasy",
            "2": "Science Fiction",
            "3": "Mystery",
            "4": "Romance",
            "5": "Horror",
            "6": "Adventure",
            "7": "Historical Fiction",
            "8": "Comedy",
            "9": "Drama",
            "10": "Fairy Tale"
        }
        
        self.stories_file = "stories.json"
        self.stories = self.load_stories()
        self.current_story = None
        
    def load_stories(self):
        """Load saved stories"""
        if os.path.exists(self.stories_file):
            with open(self.stories_file, 'r') as f:
                return json.load(f)
        return []
        
    def save_stories(self):
        """Save stories to file"""
        with open(self.stories_file, 'w') as f:
            json.dump(self.stories, f, indent=2)
            
    def generate_story_idea(self):
        """Generate a random story idea"""
        prompt = """Generate a creative story idea including:
        1. A unique premise
        2. Main character description
        3. Setting
        4. Central conflict
        
        Make it engaging and original."""
        
        idea = generate(prompt)
        print("\n" + "="*50)
        print("STORY IDEA:")
        print("="*50)
        print(idea)
        
        return idea
        
    def create_story(self):
        """Start a new story"""
        print("\n=== Create New Story ===")
        
        # Choose method
        print("\nHow would you like to start?")
        print("1. Use my own idea")
        print("2. Generate a random idea")
        print("3. Start from a genre")
        
        choice = input("Choose (1-3): ")
        
        if choice == "1":
            premise = input("Enter your story premise: ")
            title = input("Enter story title (optional): ")
            if not title:
                title = f"Story_{len(self.stories)+1}"
                
        elif choice == "2":
            premise = self.generate_story_idea()
            title = input("Enter story title: ")
            
        elif choice == "3":
            print("\nSelect genre:")
            for key, genre in self.genres.items():
                print(f"{key}. {genre}")
            genre_choice = input("Choose genre: ")
            genre = self.genres.get(genre_choice, "Fantasy")
            
            premise = input("Enter a brief premise (or press Enter for AI generation): ")
            if not premise:
                premise = generate(f"Create a story premise for a {genre} story")
                
            title = input("Enter story title: ")
            
        # Initialize story
        self.current_story = {
            "id": len(self.stories) + 1,
            "title": title,
            "genre": genre if 'genre' in locals() else "Custom",
            "premise": premise,
            "chapters": [],
            "characters": [],
            "created": datetime.now().isoformat(),
            "last_modified": datetime.now().isoformat()
        }
        
        # Generate first chapter
        self.generate_chapter(1)
        
        self.stories.append(self.current_story)
        self.save_stories()
        
        print(f"\n✅ Story '{title}' created!")
        
    def generate_chapter(self, chapter_num):
        """Generate a story chapter"""
        if not self.current_story:
            print("No active story")
            return
            
        # Build context from previous chapters
        context = ""
        if self.current_story['chapters']:
            context = "Previous chapters:\n"
            for ch in self.current_story['chapters'][-2:]:  # Last 2 chapters
                context += f"Chapter {ch['number']}: {ch['summary']}\n"
                
        # Generate chapter
        prompt = f"""Continue this story:

Title: {self.current_story['title']}
Genre: {self.current_story['genre']}
Premise: {self.current_story['premise']}
Characters: {', '.join(self.current_story['characters']) if self.current_story['characters'] else 'To be developed'}

{context}

Write Chapter {chapter_num} of this story. Make it engaging and move the plot forward.
Include dialogue and description. Chapter should be about 500 words.
Title this chapter creatively.

Chapter {chapter_num}:"""
        
        print(f"\n📝 Generating Chapter {chapter_num}...")
        chapter_content = generate(prompt)
        
        # Extract chapter title
        chapter_lines = chapter_content.split('\n')
        chapter_title = chapter_lines[0].strip() if chapter_lines else f"Chapter {chapter_num}"
        
        # Create chapter
        chapter = {
            "number": chapter_num,
            "title": chapter_title,
            "content": chapter_content,
            "summary": chapter_content[:200] + "...",
            "generated": datetime.now().isoformat()
        }
        
        self.current_story['chapters'].append(chapter)
        self.current_story['last_modified'] = datetime.now().isoformat()
        
        print(f"\n✅ Chapter {chapter_num} generated!")
        print("-"*40)
        print(chapter_content[:500] + "...")
        print("-"*40)
        
        return chapter
        
    def develop_character(self):
        """Develop a character for the story"""
        if not self.current_story:
            print("No active story")
            return
            
        print("\n=== Character Development ===")
        
        # Get character details
        name = input("Character name: ")
        role = input("Character role (protagonist/antagonist/supporting): ")
        
        prompt = f"""Create a detailed character profile for {name}, who is a {role} in a {self.current_story['genre']} story.

Include:
1. Physical description
2. Personality traits
3. Background/history
4. Motivations and goals
5. Strengths and weaknesses
6. Relationships with other characters
7. Character arc (how they might change)

Make the character compelling and three-dimensional."""
        
        print(f"\n📝 Developing character {name}...")
        character_profile = generate(prompt)
        
        character = {
            "name": name,
            "role": role,
            "profile": character_profile,
            "created": datetime.now().isoformat()
        }
        
        self.current_story['characters'].append(character)
        self.save_stories()
        
        print("\n" + "="*50)
        print(f"CHARACTER: {name}")
        print("="*50)
        print(character_profile)
        
    def plot_twist(self):
        """Generate a plot twist"""
        if not self.current_story or not self.current_story['chapters']:
            print("Need at least one chapter for plot twist")
            return
            
        prompt = f"""Based on this story:

Title: {self.current_story['title']}
Genre: {self.current_story['genre']}
Premise: {self.current_story['premise']}
Latest chapter summary: {self.current_story['chapters'][-1]['summary'] if self.current_story['chapters'] else 'Story just starting'}

Suggest an unexpected plot twist that would:
1. Surprise the reader
2. Make sense within the story
3. Raise the stakes
4. Lead to new conflicts

Describe the twist and how it would affect the story."""
        
        print("\n🔄 Generating plot twist...")
        twist = generate(prompt)
        
        print("\n" + "="*50)
        print("PLOT TWIST IDEA:")
        print("="*50)
        print(twist)
        
        # Option to incorporate twist
        use_twist = input("\nWould you like to use this twist? (y/n): ").lower()
        if use_twist == 'y':
            # Add to story notes
            if 'plot_twists' not in self.current_story:
                self.current_story['plot_twists'] = []
            self.current_story['plot_twists'].append({
                "twist": twist,
                "added": datetime.now().isoformat()
            })
            self.save_stories()
            print("✅ Twist saved to story notes!")
            
    def voice_storytelling(self):
        """Tell the story aloud"""
        if not self.current_story or not self.current_story['chapters']:
            self.va.speak("No story to tell yet")
            return
            
        print("\n🎧 Voice Storytelling Mode")
        print("Commands: 'next chapter', 'pause', 'continue', 'stop'")
        
        chapter_index = 0
        paused = False
        
        while chapter_index < len(self.current_story['chapters']):
            chapter = self.current_story['chapters'][chapter_index]
            
            if not paused:
                self.va.speak(f"Chapter {chapter['number']}: {chapter['title']}")
                
                # Read chapter in chunks
                chunk_size = 500
                content = chapter['content']
                
                for i in range(0, len(content), chunk_size):
                    chunk = content[i:i+chunk_size]
                    self.va.speak(chunk)
                    
                    # Check for pause command
                    print("\nListening for commands...")
                    command = self.va.listen(timeout=2)
                    if command and "pause" in command.lower():
                        paused = True
                        self.va.speak("Paused. Say continue when ready.")
                        break
                        
            if paused:
                command = self.va.listen(timeout=10)
                if command:
                    if "continue" in command.lower():
                        paused = False
                    elif "stop" in command.lower():
                        return
                        
            if not paused:
                chapter_index += 1
                
    def continue_story(self):
        """Continue the current story"""
        if not self.current_story:
            print("No active story")
            return
            
        next_chapter = len(self.current_story['chapters']) + 1
        self.generate_chapter(next_chapter)
        
    def save_story(self):
        """Save current story"""
        if self.current_story:
            self.save_stories()
            print(f"✅ Story '{self.current_story['title']}' saved")
            
    def load_story(self):
        """Load a saved story"""
        if not self.stories:
            print("No saved stories")
            return
            
        print("\n=== Saved Stories ===")
        for story in self.stories[-10:]:
            print(f"ID: {story['id']} | {story['title']} | Genre: {story['genre']} | Chapters: {len(story['chapters'])}")
            
        try:
            story_id = int(input("\nEnter story ID to load: "))
            story = next((s for s in self.stories if s['id'] == story_id), None)
            
            if story:
                self.current_story = story
                print(f"✅ Loaded '{story['title']}'")
                
                # Show summary
                print(f"\nTitle: {story['title']}")
                print(f"Genre: {story['genre']}")
                print(f"Premise: {story['premise']}")
                print(f"Chapters: {len(story['chapters'])}")
                print(f"Characters: {len(story['characters'])}")
            else:
                print("Story not found")
        except ValueError:
            print("Invalid ID")
            
    def run(self):
        """Main application loop"""
        print("\n📖 Interactive Story Generator")
        print("=" * 40)
        print("Commands:")
        print("  • new - Start a new story")
        print("  • load - Load a saved story")
        print("  • chapter - Generate next chapter")
        print("  • character - Develop a character")
        print("  • twist - Generate plot twist")
        print("  • tell - Voice storytelling")
        print("  • save - Save current story")
        print("  • list - List all stories")
        print("  • exit - Quit")
        print("-" * 40)
        
        while True:
            command = input("\nCommand: ").lower().strip()
            
            if command == "exit":
                if self.current_story:
                    save = input("Save current story before exiting? (y/n): ").lower()
                    if save == 'y':
                        self.save_story()
                print("Happy writing! Goodbye!")
                break
                
            elif command == "new":
                self.create_story()
                
            elif command == "load":
                self.load_story()
                
            elif command == "chapter":
                self.continue_story()
                
            elif command == "character":
                self.develop_character()
                
            elif command == "twist":
                self.plot_twist()
                
            elif command == "tell":
                self.voice_storytelling()
                
            elif command == "save":
                self.save_story()
                
            elif command == "list":
                if self.stories:
                    print("\n=== All Stories ===")
                    for story in self.stories:
                        print(f"ID: {story['id']} | {story['title']} | {story['genre']} | Chapters: {len(story['chapters'])}")
                else:
                    print("No stories yet")
                    
            elif command == "help":
                print("\nAvailable commands:")
                print("  new - Start a new story")
                print("  load - Load a saved story")
                print("  chapter - Generate next chapter")
                print("  character - Develop a character")
                print("  twist - Generate plot twist")
                print("  tell - Voice storytelling")
                print("  save - Save current story")
                print("  list - List all stories")
                print("  exit - Quit")

def main():
    generator = StoryGenerator()
    generator.run()

if __name__ == "__main__":
    main()