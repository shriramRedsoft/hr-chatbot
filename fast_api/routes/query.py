from fastapi import APIRouter
from fast_api.models.request import QueryRequest
from fast_api.models.response import QueryResponse
from fast_api.services.rag_service import get_rag_response


router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    print('received query -->',request )
    response = get_rag_response(request.query)
    return {"query": request.query, "response": response}