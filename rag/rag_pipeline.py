import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding

load_dotenv()

# ✅ Load Environment Variables
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

if not QDRANT_URL:
    raise ValueError("QDRANT_URL is missing. Check your .env file.")

# ✅ Initialize Qdrant Client
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# ✅ Collection Name
COLLECTION_NAME = "hr_docs"
vector_store = QdrantVectorStore(client=qdrant_client, collection_name=COLLECTION_NAME)

# ✅ Storage Context
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# ✅ Embedding Model
embedding_model = OpenAIEmbedding() 

# ✅ Check if Collection Exists
collections = qdrant_client.get_collections()
collection_names = [col.name for col in collections.collections]

if COLLECTION_NAME in collection_names:
    print(f"✅ Collection '{COLLECTION_NAME}' found. Loading existing data...")
    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embedding_model)
else:
    print(f"⚠️ Collection '{COLLECTION_NAME}' not found. Creating a new index...")
    text_documents = []  # ⬅️ Make sure to load actual documents
    index = VectorStoreIndex.from_documents(text_documents, storage_context=storage_context, embed_model=embedding_model)
    index.storage_context.persist()

print("🚀 Qdrant is ready for querying!")

# ✅ Query Function
def query_qdrant(query: str):
    """Query the Qdrant database and return the response."""
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return str(response)
