"""
Quickstart example for evolved instruction generation.
Shows basic usage of SFTGenerator without document grounding.
"""

from phinitydata.testset.sft_generator import SFTGenerator
import os

def quickstart_example():
    # Create output directory
    os.makedirs("examples/generated_data", exist_ok=True)
    
    # Initialize generator
    generator = SFTGenerator()
    
    # Define seed instructions - just 2 basic ML questions
    seeds = [
        "What is machine learning?",
        "How do neural networks work?"
    ]
    
    # Generate evolved instructions - more samples to show evolution
    results = generator.generate(
        seed_instructions=seeds,
        target_samples=10,  # Generate more evolved versions
        domain_context="machine learning and neural networks",
        evolution_config={
            "max_generations": 3,
            "strategies": ["deepening", "reasoning", "comparative"],
            "weights": [0.4, 0.3, 0.3]
        },
        verbose=True,
        export_format="jsonl",
        export_path="examples/generated_data/quickstart_instructions.jsonl"
    )
    
    # Print results
    print("\nGenerated Instructions:")
    for i, sample in enumerate(results['samples'], 1):
        print(f"\n{i}. {sample['instruction']}")
        print(f"Strategy: {sample['strategy']}")
        print(f"Parent: {sample['parent']}")
        print("-" * 80)

if __name__ == "__main__":
    quickstart_example() 