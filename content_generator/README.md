# Multi-Provider Content Generator
=====================================

## Description
The Multi-Provider Content Generator is a Python application that utilizes multiple AI providers to generate high-quality content. It supports various content types, including blog posts, social media posts, code, emails, poems, and stories. The application provides an interactive interface for users to select content types, parameters, and providers.

## Installation
To install the Multi-Provider Content Generator, follow these steps:

1. Clone the repository: `git clone https://github.com/firoziya/multi-provider-content-generator.git`
2. Install the required libraries: `pip install -r requirements.txt`
3. Set environment variables for API keys:
   - `OPENAI_API_KEY`
   - `GEMINI_API_KEY`
   - `GROQ_API_KEY`
   - `MISTRAL_API_KEY`

## Usage
To use the Multi-Provider Content Generator, run the application:

```bash
python content_generator.py
```

This will launch an interactive session where you can select content types, parameters, and providers.

## Example
Here's an example of generating a blog post using the OpenAI provider:

1. Select content type: `1. Blog`
2. Enter blog topic: `AI in Content Generation`
3. Enter tone: `professional`
4. Enter desired length: `500`
5. Select provider: `1. OpenAI`
6. The application will generate a blog post based on your inputs.

## License
The Multi-Provider Content Generator is licensed under the MIT License.

```markdown
Copyright (c) 2024 firoziya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```