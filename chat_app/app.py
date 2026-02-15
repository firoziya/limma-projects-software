# chat_app.py
from limma.llm import config, chat, reset_chat
import os
from datetime import datetime

class LLMChatApp:
    def __init__(self):
        self.providers = {
            "1": {"name": "OpenAI", "models": ["gpt-5", "gpt-3.5-turbo"]},
            "2": {"name": "Gemini", "models": ["gemini-2.5-flash", "gemini-3-flash-preview"]},
            "3": {"name": "Groq", "models": ["llama-3.3-70b-versatile", "moonshotai/kimi-k2-instruct-0905"]},
            "4": {"name": "Mistral", "models": ["mistral-large-latest", "mistral-medium"]}
        }
        self.current_provider = None
        self.current_model = None
        
    def setup_provider(self):
        """Interactive provider setup"""
        print("\n=== Available AI Providers ===")
        for key, provider in self.providers.items():
            print(f"{key}. {provider['name']}")
        
        choice = input("\nSelect provider (1-4): ")
        if choice in self.providers:
            provider_name = self.providers[choice]["name"].lower()
            models = self.providers[choice]["models"]
            
            print(f"\nAvailable models for {self.providers[choice]['name']}:")
            for i, model in enumerate(models, 1):
                print(f"{i}. {model}")
            
            model_choice = int(input("Select model: ")) - 1
            self.current_model = models[model_choice]
            
            api_key = input(f"Enter your {self.providers[choice]['name']} API key: ")
            
            # Configure the provider
            config(
                provider=provider_name,
                api_key=api_key,
                model=self.current_model
            )
            self.current_provider = provider_name
            print(f"\n✅ Configured {self.providers[choice]['name']} with {self.current_model}")
        else:
            print("Invalid choice!")
            
    def chat_loop(self):
        """Main chat interaction loop"""
        if not self.current_provider:
            print("Please setup a provider first!")
            return
            
        print(f"\n=== Chat Session Started (Provider: {self.current_provider}, Model: {self.current_model}) ===")
        print("Type 'exit' to quit, 'switch' to change provider, 'new' to start new conversation")
        print("-" * 50)
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            elif user_input.lower() == 'switch':
                self.setup_provider()
                continue
            elif user_input.lower() == 'new':
                reset_chat()
                print("Started new conversation!")
                continue
                
            if user_input:
                try:
                    print("AI: ", end="", flush=True)
                    response = chat(user_input)
                    print(response)
                except Exception as e:
                    print(f"Error: {e}")
                    
    def save_conversation(self, filename=None):
        """Save chat history to file"""
        if not filename:
            filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        # Note: You'd need to capture chat history to implement this
        print(f"Conversation saved to {filename}")

def main():
    app = LLMChatApp()
    print("🌟 Welcome to Multi-Provider AI Chat!")
    app.setup_provider()
    app.chat_loop()

if __name__ == "__main__":
    main()