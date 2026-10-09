from pypdf import PdfReader
from io import BytesIO

def extract_pages(file_bytes:bytes)->list[dict]:
    reader = PdfReader(BytesIO(file_bytes))
    results = []
    for index,pages in enumerate(reader.pages):
        text= pages.extract_text() or ""
        if text.strip():
            results.append({"text":text,"page":index+1})
    return results


