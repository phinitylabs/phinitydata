import os
from phinitydata.testset.sft_generator import SFTGenerator

def test_document_grounding():
    """Test document-grounded instruction generation"""
    # Create output directory
    os.makedirs("generated_data", exist_ok=True)
    
    # Initialize generator
    api_key = get_api_key()
    generator = SFTGenerator(api_key=api_key)
    
    # ... (rest of setup code remains the same)
    
    # Run tests sequentially with clear separation
    print("\n" + "="*50)
    print("1. Basic Document Grounding Test")
    print("="*50)
    results = generator.generate(
        seed_instructions=seed_instructions,
        documents=documents,
        target_samples=5,
        domain_context="transformer architecture and attention mechanisms - RULE: ONLY USE THE DOCUMENTS TO GROUND THE INSTRUCTIONS",
        evolution_config={
            "max_generations": 3,
            "strategies": ["deepening", "concretizing"],
            "weights": [0.5, 0.5]
        },
        verbose=True,
        export_format="jsonl",
        export_path="generated_data/grounded_transformer_instructions.jsonl"
    )
    
    print("\n" + "="*50)
    print("2. Mixed Document Types Test")
    print("="*50)
    # ... (mixed docs test)
    
    print("\n" + "="*50)
    print("3. Flexible Grounding Test")
    print("="*50)
    # ... (flexible test)
    
    print("\n" + "="*50)
    print("4. Strict Grounding Test")
    print("="*50)
    # ... (strict test) 