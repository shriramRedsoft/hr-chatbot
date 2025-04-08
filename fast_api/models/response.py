from pydantic import BaseModel

class QueryResponse(BaseModel):
    query: str
    response: str