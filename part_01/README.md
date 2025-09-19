# RAG in Action - Part 1: The RAG Revolution

A step-by-step guide to building a basic Retrieval-Augmented Generation system from scratch.

## Quick Start

### Install Conda (if not already installed)

**macOS:**
```bash
# Install Miniconda (lightweight)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh

# Or with Homebrew
brew install miniconda
```

**Linux:**
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

### Environment Setup

**Option 1: Conda (Recommended)**
```bash
conda env create -f environment.yml
conda activate rag-tutorial

# Mac M1/M2 optimization
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

**Option 2: pip**
```bash
pip install -r requirements.txt
```

### Install Ollama

**macOS:**
```bash
brew install ollama
ollama pull llama3.1:8b  # ~4GB download
ollama serve
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3.1:8b
ollama serve
```

### Test Installation

```bash
# Test LLM limitations (before RAG)
python 01_test_llm_limitations.py
```

### Install Jupyter (if not already installed)

**Option 1: With conda environment**
```bash
# Jupyter is already included in environment.yml
conda activate rag-tutorial
```

**Option 2: With pip**
```bash
pip install jupyter
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