"""
Test script demonstrating document-grounded instruction generation
Shows how to use documents to ground and verify generated instructions
"""

from phinitydata.testset.sft_generator import SFTGenerator
import os

def get_api_key() -> str:
    """Get OpenAI API key from environment or user input"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("Enter your OpenAI API key: ").strip()
        if not api_key:
            raise ValueError("OpenAI API key is required")
    return api_key

def test_document_grounding():
    """
    Test document-grounded instruction generation with example documents
    """
    # Create output directory
    os.makedirs("generated_data", exist_ok=True)
    
    # Initialize generator with API key
    api_key = get_api_key()
    generator = SFTGenerator(api_key=api_key)

    # Example documents about a specific ML topic
    documents = [
        """
        Transformers are a type of neural network architecture that has revolutionized NLP.
        The key innovation is the self-attention mechanism, which allows the model to weigh
        the importance of different words in a sequence when processing each word.
        The architecture consists of an encoder and decoder, though some applications
        use only the encoder (BERT) or only the decoder (GPT).
        """,
        """
        The self-attention mechanism works by computing three matrices: Query (Q),
        Key (K), and Value (V) for each input token. The attention scores are
        computed by taking the dot product of Q and K, then applying softmax to
        get weights. These weights are used to create a weighted sum of V,
        producing the final attention output.
        """,
        """
        Training transformers involves several key techniques:
        1. Masked Language Modeling (MLM) - randomly mask tokens and train the model to predict them
        2. Causal Language Modeling (CLM) - predict the next token given previous tokens
        3. Positional Encoding - add position information since the model has no inherent sequence understanding
        The training typically requires large amounts of text data and computational resources.
        """
    ]

    # Seed instructions focused on the document content
    seed_instructions = [
        "What are transformers in machine learning?",
        "Explain how self-attention works",
        "What techniques are used to train transformers?"
    ]

    print("\n=== Document-Grounded Instruction Generation ===")
    print(f"Using {len(documents)} documents for grounding")
    print(f"Starting with {len(seed_instructions)} seed instructions")

    # Generate grounded instructions with simpler evolution config
    results = generator.generate(
        seed_instructions=seed_instructions,
        documents=documents,
        target_samples=5,
        domain_context="transformer architecture and attention mechanisms - RULE: ONLY USE THE DOCUMENTS TO GROUND THE INSTRUCTIONS",
        evolution_config={
            "max_generations": 3,  # Reduced from 10
            "steps": 1,  # Only one evolution step per generation
            "strategies": ["deepening", "concretizing"],  # Removed more complex strategies
            "weights": [0.5, 0.5]
        },
        verbose=True,
        export_format="jsonl",
        export_path="generated_data/grounded_transformer_instructions.jsonl"
    )

    # Print results
    print("\n=== Generated Instruction-Response Pairs ===")
    for i, sample in enumerate(results['samples'], 1):
        print(f"\nSample {i}:")
        print(f"Instruction: {sample['instruction']}")
        if 'response' in sample:
            print(f"Response: {sample['response'][:200]}...")  # First 200 chars
        if 'metadata' in sample and 'evolution_chain' in sample['metadata']:
            last_evolution = sample['metadata']['evolution_chain'][-1]
            print(f"Generation: {last_evolution['step']}")
            print(f"Strategy: {last_evolution['strategy']}")
        print("-" * 80)

    # Print metrics
    print("\n=== Generation Metrics ===")
    for metric, value in results['metrics'].items():
        print(f"{metric}: {value}")

    # Test with different document types
    research_paper = """
    Attention Is All You Need (Vaswani et al., 2017) introduced the transformer
    architecture. The model achieves state-of-the-art results on machine translation
    tasks while being more parallelizable and requiring less training time than
    previous architectures based on recurrent or convolutional neural networks.
    """

    technical_docs = """
    To implement a transformer, follow these steps:
    1. Create embedding layers for tokens and positions
    2. Build the encoder with self-attention and feed-forward layers
    3. Add layer normalization and residual connections
    4. Implement multi-head attention by running attention multiple times in parallel
    5. Create the decoder with masked self-attention to prevent looking ahead
    """

    mixed_docs = [research_paper, technical_docs]

    print("\n=== Testing with Different Document Types ===")
    mixed_results = generator.generate(
        seed_instructions=["How do transformers process input sequences?"],
        documents=mixed_docs,
        target_samples=3,
        domain_context="transformer implementation details",
        evolution_config={
            "max_generations": 2,
            "steps": 1,
            "strategies": ["deepening"],
            "weights": [1.0]
        },
        verbose=True,
        export_path="generated_data/mixed_transformer_instructions.jsonl"
    )

    print(f"\nGenerated {len(mixed_results['samples'])} instruction-response pairs")
    print("Results exported to mixed_transformer_instructions.jsonl")

    # Test with flexible document grounding (default behavior)
    print("\n=== Testing with Flexible Document Grounding ===")
    flexible_results = generator.generate(
        seed_instructions=[
            "How might transformer architectures evolve in the future?",
            "What are the ethical implications of large language models?",
            "Compare transformers with traditional neural networks"
        ],
        documents=documents,  # Same documents as context
        target_samples=3,
        domain_context="transformer architecture and future implications",
        evolution_config={
            "max_generations": 3,
            "strategies": ["reasoning", "comparative", "deepening"],
            "weights": [0.4, 0.4, 0.2]
        },
        verbose=True,
        export_path="generated_data/flexible_transformer_instructions.jsonl"
    )

    # Test with strict document grounding (opt-in)
    print("\n=== Testing with Strict Document Grounding ===")
    strict_results = generator.generate(
        seed_instructions=seed_instructions,
        documents=documents,
        target_samples=3,
        domain_context="transformer architecture and attention mechanisms",
        evolution_config={
            "max_generations": 3,
            "steps": 1,
            "strategies": ["deepening", "concretizing"],  # More focused strategies for strict mode
            "weights": [0.5, 0.5]
        },
        strict_grounding=True,  # Explicitly enable strict mode
        verbose=True,
        export_path="generated_data/strict_transformer_instructions.jsonl"
    )

if __name__ == "__main__":
    test_document_grounding() 