# docs.md
## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Module Explanation](#module-explanation)
3. [Function Breakdown](#function-breakdown)
4. [Future Improvements](#future-improvements)
5. [Usage Examples](#usage-examples)

## Architecture Overview
The ContentGenerator class is the core component of this project, responsible for content generation, provider setup, and comparison. It utilizes the `limma.llm` library for interacting with various language models.

The following components make up the architecture:

*   **ContentGenerator Class**: This class encapsulates the functionality of content generation, provider setup, and comparison.
*   **Provider Setup**: The class allows for the setup of different providers, including OpenAI, Gemini, Groq, and Mistral.
*   **Content Templates**: Predefined templates for generating different types of content, such as blog posts, social media posts, code, emails, poems, and stories.
*   **Interactive Generator**: An interactive session that guides the user through the content generation process.

## Module Explanation
The `content_generator.py` module contains the ContentGenerator class and its associated functions.

### ContentGenerator Class
This class has the following attributes:

*   `providers`: A dictionary containing the configuration for each provider, including API keys and available models.
*   `content_templates`: A dictionary containing predefined templates for generating different types of content.

The class has the following methods:

*   `__init__`: Initializes the ContentGenerator instance, setting up the providers and content templates.
*   `setup_provider`: Configures a specific provider, including setting the API key and selecting a model.
*   `generate_content`: Generates content based on a given type and parameters.
*   `compare_providers`: Compares the output from different providers for a given prompt.
*   `save_content`: Saves generated content to a file.
*   `interactive_generator`: Starts an interactive content generation session.

### Functions
The following functions are defined in the module:

*   `main`: Creates a ContentGenerator instance and starts an interactive content generation session.

## Function Breakdown
Here's a detailed breakdown of each function in the ContentGenerator class:

### `__init__`
Initializes the ContentGenerator instance, setting up the providers and content templates.

*   **Parameters**: None
*   **Returns**: None

### `setup_provider`
Configures a specific provider, including setting the API key and selecting a model.

*   **Parameters**:
    *   `provider_name`: The name of the provider to configure.
    *   `model`: The model to use for the provider (optional).
*   **Returns**: `True` if the provider is configured successfully, `False` otherwise.

### `generate_content`
Generates content based on a given type and parameters.

*   **Parameters**:
    *   `content_type`: The type of content to generate.
    *   `params`: A dictionary containing the parameters for the content type.
*   **Returns**: The generated content, or `None` if an error occurs.

### `compare_providers`
Compares the output from different providers for a given prompt.

*   **Parameters**:
    *   `prompt`: The prompt to use for comparison.
*   **Returns**: A dictionary containing the output from each provider.

### `save_content`
Saves generated content to a file.

*   **Parameters**:
    *   `content`: The content to save.
    *   `filename`: The filename to use for saving (optional).
*   **Returns**: None

### `interactive_generator`
Starts an interactive content generation session.

*   **Parameters**: None
*   **Returns**: None

## Future Improvements
Here are some potential improvements for the project:

*   **Add more providers**: Integrate additional language model providers to increase the range of options for users.
*   **Improve error handling**: Enhance error handling to provide more informative error messages and to handle a wider range of potential errors.
*   **Implement content evaluation**: Develop a system to evaluate the quality of generated content, providing feedback to users and helping them refine their prompts.
*   **Integrate with other tools**: Explore integrating the content generator with other tools and platforms, such as content management systems or social media schedulers.

## Usage Examples
Here are some examples of using the ContentGenerator class:

### Generating a Blog Post
```python
generator = ContentGenerator()
params = {
    "topic": "Artificial Intelligence",
    "tone": "professional",
    "length": "500"
}
content = generator.generate_content("blog", params)
print(content)
```

### Comparing Providers
```python
generator = ContentGenerator()
prompt = "Write a short story about a character who discovers a hidden world."
results = generator.compare_providers(prompt)
for provider, response in results.items():
    print(f"\n--- {provider} ---")
    print(response[:200] + "..." if len(response) > 200 else response)
```

### Saving Generated Content
```python
generator = ContentGenerator()
params = {
    "topic": "Machine Learning",
    "tone": "casual",
    "length": "300"
}
content = generator.generate_content("blog", params)
generator.save_content(content, "example_blog_post.txt")
```