"""
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
tokens = enc.encode("Penguins huddle to stay warm.")
print(len(tokens))        # e.g. 7
print(tokens)             # [46459, 59837, 311, 1741, 7245, 13]
print(enc.decode(tokens)) # "Penguins huddle to stay warm."
"""

from dotenv import load_dotenv
from file_reader import extract_paragraphs 
from langchain_core.vectorstores import InMemoryVectorStore
from  langchain_openai import OpenAIEmbeddings


load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = InMemoryVectorStore(embedding)


chunks= extract_paragraphs("../pdfs/Penguins_ACL.pdf")

vector_store.add_texts(chunks)

print(f"Number of chunks added to the vector store: {len(chunks)}")