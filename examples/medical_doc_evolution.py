"""
Tutorial showing how to use SFTGenerator with medical documents.
Demonstrates document-grounded instruction generation in the medical domain.
"""

from phinitydata.testset.sft_generator import SFTGenerator
import os

def medical_doc_example():
    # Initialize generator
    generator = SFTGenerator()
    
    # Example medical documents
    medical_docs = [
        """
        Type 2 diabetes is characterized by insulin resistance and relative insulin deficiency.
        Key symptoms include increased thirst (polydipsia), frequent urination (polyuria),
        increased hunger (polyphagia), and unexplained weight loss. The condition is often
        associated with obesity and physical inactivity. Management typically involves
        lifestyle modifications, oral medications, and sometimes insulin therapy.
        """,
        
        """
        The pathophysiology of type 2 diabetes involves multiple organs:
        1. Pancreas: Decreased insulin production from beta cells
        2. Liver: Increased glucose production
        3. Muscle and fat cells: Reduced glucose uptake due to insulin resistance
        This creates a cycle of elevated blood glucose levels and metabolic dysfunction.
        """,
        
        """
        Treatment options for type 2 diabetes include:
        - Metformin: First-line medication that reduces liver glucose production
        - Sulfonylureas: Increase insulin secretion from pancreas
        - GLP-1 receptor agonists: Enhance insulin release and reduce appetite
        - DPP-4 inhibitors: Prolong the action of incretin hormones
        Regular monitoring of blood glucose and HbA1c levels is essential.
        """
    ]
    
    # Seed instructions focused on medical content
    seeds = [
        "What is type 2 diabetes?",
        "How does type 2 diabetes affect different organs?",
        "What are the treatment options for diabetes?"
    ]
    
    print("\n=== Medical Document-Grounded Instruction Generation ===")
    print(f"Using {len(medical_docs)} medical documents")
    print(f"Starting with {len(seeds)} seed instructions")
    
    # Generate with strict document grounding
    results = generator.generate(
        seed_instructions=seeds,
        documents=medical_docs,
        target_samples=5,
        domain_context="medical knowledge about type 2 diabetes - RULE: USE ONLY INFORMATION FROM THE PROVIDED DOCUMENTS",
        evolution_config={
            "max_generations": 3,
            "strategies": ["deepening", "concretizing"],
            "weights": [0.5, 0.5]
        },
        strict_grounding=True,
        verbose=True,
        export_format="jsonl",
        export_path="generated_data/medical_instructions.jsonl"
    )
    
    # Print results with document sources
    print("\n=== Generated Medical Instructions ===")
    for i, sample in enumerate(results['samples'], 1):
        print(f"\nInstruction {i}:")
        print(f"Q: {sample['instruction']}")
        print("\nRelevant Documents:")
        for j, doc in enumerate(sample['relevant_documents'], 1):
            print(f"Doc {j}: {doc[:100]}...")
        print("-" * 80)

if __name__ == "__main__":
    # Create output directory
    os.makedirs("generated_data", exist_ok=True)
    medical_doc_example() 