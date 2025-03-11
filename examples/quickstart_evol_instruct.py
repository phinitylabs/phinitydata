"""
Quick start example demonstrating evolution instruction functionality without documents.
This example shows how to:
1. Initialize the SFT generator
2. Configure evolution strategies
3. Generate evolved instructions and responses
"""

import os
from phinitydata.testset.sft_generator import SFTGenerator

# Set OpenAI API key if not in environment
if "OPENAI_API_KEY" not in os.environ:
    api_key = input("Enter your OpenAI API key: ")
    os.environ["OPENAI_API_KEY"] = api_key

def run_quickstart():
    # Initialize the generator
    generator = SFTGenerator()

    # Define some seed instructions
    seed_instructions = [
        "What is machine learning?",
        "Explain how neural networks work.",
        "What is the difference between supervised and unsupervised learning?"
    ]

    # Configure the evolution process
    evolution_config = {
        "steps": 2,  # Number of evolution steps
        "strategies": ["deepening", "concretizing", "reasoning"],
        "weights": [0.4, 0.3, 0.3]  # Probability weights for strategy selection
    }

    # Add a custom evolution strategy (optional)
    generator.add_evolution_strategy(
        name="practical_application",
        description="Evolves the instruction to focus on practical applications",
        prompt_template="""
        Rewrite the given prompt to focus on real-world applications.
        The evolved prompt should:
        1. Include specific use cases or examples
        2. Ask about practical implementation
        3. Consider real-world constraints or limitations
        4. Maintain the core learning objective
        
        ORIGINAL PROMPT: {original_prompt}
        
        RECENT INSTRUCTIONS (avoid repeating these):
        {recent_history}
        
        Create a practical application-focused version:
        """
    )

    # Update config to include custom strategy
    evolution_config["strategies"].append("practical_application")
    evolution_config["weights"] = [0.3, 0.2, 0.2, 0.3]

    try:
        # Generate evolved instructions and responses
        results = generator.generate(
            seed_instructions=seed_instructions,
            documents=None,  # No documents for this example
            num_samples=2,  # Generate 2 examples per seed
            evolution_config=evolution_config,
            verbose=True
        )

        # Print results
        print("\nEvolution Results:")
        for i, sample in enumerate(results["samples"], 1):
            print(f"\nExample {i}:")
            print(f"Original: {sample['metadata']['seed']}")
            print("\nEvolution Steps:")
            for step in sample["metadata"]["evolution_chain"]:
                print(f"\nStrategy: {step['strategy']}")
                print(f"Before: {step['before']}")
                print(f"After:  {step['after']}")
            
            print("\nFinal Result:")
            print(f"Instruction: {sample['instruction']}")
            print(f"Response: {sample['response'][:200]}...")
            print("-" * 80)

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    run_quickstart() 