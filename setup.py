"""
Setup file for phinitydata package

This setup script configures the installation of the phinitydata package,
including all necessary dependencies and package data.
"""
from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="phinitydata",
    version="0.1.0",
    author="Sonya Jin",
    author_email="sonyajin@stanford.edu",
    description="A package for generating synthetic data for LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phinitylabs/phinitydata.git",
    
    # Explicitly include all packages and subpackages
    packages=find_packages(where=".", exclude=["tests*", "examples*"]),
    
    # Include package data
    include_package_data=True,
    package_data={
        "phinitydata": ["*.py", "**/*.py"],
    },
    
    # Ensure the package is zip_safe
    zip_safe=False,
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "langchain",
        "faiss-cpu",  # or faiss-gpu if needed
        "chromadb>=0.3.0",
        "tiktoken",
        "tqdm>=4.65.0",
        "numpy>=1.24.0",
        "pandas>=1.5.0",
        "transformers>=4.30.0",
        "torch>=2.0.0",
        "ragas>=0.0.20",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=4.0.0",
        ],
    }
)