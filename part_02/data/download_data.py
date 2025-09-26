#!/usr/bin/env python3
"""
Download Apple's 2023 10-K filing
"""

import requests
from pathlib import Path

def download_apple_10k():
    """Download Apple 2023 10-K report"""

    # Apple 2023 10-K official PDF from Q4CDN
    url = "https://s2.q4cdn.com/470004039/files/doc_earnings/2023/q4/filing/_10-K-Q4-2023-As-Filed.pdf"
    filename = "apple_10k_2023.pdf"

    data_dir = Path(__file__).parent
    file_path = data_dir / filename

    if file_path.exists():
        print(f"File already exists: {file_path}")
        return str(file_path)

    print("Downloading Apple 2023 10-K PDF...")

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Downloaded: {file_path}")
    print(f"Size: {file_path.stat().st_size / (1024*1024):.1f} MB")

    return str(file_path)

if __name__ == "__main__":
    download_apple_10k()