import os
from typing import List

import requests
from bs4 import BeautifulSoup

class CustomWebLoader:
    def __init__(self, urls: list[str]):
        self.urls = urls
        self.documents = []
        # Header to mimic a browser and avoid being blocked
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

    def load(self):
        """Iterates through URLs and fetches content."""
        session = requests.Session()
        # Disables system proxy settings to avoid ProxyError
        session.trust_env = False 
        
        for url in self.urls:
            try:
                response = session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status() # Raise error for bad status (404, 500)
                
                # Parse HTML and extract clean text
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Remove script and style elements from the text
                for script_or_style in soup(["script", "style"]):
                    script_or_style.decompose()

                clean_text = soup.get_text(separator="\n", strip=True)
                self.documents.append(clean_text)
                
            except Exception as e:
                print(f"Failed to load {url}: {e}")

    def load_documents(self):
        """Matches your TextFileLoader signature."""
        self.load()
        return self.documents


class TextFileLoader:
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.path = path
        self.encoding = encoding

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path) and self.path.endswith(".txt"):
            self.load_file()
        else:
            raise ValueError(
                "Provided path is neither a valid directory nor a .txt file."
            )

    def load_file(self):
        with open(self.path, "r", encoding=self.encoding) as f:
            self.documents.append(f.read())

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".txt"):
                    with open(
                        os.path.join(root, file), "r", encoding=self.encoding
                    ) as f:
                        self.documents.append(f.read())

    def load_documents(self):
        self.load()
        return self.documents


class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunks.append(text[i : i + self.chunk_size])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            chunks.extend(self.split(text))
        return chunks


if __name__ == "__main__":
    loader = TextFileLoader("data/KingLear.txt")
    loader.load()
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print(len(chunks))
    print(chunks[0])
    print("--------")
    print(chunks[1])
    print("--------")
    print(chunks[-2])
    print("--------")
    print(chunks[-1])
