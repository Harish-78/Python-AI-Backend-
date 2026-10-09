from pydantic import BaseModel, HttpUrl, Field

class IngestRequest(BaseModel):
    pdf_url:HttpUrl=Field(...,description="Public URL to the PDF")
    collection_name:str=Field(...,description="Name of the Chroma collection")
    chunk_size:int=Field(500,description="Chunk size in characters")
    chunk_overlap:int=Field(50,description="Overlap between chunks")


class IngestResponse(BaseModel):
    status:str
    source_url:str
    num_pages:int
    num_chunks:int
    collection_name:str


class QueryRequest(BaseModel):
    question:str=Field(...,description="User query")
    collection_name:str=Field(...,description="Name of the collection")
    top_k:int=Field(5,description="Top k for the model params",ge=1,le=20)


class QueryResponse(BaseModel):
    answer:str
    sources:list[dict]=[]


class ParsePdfRequest(BaseModel):
    pdf_url:str=Field(...,description="PDF url to be extracted")

class ParsePdfResponse(BaseModel):
    num_pages:int
    pages:list[dict]
    
    
class ChunkRequest(BaseModel):
    pdf_url:str=Field(...,description="PDF URL to be extracted")
    chunk_size:int=Field(...,description="Size of the chunk to be perform")
    chunk_overlap:int=Field(...,description="Chunk overlap size to be perfrom chunking")
    
class ChunkResponse(BaseModel):
    num_pages:int
    num_chunks:int
    samples:list[dict]
    
class EmbedTextRequest(BaseModel):
    texts:list[str]=Field(...,description="Array of string to convert to embeddings")
    
class EmbedTextResponse(BaseModel):
    num_text:int
    num_vectors:int
    vectors:list[list[float]]
    