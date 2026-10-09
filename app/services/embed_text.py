from app.core.config import GEMINI_API_KEY
from google import genai
from google.genai import types


_gemini_client = genai.Client(api_key=GEMINI_API_KEY)

def embed_text_by_google(text:list[str])->list[list[float]]:
    if not text:
        raise ValueError("Text should not be empty")
    
    result = _gemini_client.models.embed_content(
        model="gemini-embedding-2",
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
             output_dimensionality=768,
        )
    )
    
    return [e.values for e in result.embeddings] 
    