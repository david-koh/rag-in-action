#!/usr/bin/env python3
"""
Utility functions for RAG in Action - Part 2: Mastering Qdrant
Helper functions used in the main notebook
"""

import subprocess
import time
import requests
from typing import List, Dict, Any, Optional, Tuple


def check_docker_running() -> bool:
    """Check if Docker daemon is running"""
    try:
        result = subprocess.run(
            ["docker", "info"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def wait_for_qdrant_ready(host: str = "localhost", port: int = 6333,
                         max_attempts: int = 30, delay: float = 2.0) -> bool:
    """
    Wait for Qdrant server to be ready to accept connections

    Args:
        host: Qdrant host
        port: Qdrant port
        max_attempts: Maximum number of connection attempts
        delay: Delay between attempts in seconds

    Returns:
        True if Qdrant is ready, False if timeout
    """
    url = f"http://{host}:{port}/health"

    for attempt in range(max_attempts):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return True
        except requests.exceptions.RequestException:
            pass

        if attempt < max_attempts - 1:
            time.sleep(delay)

    return False


def format_bytes(bytes_value: int) -> str:
    """Format bytes into human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f} TB"


def print_section_header(title: str, width: int = 60) -> None:
    """Print a formatted section header"""
    print("=" * width)
    print(f" {title}")
    print("=" * width)


def print_step_info(step: int, title: str, description: str = None) -> None:
    """Print formatted step information"""
    print(f"\n🔹 Step {step}: {title}")
    if description:
        print(f"   {description}")
    print("-" * 50)


def validate_environment() -> Dict[str, bool]:
    """
    Validate that all required components are available

    Returns:
        Dictionary with validation results
    """
    results = {
        "docker": False,
        "docker_compose": False,
        "python_packages": False,
        "ollama": False
    }

    # Check Docker
    results["docker"] = check_docker_running()

    # Check Docker Compose
    try:
        subprocess.run(
            ["docker-compose", "--version"],
            capture_output=True,
            timeout=5
        )
        results["docker_compose"] = True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Check Python packages
    try:
        import qdrant_client
        import langchain
        import sentence_transformers
        import torch
        results["python_packages"] = True
    except ImportError:
        pass

    # Check Ollama
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=5
        )
        results["ollama"] = "llama3.1:8b" in result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    return results


def print_validation_report(results: Dict[str, bool]) -> None:
    """Print environment validation report"""
    print_section_header("Environment Validation Report")

    status_symbols = {True: "✅", False: "❌"}

    print(f"{status_symbols[results['docker']]} Docker daemon running")
    print(f"{status_symbols[results['docker_compose']]} Docker Compose available")
    print(f"{status_symbols[results['python_packages']]} Required Python packages")
    print(f"{status_symbols[results['ollama']]} Ollama with llama3.1:8b")

    all_ready = all(results.values())
    print(f"\n🎯 Overall status: {'Ready to proceed' if all_ready else 'Setup required'}")

    if not all_ready:
        print("\n📋 Next steps:")
        if not results["docker"]:
            print("   - Install and start Docker")
        if not results["docker_compose"]:
            print("   - Install Docker Compose")
        if not results["python_packages"]:
            print("   - Run: pip install -r requirements.txt")
        if not results["ollama"]:
            print("   - Install Ollama and run: ollama pull llama3.1:8b")


if __name__ == "__main__":
    # Quick validation when run directly
    results = validate_environment()
    print_validation_report(results)