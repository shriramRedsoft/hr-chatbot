from rag.rag_pipeline import query_qdrant

def get_rag_response(query: str) -> str:
    """Handles query processing using RAG pipeline."""
    return query_qdrant(query)