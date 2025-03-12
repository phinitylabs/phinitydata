"""
Test script for generating RAG test cases using ChromaDB and Phinity
"""

import os
from phinitydata.testset.rag_generator import TestsetGenerator
import chromadb
from phinitydata.connectors.chromadb import ChromaDBConnector

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Check for OpenAI API key
if "OPENAI_API_KEY" not in os.environ:
    print("Please set your OpenAI API key first:")
    print("export OPENAI_API_KEY='your-api-key-here'")
    print("or")
    api_key = input("Enter your OpenAI API key: ")
    os.environ["OPENAI_API_KEY"] = api_key

# Sample documents (two different topics for multi-hop questions)
doc1 = """
    Phinity is a comprehensive synthetic data generation platform designed for AI applications. 
    It helps create realistic test data for training and evaluating AI systems without using real user data.
    The platform specializes in generating question-answer pairs for RAG (Retrieval Augmented Generation) systems.
    It can create various types of questions including simple factual questions, complex multi-hop questions,
    and abstract questions that require synthesizing information from multiple sources.
    Phinity uses advanced natural language processing techniques to ensure the generated data is diverse and realistic.
    The platform integrates with vector databases like ChromaDB to generate evaluation data directly from stored documents.
    """

doc2 = """
    ChromaDB is an open-source vector database designed specifically for AI applications.
    It efficiently stores and retrieves vector embeddings, which are numerical representations of text, images, or other data.
    Vector databases are essential components of RAG systems, enabling semantic search beyond simple keyword matching.
    ChromaDB offers high-performance similarity search, allowing developers to find the most relevant documents for a given query.
    It supports various embedding models and can be deployed either in-memory for development or as a persistent database for production.
    The database is designed to scale horizontally and handle millions of embeddings efficiently.
    ChromaDB's Python client makes it easy to integrate with machine learning pipelines and LLM-based applications.
    """

try:
    print("Setting up ChromaDB collection...")

    # Initialize ChromaDB
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(
        name="test_collection",
        metadata={"description": "Test collection for RAG evaluation"}
    )

    # Add documents to ChromaDB
    collection.add(
        documents=[doc1, doc2],
        ids=["doc1", "doc2"],
        metadatas=[{"source": "phinity_docs"}, {"source": "chromadb_docs"}]
    )

    print("\nGenerating test cases from ChromaDB collection...")

    # Initialize TestsetGenerator and connector
    generator = TestsetGenerator()
    connector = ChromaDBConnector(collection)

    # Generate QA pairs from the collection
    testset = generator.generate_from_connector(
        connector=connector,
        testset_size=4
    )

    # Print generated QA pairs
    print("\nGenerated test cases:")
    for qa in testset.qa_pairs:
        print(f"\nInput Query: {qa.question}")
        print(f"Expected Answer: {qa.answer}")
        print("Retrieved Context:")
        for ctx in qa.context:
            print(f"- {ctx.strip()}")
        print("--------------------------------------------------")

    # Export results
    output_file = "rag_testset.json"
    testset.to_json(output_file)
    print(f"\nExported test cases to {output_file}")

except ValueError as e:
    print(f"\nError: {str(e)}")
    print("This might be due to insufficient or invalid content in the documents.")
except Exception as e:
    print(f"\nError: {str(e)}")
    if "API key" in str(e):
        print("\nPlease make sure your OpenAI API key is valid and has sufficient credits.") 