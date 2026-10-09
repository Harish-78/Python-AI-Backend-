from fastapi import APIRouter,HTTPException
import httpx
from app.schemas.requests import (IngestRequest,IngestResponse,ParsePdfRequest,ParsePdfResponse,ChunkRequest,ChunkResponse,EmbedTextRequest,EmbedTextResponse)
from app.services.pdf_parser import (extract_pages)
from app.services.chunk_pages import(chunk_pages)
from app.services.embed_text import(embed_text_by_google)

router = APIRouter()

@router.get("/ping")
def get_ping():
    return {"Ping Status":"Success!"}


@router.post("/parse-pdf",response_model=ParsePdfResponse)
async def parse_pdf(request:ParsePdfRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                str(request.pdf_url),
                timeout=30,
                follow_redirects=True
            )
    except httpx.RequestError as e:
        raise HTTPException(status_code=502,detail=f"Download Failed: {str(e)}")

    if response.status_code != 200:
        raise HTTPException(status_code=400,detail="Unable to download the PDf")

    try:
         pages = extract_pages(response.content)
    except Exception as e:
         raise HTTPException(status_code=422,detail=f"Unable to extact the pages {str(e)}")
     
    if not pages:
         raise HTTPException(status_code=422, detail="No extactable content exixts to extract")

    previews=[{"page":p["page"],"preview":p["text"][:200] }for p in pages]

    return ParsePdfResponse(num_pages=len(pages),pages=previews)


@router.post('/chunk-test',response_model=ChunkResponse)
async def chunk_test(request:ChunkRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                str(request.pdf_url),
                timeout=30,
                follow_redirects=True
            )
    except httpx.RequestError as e:
        raise HTTPException(status_code=502,detail=f"Download Failed: {str(e)}")

    if response.status_code != 200:
        raise HTTPException(status_code=400,detail="Unable to download the PDf")

    try:
         pages = extract_pages(response.content)
    except Exception as e:
         raise HTTPException(status_code=422,detail=f"Unable to extact the pages {str(e)}")
     
    if not pages:
         raise HTTPException(status_code=422, detail="No extactable content exixts to extract")
     
    chunks = chunk_pages(pages=pages,chunk_size=request.chunk_size,chunk_overlap=request.chunk_overlap)
    
    return ChunkResponse(num_pages=len(pages),num_chunks=len(chunks),samples=chunks)
     

    
@router.post('/embed-text',response_model=EmbedTextResponse)
async def embed_text(request:EmbedTextRequest):
    result = embed_text_by_google(text=request.texts)
    
    return EmbedTextResponse(num_text=len(request.texts),num_vectors=len(result),vectors=result
    )
   