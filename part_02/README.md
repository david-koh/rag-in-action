# RAG in Action - Part 2: Mastering Qdrant

A step-by-step guide to building production-grade Retrieval-Augmented Generation with persistent vector storage and metadata filtering.

## Quick Start

### Install Docker (if not already installed)

**macOS:**
```bash
brew install --cask docker
# Or download from: https://docker.com/products/docker-desktop
```

**Linux:**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

### Environment Setup

**Option 1: Conda (Recommended)**
```bash
conda env create -f environment.yml
conda activate rag-in-action-part2

# Mac M1/M2 optimization
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

**Option 2: pip**
```bash
pip install -r requirements.txt
```

### Install Ollama (if not from Part 1)

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

### Start Qdrant Server

```bash
docker-compose up -d
```

### Download Sample Data

```bash
python data/download_data.py
```

### Run the Tutorial

```bash
jupyter notebook notebooks/02_production_qdrant_demo.ipynb
```

### Stop Qdrant Server

```bash
# Stop server (keep data)
docker-compose down

# Complete cleanup (delete all data)
docker-compose down -v
rm -rf qdrant_storage/
```

## Requirements

- Python 3.10+
- Docker & Docker Compose
- 8GB+ RAM
- Ollama (local LLM)
- Uses MPS acceleration on Mac