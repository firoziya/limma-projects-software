# docs.md
## Introduction
The AI Comparison Tool is a Python project designed to compare the performance of different AI providers. The tool allows users to interactively compare the response times, word counts, and quality of responses from various AI providers.

## Architecture Overview
The AI Comparison Tool consists of a single class, `AIComparisonTool`, which encapsulates all the functionality of the tool. The class has several methods that enable users to:

* Set up AI providers and their corresponding API keys
* Test individual providers with a given prompt
* Compare the performance of all enabled providers for a given prompt
* Analyze the quality of responses based on user-defined criteria
* Export comparison results to a file
* Create visual comparison charts
* Perform batch comparisons using a file containing multiple prompts

## Module Explanation
The project uses the following external modules:

* `limma.llm`: provides functionality for interacting with AI providers
* `time`: used for timing the response times of AI providers
* `json`: used for exporting comparison results to a file
* `datetime`: used for timestamping comparison results
* `matplotlib`: used for creating visual comparison charts

## Function Breakdown
The `AIComparisonTool` class has the following methods:

* `__init__`: initializes the tool with a dictionary of AI providers and their corresponding settings
* `setup_providers`: interactively sets up AI providers and their API keys
* `test_provider`: tests a single AI provider with a given prompt and returns the response time, word count, and response
* `compare_all`: compares the performance of all enabled AI providers for a given prompt
* `display_comparison`: displays the comparison results, including response times, word counts, and response previews
* `analyze_quality`: analyzes the quality of responses based on user-defined criteria
* `export_results`: exports comparison results to a file
* `plot_comparison`: creates a visual comparison chart
* `batch_comparison`: performs batch comparisons using a file containing multiple prompts
* `interactive_comparison`: provides an interactive interface for users to compare AI providers

## Future Improvements
Some potential future improvements to the AI Comparison Tool include:

* Adding support for more AI providers
* Implementing more advanced quality analysis criteria
* Enhancing the visual comparison chart to include more metrics
* Adding support for comparing AI providers based on specific tasks or use cases
* Integrating the tool with other AI-related projects or frameworks

## Usage Examples
To use the AI Comparison Tool, simply run the `main.py` file and follow the interactive prompts. Here are some examples of how to use the tool:

* Compare the performance of all enabled AI providers for a given prompt:
```python
tool = AIComparisonTool()
tool.setup_providers()
prompt = input("Enter your prompt: ")
results = tool.compare_all(prompt)
tool.display_comparison(results)
```
* Analyze the quality of responses based on user-defined criteria:
```python
tool = AIComparisonTool()
tool.setup_providers()
prompt = input("Enter your prompt: ")
results = tool.compare_all(prompt)
criteria = input("Enter quality criteria (e.g., 'accuracy, clarity, creativity'): ")
tool.analyze_quality(results, criteria)
```
* Export comparison results to a file:
```python
tool = AIComparisonTool()
tool.setup_providers()
prompt = input("Enter your prompt: ")
results = tool.compare_all(prompt)
tool.export_results(results)
```
* Create a visual comparison chart:
```python
tool = AIComparisonTool()
tool.setup_providers()
prompt = input("Enter your prompt: ")
results = tool.compare_all(prompt)
tool.plot_comparison(results)
```