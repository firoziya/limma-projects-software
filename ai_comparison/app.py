# ai_comparison.py
from limma.llm import config, generate
import time
import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

class AIComparisonTool:
    def __init__(self):
        self.providers = {
            "openai": {
                "name": "OpenAI",
                "models": ["gpt-5", "gpt-3.5-turbo"],
                "api_key": None,
                "enabled": False
            },
            "gemini": {
                "name": "Google Gemini",
                "models": ["gemini-2.5-flash", "gemini-3-flash-preview"],
                "api_key": None,
                "enabled": False
            },
            "groq": {
                "name": "Groq",
                "models": ["moonshotai/kimi-k2-instruct-0905", "llama-3.3-70b-versatile"],
                "api_key": None,
                "enabled": False
            },
            "mistral": {
                "name": "Mistral AI",
                "models": ["mistral-large-latest", "mistral-medium"],
                "api_key": None,
                "enabled": False
            }
        }
        
        self.results = []
        self.metrics = defaultdict(list)
        
    def setup_providers(self):
        """Interactive provider setup"""
        print("\n=== AI Provider Setup ===")
        print("Configure the providers you want to compare:")
        
        for provider_id, provider in self.providers.items():
            print(f"\n{provider['name']}:")
            enable = input(f"Enable {provider['name']}? (y/n): ").lower()
            
            if enable == 'y':
                api_key = input(f"Enter {provider['name']} API key: ")
                provider['api_key'] = api_key
                provider['enabled'] = True
                
                print("Available models:")
                for i, model in enumerate(provider['models'], 1):
                    print(f"  {i}. {model}")
                model_choice = int(input("Select model (1-2): ")) - 1
                provider['selected_model'] = provider['models'][model_choice]
                
    def test_provider(self, provider_id, prompt):
        """Test a single provider with a prompt"""
        provider = self.providers[provider_id]
        
        if not provider['enabled']:
            return None
            
        try:
            # Configure provider
            config(
                provider=provider_id,
                api_key=provider['api_key'],
                model=provider['selected_model']
            )
            
            # Time the response
            start_time = time.time()
            response = generate(prompt)
            end_time = time.time()
            
            response_time = end_time - start_time
            word_count = len(response.split())
            char_count = len(response)
            
            result = {
                "provider": provider['name'],
                "model": provider['selected_model'],
                "response": response,
                "response_time": response_time,
                "word_count": word_count,
                "char_count": char_count,
                "timestamp": datetime.now().isoformat()
            }
            
            self.results.append(result)
            
            # Update metrics
            self.metrics[provider['name']].append(response_time)
            
            return result
            
        except Exception as e:
            print(f"Error testing {provider['name']}: {e}")
            return None
            
    def compare_all(self, prompt):
        """Compare all enabled providers"""
        print(f"\n📊 Comparing AI Providers for prompt: '{prompt}'")
        print("=" * 60)
        
        results = []
        for provider_id in self.providers:
            if self.providers[provider_id]['enabled']:
                print(f"\nTesting {self.providers[provider_id]['name']}...")
                result = self.test_provider(provider_id, prompt)
                if result:
                    results.append(result)
                    print(f"  ✅ Response time: {result['response_time']:.2f}s")
                    print(f"  📝 Words: {result['word_count']}")
                    
        return results
        
    def display_comparison(self, results):
        """Display comparison results"""
        if not results:
            print("No results to display")
            return
            
        print("\n" + "="*70)
        print("COMPARISON RESULTS")
        print("="*70)
        
        # Sort by response time
        sorted_results = sorted(results, key=lambda x: x['response_time'])
        
        for i, result in enumerate(sorted_results, 1):
            print(f"\n{i}. {result['provider']} ({result['model']})")
            print(f"   ⏱️  Response time: {result['response_time']:.2f}s")
            print(f"   📊 Words: {result['word_count']} | Characters: {result['char_count']}")
            print(f"   💬 Response preview: {result['response'][:200]}...")
            
        # Winner
        fastest = sorted_results[0]
        most_words = max(results, key=lambda x: x['word_count'])
        
        print("\n" + "🏆" * 20)
        print(f"Fastest: {fastest['provider']} ({fastest['response_time']:.2f}s)")
        print(f"Most verbose: {most_words['provider']} ({most_words['word_count']} words)")
        print("🏆" * 20)
        
    def analyze_quality(self, results, criteria):
        """Analyze response quality based on criteria"""
        print(f"\n📈 Quality Analysis based on: {criteria}")
        
        analysis_results = []
        for result in results:
            # Use AI to evaluate quality
            eval_prompt = f"""Evaluate this response based on: {criteria}
            Rate it 1-10 and explain briefly.
            
            Response: {result['response']}
            
            Format: Score: [1-10], Brief explanation:"""
            
            try:
                config(
                    provider="gemini",  # Use a free provider for evaluation
                    api_key=self.providers['gemini']['api_key'],
                    model="gemini-2.5-flash"
                )
                evaluation = generate(eval_prompt)
                
                analysis_results.append({
                    "provider": result['provider'],
                    "evaluation": evaluation
                })
            except:
                analysis_results.append({
                    "provider": result['provider'],
                    "evaluation": "Evaluation failed"
                })
                
        for ar in analysis_results:
            print(f"\n{ar['provider']}: {ar['evaluation']}")
            
    def export_results(self, results, filename=None):
        """Export results to file"""
        if not filename:
            filename = f"comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
        export_data = {
            "timestamp": datetime.now().isoformat(),
            "results": results
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
            
        print(f"\n💾 Results exported to {filename}")
        
    def plot_comparison(self, results):
        """Create visual comparison chart"""
        providers = [r['provider'] for r in results]
        times = [r['response_time'] for r in results]
        words = [r['word_count'] for r in results]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Response time chart
        ax1.bar(providers, times, color='skyblue')
        ax1.set_title('Response Time by Provider')
        ax1.set_xlabel('Provider')
        ax1.set_ylabel('Time (seconds)')
        ax1.tick_params(axis='x', rotation=45)
        
        # Word count chart
        ax2.bar(providers, words, color='lightgreen')
        ax2.set_title('Response Length by Provider')
        ax2.set_xlabel('Provider')
        ax2.set_ylabel('Word Count')
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        # Save chart
        chart_file = f"comparison_chart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(chart_file)
        print(f"\n📊 Chart saved to {chart_file}")
        plt.show()
        
    def batch_comparison(self, prompts_file):
        """Compare multiple prompts"""
        with open(prompts_file, 'r') as f:
            prompts = [line.strip() for line in f if line.strip()]
            
        all_results = []
        
        for i, prompt in enumerate(prompts, 1):
            print(f"\n[{i}/{len(prompts)}] Testing prompt: {prompt}")
            results = self.compare_all(prompt)
            all_results.append({
                "prompt": prompt,
                "results": results
            })
            
        # Summary statistics
        print("\n" + "="*70)
        print("BATCH COMPARISON SUMMARY")
        print("="*70)
        
        provider_stats = defaultdict(lambda: {"total_time": 0, "count": 0, "total_words": 0})
        
        for test in all_results:
            for result in test['results']:
                provider = result['provider']
                provider_stats[provider]["total_time"] += result['response_time']
                provider_stats[provider]["count"] += 1
                provider_stats[provider]["total_words"] += result['word_count']
                
        for provider, stats in provider_stats.items():
            avg_time = stats['total_time'] / stats['count']
            avg_words = stats['total_words'] / stats['count']
            print(f"\n{provider}:")
            print(f"  Average response time: {avg_time:.2f}s")
            print(f"  Average words: {avg_words:.1f}")
            
        return all_results
        
    def interactive_comparison(self):
        """Interactive comparison session"""
        print("\n🤖 Multi-Model AI Comparison Tool")
        print("=" * 40)
        
        # Setup providers first
        self.setup_providers()
        
        while True:
            print("\n" + "="*40)
            print("Comparison Options:")
            print("1. Single prompt comparison")
            print("2. Batch comparison from file")
            print("3. View history")
            print("4. Performance trends")
            print("5. Exit")
            
            choice = input("\nSelect option (1-5): ")
            
            if choice == "1":
                prompt = input("\nEnter your prompt: ")
                results = self.compare_all(prompt)
                if results:
                    self.display_comparison(results)
                    
                    # Additional options
                    action = input("\nAnalyze quality? (y/n): ")
                    if action.lower() == 'y':
                        criteria = input("Quality criteria (e.g., 'accuracy, clarity, creativity'): ")
                        self.analyze_quality(results, criteria)
                        
                    action = input("Export results? (y/n): ")
                    if action.lower() == 'y':
                        self.export_results(results)
                        
                    action = input("Create chart? (y/n): ")
                    if action.lower() == 'y':
                        self.plot_comparison(results)
                        
            elif choice == "2":
                filename = input("Enter prompts file name: ")
                self.batch_comparison(filename)
                
            elif choice == "3":
                if self.results:
                    print("\n=== Comparison History ===")
                    for i, result in enumerate(self.results[-10:], 1):
                        print(f"{i}. {result['provider']} - {result['response_time']:.2f}s - {result['word_count']} words")
                else:
                    print("No history yet")
                    
            elif choice == "4":
                if self.metrics:
                    print("\n=== Performance Trends ===")
                    for provider, times in self.metrics.items():
                        avg_time = sum(times) / len(times)
                        print(f"{provider}: avg {avg_time:.2f}s over {len(times)} tests")
                        
            elif choice == "5":
                print("Goodbye!")
                break

def main():
    tool = AIComparisonTool()
    tool.interactive_comparison()

if __name__ == "__main__":
    main()