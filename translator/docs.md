# docs.md
## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Module Explanation](#module-explanation)
3. [Function Breakdown](#function-breakdown)
4. [Future Improvements](#future-improvements)
5. [Usage Examples](#usage-examples)

## Architecture Overview
The AI-Powered Language Translator is a Python-based project that utilizes the Limma library for large language models (LLMs) and voice assistance. The project consists of a single module, `translator.py`, which contains the `AITranslator` class. This class encapsulates the functionality of the translator, including text translation, voice translation, conversation mode, batch translation, and translation history management.

The project relies on the following external libraries:

* `limma.llm` for large language models
* `limma.voice` for voice assistance
* `json` for data storage and retrieval
* `os` for file system interactions
* `datetime` for timestamp generation

## Module Explanation
The `translator.py` module contains the `AITranslator` class, which is the core component of the project. This class has several key attributes and methods:

* `__init__`: Initializes the translator instance, setting up the voice assistant, LLM configuration, and language options.
* `load_history` and `save_history`: Manage the translation history, loading and saving it to a JSON file.
* `translate`: Translates text using the LLM, saving the translation to the history.
* `detect_language`: Detects the language of a given text.
* `voice_translate`, `conversation_mode`, and `batch_translate`: Implement different translation modes, including voice translation, conversation mode, and batch translation.
* `show_history`: Displays the translation history.
* `run`: The main entry point of the translator, presenting a menu-driven interface for the user to interact with the translator.

## Function Breakdown
The following functions are part of the `AITranslator` class:

### `load_history`
Loads the translation history from a JSON file.
```python
def load_history(self):
    """Load translation history"""
    if os.path.exists(self.history_file):
        with open(self.history_file, 'r') as f:
            return json.load(f)
    return []
```

### `save_history`
Saves the translation history to a JSON file, keeping only the last 50 entries.
```python
def save_history(self):
    """Save translation history"""
    with open(self.history_file, 'w') as f:
        json.dump(self.history[-50:], f, indent=2)  # Keep last 50
```

### `translate`
Translates text using the LLM, saving the translation to the history.
```python
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
```

### `detect_language`
Detects the language of a given text.
```python
def detect_language(self, text):
    """Detect language of text"""
    prompt = f"""Detect the language of this text. Return only the language name.
    Text: {text}"""
    
    try:
        return generate(prompt).strip()
    except:
        return "Unknown"
```

### `voice_translate`
Implements voice translation, allowing the user to speak and translate text in real-time.
```python
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
```

### `conversation_mode`
Implements conversation mode, allowing two users to communicate in different languages.
```python
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
```

### `batch_translate`
Implements batch translation, allowing the user to translate multiple texts from a file.
```python
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
```

### `show_history`
Displays the translation history, showing the last 10 entries.
```python
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
```

### `run`
The main entry point of the translator, presenting a menu-driven interface for the user to interact with the translator.
```python
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
```

## Future Improvements
The following improvements can be made to the project:

* **Improved language detection**: The current language detection model can be improved by using more advanced techniques, such as machine learning algorithms or natural language processing (NLP) techniques.
* **Additional translation modes**: More translation modes can be added, such as translation from images or audio files.
* **Integration with other services**: The translator can be integrated with other services, such as Google Translate or Microsoft Translator, to provide more accurate translations.
* **User interface improvements**: The user interface can be improved by adding more features, such as the ability to save and load translations, or to view the translation history in a more user-friendly format.
* **Error handling**: The project can be improved by adding more error handling, such as handling cases where the user input is invalid or where the translation fails.

## Usage Examples
The following are some examples of how to use the translator:

* **Text translation**: Enter the text to translate, select the target language, and the translator will provide the translation.
* **Voice translation**: Speak the text to translate, and the translator will provide the translation in real-time.
* **Conversation mode**: Select the languages to translate between, and the translator will provide real-time translation for a conversation between two people.
* **Batch translation**: Enter the filename of a file containing texts to translate, select the target language, and the translator will provide the translations.
* **View history**: View the translation history, showing the last 10 translations.