# Phinity
Phinity is a synthetic data generation SDK designed to create high-quality, verifiable datasets for LLM development and evaluation.

One of the most difficult aspects of synthetic data generation at scale is diversity. Instruction generation methods like WizardLM Evol-Instruct have been developed to enable diverse instruction generation at scale - to do this, they continuously create new prompts from a seed set of prompts that the user provides by "evolving" them in the domain. Think of a never-ending family tree: prompts give birth to new prompts with various added mutations through generations. Now you have 1000000s of new family members from a starting set of a couple of seed family members. Evol-Instruct is used by frontier AI labs to generate code SFT (supervised fine-tuning) datasets for LLMs. 

We extend this approach to support custom domain-specific dataset generation, ensuring high-quality data that aligns with your rules and context.

# 🎯 Key Features
**Instruction Evolution Framework**
Phinity enables structured prompt evolution with multiple built-in strategies:

- Deepening – Makes instructions more detailed and specific.
- Concretizing – Adds concrete examples or scenarios.
- Reasoning – Enhances reasoning or step-by-step explanations.
- Comparative – Transforms prompts to include comparative elements.

Users can add custom evolution strategies, define domain-specific constraints, and integrate supporting documents for more controlled instruction generation.

**Document/Knowledge Base Support** 
- Instruction Verification and Repair: Phinity includes robust document verification to ensure evolved instructions remain answerable and relevant to provided sources. There is an instruction repair pipeline that detects and corrects instructions that drift from document context (`_repair_instruction` and `_simplify_instruction`) which supports both strict and partial answerability checks and integration with vector databases such as ChromaDB.

**RAG Benchmark Generation**
Phinity also supports creating multi-hop RAG benchmarks by constructing knowledge graphs from documents and generating synthetic QA pairs. 


# Phinity

Phinity is a synthetic data generation SDK designed to create high-quality, verifiable datasets for LLM development and evaluation.

One of the most difficult aspects of synthetic data generation at scale is diversity. Instruction generation methods like WizardLM Evol-Instruct have been developed to enable diverse instruction generation at scale - to do this, they continuously create new prompts from a seed set of prompts that the user provides by "evolving" them in the domain. Think of a never-ending family tree: prompts give birth to new prompts with various added mutations through generations. Now you have 1000000s of new family members from a starting set of a couple of seed family members. Evol-Instruct is used by frontier AI labs to generate code SFT (supervised fine-tuning) datasets for LLMs. 

We extend this approach to support custom domain-specific dataset generation, ensuring high-quality data that aligns with your rules and context.

## 🎯 Key Features

### Instruction Evolution Framework
Phinity enables structured prompt evolution with multiple built-in strategies:
- **Deepening** – Makes instructions more detailed and specific.
- **Concretizing** – Adds concrete examples or scenarios.
- **Reasoning** – Enhances reasoning or step-by-step explanations.
- **Comparative** – Transforms prompts to include comparative elements.

Users can add custom evolution strategies, define domain-specific constraints, and integrate supporting documents for more controlled instruction generation.

### Document/Knowledge Base Support
- **Instruction Verification and Repair**: Phinity includes robust document verification to ensure evolved instructions remain answerable and relevant to provided sources. There is an instruction repair pipeline that detects and corrects instructions that drift from document context (`_repair_instruction` and `_simplify_instruction`) which supports both strict and partial answerability checks and integration with vector databases such as ChromaDB.

### RAG Benchmark Generation
Phinity also supports creating multi-hop RAG benchmarks by constructing knowledge graphs from documents and generating synthetic QA pairs.

## Quick Start

### Installation

```bash
pip install phinitydata
```

### Basic Usage (Step-by-Step)

Follow these steps to generate evolved instructions with Phinity:

#### 1. Import the necessary modules

```python
from phinitydata.testset.sft_generator import SFTGenerator
import os
```

#### 2. Set up your OpenAI API key

```python
# Option 1: Set environment variable
# export OPENAI_API_KEY='your-api-key-here'
    
# Option 2: Pass directly to generator
api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"
```

#### 3. Initialize the generator

```python
generator = SFTGenerator(
    api_key=api_key,
    llm_model="gpt-4o-mini",  # or your preferred model
    temperature=0.7
)
```

#### 4. Define your seed instructions

```python
seed_instructions = [
    "What is machine learning?",
    "Explain how neural networks work"
]
```

#### 5. Generate instruction-response pairs

```python
results = generator.generate_evolved_instructions(
    seed_instructions=seed_instructions,
    target_samples=5,  # Number of samples to generate
    max_generations=10,  # Maximum evolution generations
    domain_context="artificial intelligence and machine learning",
    generate_responses=True,  # Set False to generate instructions only
    export_format="jsonl",
    export_path="evolved_instructions.jsonl"
)
```

#### 6. Access the generated data

```python
print("\n=== Generated Samples ===")
for i, sample in enumerate(results['samples'], 1):
    print(f"\nSample {i}:")
    print(f"Instruction: {sample['instruction']}")
    if 'response' in sample:
        print(f"Response: {sample['response'][:100]}...")  # Show first 100 chars
    print(f"Generation: {sample['metadata']['generation']}")
    print(f"Strategy: {sample['metadata']['strategy']}")
```

#### 7. Print metrics

```python
print("\n=== Generation Metrics ===")
print(f"Total generations: {results['metrics']['generations']}")
print(f"Time taken: {results['metrics']['total_time']:.2f} seconds")
print(f"Samples generated: {results['metrics']['samples_generated']}")
print(f"Samples verified: {results['metrics']['samples_verified']}")
```

#### 8. Document-grounded generation (optional)

```python
documents = [
    "Machine learning is a subset of artificial intelligence...",
    "Neural networks are composed of layers of interconnected nodes..."
]

grounded_results = generator.generate_evolved_instructions(
    seed_instructions=seed_instructions,
    target_samples=5,
    max_generations=10,
    docs=documents,  # Provide documents for grounding
    domain_context="artificial intelligence",
    export_path="grounded_instructions.jsonl"
)
```


## Documentation and Roadmap

For comprehensive documentation, visit:
[https://phinity.gitbook.io/phinity/use-cases/in-domain-sft](https://phinity.gitbook.io/phinity/use-cases/in-domain-sft)



  
