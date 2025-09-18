# RAG in Action - Part 1: The RAG Revolution

A step-by-step guide to building a basic Retrieval-Augmented Generation system from scratch.

## Quick Start

### Environment Setup

**Option 1: Conda (Recommended)**
```bash
conda env create -f environment.yml
conda activate rag-tutorial
```

**Option 2: pip**
```bash
pip install -r requirements.txt
```

### Install Ollama

**macOS:**
```bash
brew install ollama
ollama pull llama3.1:8b
ollama serve
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3.1:8b
ollama serve
```

### Run the Tutorial

```bash
jupyter notebook notebooks/01_naive_rag_demo.ipynb
```

## Requirements

- Python 3.10+
- 8GB+ RAM
- Ollama (local LLM)
- Uses MPS acceleration on Mac