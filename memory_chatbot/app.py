# memory_chatbot.py
from limma.llm import config, generate, chat, reset_chat
import json
import os
from datetime import datetime
import hashlib

class ContextAwareChatbot:
    def __init__(self, user_id="default"):
        self.user_id = user_id
        self.memory_file = f"memory_{user_id}.json"
        self.conversation_file = f"conversations_{user_id}.json"
        
        # Load or initialize memory
        self.memory = self.load_memory()
        self.conversations = self.load_conversations()
        
        # Configure LLM (using Gemini as default)
        config(
            provider="gemini",
            api_key=os.getenv("GEMINI_API_KEY", "your-key-here"),
            model="gemini-2.5-flash"
        )
        
        # System prompt with context
        self.update_system_prompt()
        
    def load_memory(self):
        """Load user memory from file"""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        return {
            "name": None,
            "preferences": {},
            "facts": [],
            "topics_discussed": [],
            "last_interaction": None
        }
        
    def save_memory(self):
        """Save user memory to file"""
        self.memory["last_interaction"] = datetime.now().isoformat()
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)
            
    def load_conversations(self):
        """Load conversation history"""
        if os.path.exists(self.conversation_file):
            with open(self.conversation_file, 'r') as f:
                return json.load(f)
        return []
        
    def save_conversation(self, user_input, bot_response):
        """Save conversation turn"""
        self.conversations.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "bot": bot_response
        })
        
        # Keep only last 100 conversations
        if len(self.conversations) > 100:
            self.conversations = self.conversations[-100:]
            
        with open(self.conversation_file, 'w') as f:
            json.dump(self.conversations, f, indent=2)
            
    def extract_facts(self, text):
        """Extract potential facts about user"""
        facts = []
        
        # Look for personal information patterns
        patterns = [
            (r"my name is (\w+)", "name"),
            (r"I am (\d+)", "age"),
            (r"I like (\w+)", "preference"),
            (r"I work as (\w+)", "profession"),
            (r"I live in (\w+)", "location")
        ]
        
        # This would use more sophisticated NLP in production
        # Simple keyword-based for demo
        keywords = ["like", "love", "hate", "work", "live", "name", "age"]
        for keyword in keywords:
            if keyword in text.lower():
                facts.append(text)
                
        return facts
        
    def update_system_prompt(self):
        """Update system prompt with user context"""
        context = f"""You are a helpful AI assistant chatting with {self.memory.get('name', 'a user')}.

User Context:
- Name: {self.memory.get('name', 'Unknown')}
- Known preferences: {self.memory.get('preferences', {})}
- Topics previously discussed: {', '.join(self.memory.get('topics_discussed', [])[-5:])}

Guidelines:
1. Be friendly and conversational
2. Remember previous discussions
3. Ask clarifying questions when needed
4. Be concise but helpful
5. Adapt to user's communication style
"""
        
        # Reset chat and set new context
        reset_chat()
        # The first message will set the context
        generate(context)  # This primes the conversation
        
    def process_message(self, user_input):
        """Process user message with context awareness"""
        
        # Check for name if unknown
        if not self.memory["name"] and "my name is" in user_input.lower():
            import re
            name_match = re.search(r"my name is (\w+)", user_input, re.IGNORECASE)
            if name_match:
                self.memory["name"] = name_match.group(1)
                self.save_memory()
                
        # Extract potential facts
        new_facts = self.extract_facts(user_input)
        if new_facts:
            self.memory["facts"].extend(new_facts)
            
        # Update topics discussed
        words = set(user_input.lower().split())
        topics = [w for w in words if len(w) > 4]  # Simple topic extraction
        self.memory["topics_discussed"].extend(topics)
        
        # Generate response with context
        try:
            # Include recent conversation in context
            recent_context = ""
            if len(self.conversations) > 0:
                recent = self.conversations[-3:]  # Last 3 exchanges
                recent_context = "Recent conversation:\n"
                for exchange in recent:
                    recent_context += f"User: {exchange['user']}\nBot: {exchange['bot']}\n"
                    
            enhanced_input = f"{recent_context}\nCurrent user message: {user_input}"
            
            response = chat(enhanced_input)
            
            # Save conversation
            self.save_conversation(user_input, response)
            self.save_memory()
            
            return response
            
        except Exception as e:
            return f"Sorry, I encountered an error: {e}"
            
    def get_summary(self):
        """Get summary of user context"""
        summary = f"""
📊 Context Summary for {self.memory.get('name', 'Anonymous User')}

Known Information:
- Name: {self.memory.get('name', 'Not provided')}
- Preferences: {self.memory.get('preferences', {})}
- Facts stored: {len(self.memory.get('facts', []))}
- Topics discussed: {len(set(self.memory.get('topics_discussed', [])))}
- Total conversations: {len(self.conversations)}

Recent topics: {', '.join(set(self.memory.get('topics_discussed', []))[-10:])}
"""
        return summary
        
    def interactive_chat(self):
        """Main chat loop"""
        print(f"\n🌟 Hello {self.memory.get('name', 'User')}! I'm your context-aware chatbot.")
        print("I remember our conversations and learn about you over time.")
        print("Type 'summary' to see what I know about you")
        print("Type 'clear' to reset memory")
        print("Type 'exit' to quit")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() == 'exit':
                    print("Bot: Goodbye! I'll remember our conversation next time.")
                    break
                    
                elif user_input.lower() == 'summary':
                    print(self.get_summary())
                    continue
                    
                elif user_input.lower() == 'clear':
                    confirm = input("Are you sure? This will erase all memory. (yes/no): ")
                    if confirm.lower() == 'yes':
                        self.memory = {
                            "name": None,
                            "preferences": {},
                            "facts": [],
                            "topics_discussed": [],
                            "last_interaction": None
                        }
                        self.conversations = []
                        self.save_memory()
                        print("Bot: Memory cleared. I've forgotten everything.")
                        self.update_system_prompt()
                    continue
                    
                if user_input:
                    response = self.process_message(user_input)
                    print(f"Bot: {response}")
                    
            except KeyboardInterrupt:
                print("\nBot: Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    # Create chatbot for specific user
    user_id = input("Enter your user ID (or press Enter for default): ").strip()
    if not user_id:
        user_id = "default"
        
    chatbot = ContextAwareChatbot(user_id)
    chatbot.interactive_chat()

if __name__ == "__main__":
    main()