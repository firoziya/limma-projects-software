# content_generator.py
from limma.llm import config, generate
import json
from datetime import datetime
import os

class ContentGenerator:
    def __init__(self):
        self.providers = {
            "openai": {
                "api_key": os.getenv("OPENAI_API_KEY"),
                "models": ["gpt-5", "gpt-3.5-turbo"],
                "best_for": ["creative writing", "detailed content"]
            },
            "gemini": {
                "api_key": os.getenv("GEMINI_API_KEY"),
                "models": ["gemini-2.5-flash", "gemini-3-flash-preview"],
                "best_for": ["quick responses", "free tier"]
            },
            "groq": {
                "api_key": os.getenv("GROQ_API_KEY"),
                "models": ["moonshotai/kimi-k2-instruct-0905", "llama-3.3-70b-versatile"],
                "best_for": ["ultra-fast generation", "code"]
            },
            "mistral": {
                "api_key": os.getenv("MISTRAL_API_KEY"),
                "models": ["mistral-large-latest", "mistral-medium"],
                "best_for": ["technical content", "analysis"]
            }
        }
        
        self.content_templates = {
            "blog": "Write a blog post about {topic}. Style: {tone}. Length: {length} words.",
            "social": "Create a social media post about {topic} for {platform}. Make it {tone}.",
            "code": "Write {language} code to {task}. Include comments and error handling.",
            "email": "Write a professional email about {topic}. Tone: {tone}.",
            "poem": "Write a {style} poem about {topic}.",
            "story": "Write a short {genre} story about {topic}. Length: {length} words."
        }
        
    def setup_provider(self, provider_name, model=None):
        """Configure a specific provider"""
        if provider_name in self.providers:
            provider_config = self.providers[provider_name]
            if not provider_config["api_key"]:
                provider_config["api_key"] = input(f"Enter {provider_name} API key: ")
            
            if not model:
                print(f"\nAvailable models for {provider_name}:")
                for i, m in enumerate(provider_config["models"], 1):
                    print(f"{i}. {m}")
                model_choice = int(input("Select model: ")) - 1
                model = provider_config["models"][model_choice]
            
            config(
                provider=provider_name,
                api_key=provider_config["api_key"],
                model=model
            )
            return True
        return False
        
    def generate_content(self, content_type, params):
        """Generate content based on type and parameters"""
        if content_type not in self.content_templates:
            return None
            
        template = self.content_templates[content_type]
        prompt = template.format(**params)
        
        print(f"\nGenerating {content_type}...")
        print(f"Prompt: {prompt[:100]}...")
        
        try:
            content = generate(prompt)
            return content
        except Exception as e:
            print(f"Error generating content: {e}")
            return None
            
    def compare_providers(self, prompt):
        """Compare output from different providers"""
        results = {}
        
        for provider in self.providers.keys():
            print(f"\nTesting {provider}...")
            if self.setup_provider(provider, self.providers[provider]["models"][0]):
                try:
                    results[provider] = generate(prompt)
                    print(f"✅ {provider} response received")
                except Exception as e:
                    results[provider] = f"Error: {e}"
                    
        return results
        
    def save_content(self, content, filename=None):
        """Save generated content to file"""
        if not filename:
            filename = f"content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Content saved to {filename}")
        
    def interactive_generator(self):
        """Interactive content generation session"""
        print("\n🌟 Welcome to Multi-Provider Content Generator!")
        print("=" * 50)
        
        while True:
            print("\nContent Types:")
            for i, ctype in enumerate(self.content_templates.keys(), 1):
                print(f"{i}. {ctype.capitalize()}")
            print(f"{len(self.content_templates)+1}. Compare providers")
            print(f"{len(self.content_templates)+2}. Exit")
            
            choice = input("\nSelect content type (1-{}): ".format(len(self.content_templates)+2))
            
            if choice == str(len(self.content_templates)+2):
                print("Goodbye!")
                break
                
            if choice == str(len(self.content_templates)+1):
                # Compare providers
                prompt = input("Enter a test prompt: ")
                results = self.compare_providers(prompt)
                print("\n=== Comparison Results ===")
                for provider, response in results.items():
                    print(f"\n--- {provider} ---")
                    print(response[:200] + "..." if len(response) > 200 else response)
                continue
                
            try:
                content_type = list(self.content_templates.keys())[int(choice)-1]
                
                # Get parameters based on content type
                params = {}
                if content_type == "blog":
                    params["topic"] = input("Enter blog topic: ")
                    params["tone"] = input("Enter tone (professional/casual/persuasive): ")
                    params["length"] = input("Enter desired length (words): ")
                    
                elif content_type == "social":
                    params["topic"] = input("Enter post topic: ")
                    params["platform"] = input("Enter platform (Twitter/LinkedIn/Facebook): ")
                    params["tone"] = input("Enter tone (funny/inspirational/professional): ")
                    
                elif content_type == "code":
                    params["language"] = input("Enter programming language: ")
                    params["task"] = input("Enter task description: ")
                    
                elif content_type == "email":
                    params["topic"] = input("Enter email subject/topic: ")
                    params["tone"] = input("Enter tone (formal/friendly/urgent): ")
                    
                elif content_type == "poem":
                    params["style"] = input("Enter poem style (haiku/sonnet/free verse): ")
                    params["topic"] = input("Enter poem topic: ")
                    
                elif content_type == "story":
                    params["genre"] = input("Enter story genre: ")
                    params["topic"] = input("Enter story topic: ")
                    params["length"] = input("Enter desired length (words): ")
                
                # Select provider
                print("\nSelect Provider:")
                for i, provider in enumerate(self.providers.keys(), 1):
                    print(f"{i}. {provider}")
                
                provider_choice = int(input("Choose provider: ")) - 1
                provider = list(self.providers.keys())[provider_choice]
                
                # Setup and generate
                if self.setup_provider(provider):
                    content = self.generate_content(content_type, params)
                    
                    if content:
                        print("\n" + "="*50)
                        print("GENERATED CONTENT:")
                        print("="*50)
                        print(content)
                        
                        # Save option
                        save = input("\nSave this content? (y/n): ")
                        if save.lower() == 'y':
                            self.save_content(content)
                            
            except (ValueError, IndexError, KeyError) as e:
                print(f"Invalid input: {e}")

def main():
    generator = ContentGenerator()
    generator.interactive_generator()

if __name__ == "__main__":
    main()