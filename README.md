# Phinity
Phinity is a synthetic data generation SDK designed to create high-quality, verifiable datasets for LLM development and evaluation.

Phinity builds upon Evol-Instruct, an instruction evolution method used by frontier AI labs to generate code SFT (supervised fine-tuning) datasets for LLMs. We extend this approach to support custom domain-specific dataset generation, ensuring high-quality data that aligns with your rules and context.

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

# Documentation and Roadmap:
  https://phinity.gitbook.io/phinity/use-cases/in-domain-sft

  
