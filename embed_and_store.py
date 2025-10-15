import os
from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from datetime import datetime

from langchain_text_splitters import RecursiveCharacterTextSplitter

embeddings_model = OllamaEmbeddings(model = "mxbai-embed-large")

analysts = [
    "sigmund_freud",
    "carl_gustav_jung"
]

db_locations = Path("stores")
data_locations = Path("data")
vector_stores = {}
retrievers = {}

for analyst in analysts:

    print(f"Analyst: {analyst}")

    db_location = db_locations / f"{analyst}_db"

    if not os.path.exists(db_location):
        vector_stores[analyst] = Chroma(
            collection_name = analyst,
            persist_directory = str(db_location),
            embedding_function = embeddings_model
        )
        print(f"Creating Embeddings at: {db_location}")
        analyst_data_path = data_locations / analyst
        files = [file for file in analyst_data_path.iterdir() if file.suffix == ".txt"]
        if not files:
            continue

        for file in files:
            print(f"Creating embeddings for file: {file}")
            split_and_embed_start = datetime.now()
            with open(file) as f:
                content = f.read()

            text_splitter = RecursiveCharacterTextSplitter(
                separators = ["\n\n", ".", "\n", ""],
                chunk_size = 500,
                chunk_overlap = 30,
                length_function = len
            )

            documents = text_splitter.create_documents([content])

            vector_stores[analyst].add_documents(documents = documents)
            split_and_embed_end = datetime.now()
            took = split_and_embed_end - split_and_embed_start
            print(f"Took: {took}")


for analyst in analysts:
    retrievers[analyst] = vector_stores[analyst].as_retriever(
        search_kwargs = {"k": 3}
    )

