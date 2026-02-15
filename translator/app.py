# translator.py
from limma.llm import config, generate
from limma.voice import VoiceAssistant
import json
import os
from datetime import datetime

class AITranslator:
    def __init__(self):
        self.va = VoiceAssistant(speech_rate=150)
        
        # Configure LLM for translation
        config(
            provider="groq",  # Free tier suitable for translation
            api_key=os.getenv("GROQ_API_KEY", "your-key-here"),
            model="moonshotai/kimi-k2-instruct-0905"
        )
        
        self.languages = {
            "1": "Spanish",
            "2": "French",
            "3": "German",
            "4": "Italian",
            "5": "Portuguese",
            "6": "Russian",
            "7": "Japanese",
            "8": "Chinese",
            "9": "Arabic",
            "10": "Hindi",
            "11": "Dutch",
            "12": "Korean",
            "13": "Turkish",
            "14": "Polish",
            "15": "Vietnamese"
        }
        
        self.history_file = "translation_history.json"
        self.history = self.load_history()
        
    def load_history(self):
        """Load translation history"""
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                return json.load(f)
        return []
        
    def save_history(self):
        """Save translation history"""
        with open(self.history_file, 'w') as f:
            json.dump(self.history[-50:], f, indent=2)  # Keep last 50
            
    def translate(self, text, source_lang, target_lang):
        """Translate text using LLM"""
        prompt = f"""Translate the following {source_lang} text to {target_lang}.
        Only provide the translation, no additional text or explanations.
        
        Text: {text}
        
        Translation:"""
        
        try:
            translation = generate(prompt)
            
            # Save to history
            self.history.append({
                "timestamp": datetime.now().isoformat(),
                "source_lang": source_lang,
                "target_lang": target_lang,
                "original": text,
                "translation": translation
            })
            self.save_history()
            
            return translation.strip()
        except Exception as e:
            return f"Translation error: {e}"
            
    def detect_language(self, text):
        """Detect language of text"""
        prompt = f"""Detect the language of this text. Return only the language name.
        Text: {text}"""
        
        try:
            return generate(prompt).strip()
        except:
            return "Unknown"
            
    def voice_translate(self):
        """Translate spoken text"""
        self.va.speak("What would you like to translate?")
        text = self.va.listen()
        
        if text:
            source_lang = self.detect_language(text)
            print(f"Detected language: {source_lang}")
            
            # Show language options
            print("\nTarget languages:")
            for key, lang in self.languages.items():
                print(f"{key}. {lang}")
                
            choice = input("Select target language (1-15): ")
            if choice in self.languages:
                target_lang = self.languages[choice]
                
                print(f"Translating to {target_lang}...")
                translation = self.translate(text, source_lang, target_lang)
                
                print(f"\nTranslation: {translation}")
                self.va.speak(translation)
                
    def conversation_mode(self):
        """Real-time conversation translation"""
        self.va.speak("Conversation mode activated")
        
        # Choose languages
        print("\nSelect your language:")
        for key, lang in self.languages.items():
            print(f"{key}. {lang}")
        lang1_choice = input("Choose (1-15): ")
        lang1 = self.languages.get(lang1_choice, "English")
        
        print("\nSelect other person's language:")
        lang2_choice = input("Choose (1-15): ")
        lang2 = self.languages.get(lang2_choice, "English")
        
        self.va.speak(f"I'll translate between {lang1} and {lang2}")
        
        while True:
            # Listen in first language
            self.va.speak(f"Speak in {lang1}")
            text1 = self.va.listen(timeout=10)
            
            if text1 and "exit" not in text1.lower():
                print(f"You ({lang1}): {text1}")
                
                # Translate to second language
                translation = self.translate(text1, lang1, lang2)
                print(f"Translated ({lang2}): {translation}")
                self.va.speak(translation)
                
                # Listen for response in second language
                self.va.speak(f"Now speak in {lang2}")
                text2 = self.va.listen(timeout=10)
                
                if text2 and "exit" not in text2.lower():
                    print(f"Them ({lang2}): {text2}")
                    
                    # Translate back
                    back_translation = self.translate(text2, lang2, lang1)
                    print(f"Translated ({lang1}): {back_translation}")
                    self.va.speak(back_translation)
            else:
                break
                
    def batch_translate(self):
        """Translate multiple texts from file"""
        filename = input("Enter filename with texts to translate: ")
        
        try:
            with open(filename, 'r') as f:
                texts = f.readlines()
                
            # Get language settings
            print("\nTarget languages:")
            for key, lang in self.languages.items():
                print(f"{key}. {lang}")
            target_choice = input("Select target language (1-15): ")
            target_lang = self.languages.get(target_choice, "English")
            
            translations = []
            for i, text in enumerate(texts, 1):
                text = text.strip()
                if text:
                    source_lang = self.detect_language(text)
                    print(f"Translating line {i}...")
                    translation = self.translate(text, source_lang, target_lang)
                    translations.append(translation)
                    
            # Save translations
            output_file = f"translations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(output_file, 'w') as f:
                f.write('\n'.join(translations))
                
            print(f"Translations saved to {output_file}")
            
        except Exception as e:
            print(f"Error: {e}")
            
    def show_history(self):
        """Show translation history"""
        if not self.history:
            print("No translation history")
            return
            
        print("\n=== Translation History ===")
        for i, item in enumerate(self.history[-10:], 1):  # Last 10
            print(f"\n{i}. [{item['timestamp']}]")
            print(f"   {item['source_lang']} → {item['target_lang']}")
            print(f"   Original: {item['original'][:50]}...")
            print(f"   Translation: {item['translation'][:50]}...")
            
    def run(self):
        """Main translator interface"""
        print("\n🌐 AI-Powered Language Translator")
        print("=" * 40)
        print("1. Text Translation")
        print("2. Voice Translation")
        print("3. Conversation Mode")
        print("4. Batch Translation")
        print("5. View History")
        print("6. Exit")
        
        while True:
            choice = input("\nSelect option (1-6): ")
            
            if choice == "1":
                text = input("Enter text to translate: ")
                source_lang = self.detect_language(text)
                print(f"Detected language: {source_lang}")
                
                print("\nTarget languages:")
                for key, lang in self.languages.items():
                    print(f"{key}. {lang}")
                target_choice = input("Select target language (1-15): ")
                
                if target_choice in self.languages:
                    target_lang = self.languages[target_choice]
                    translation = self.translate(text, source_lang, target_lang)
                    print(f"\nTranslation: {translation}")
                    
            elif choice == "2":
                self.voice_translate()
                
            elif choice == "3":
                self.conversation_mode()
                
            elif choice == "4":
                self.batch_translate()
                
            elif choice == "5":
                self.show_history()
                
            elif choice == "6":
                print("Goodbye!")
                break

def main():
    translator = AITranslator()
    translator.run()

if __name__ == "__main__":
    main()