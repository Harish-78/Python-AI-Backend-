
def chunk_pages(pages:list[dict],chunk_size:int,chunk_overlap:int)->list[dict]:
    # chunk over lap shd be less then chunk size
    if chunk_overlap > chunk_size:
        raise ValueError("chunk overlap shd be less than chunk size")
    
    step=chunk_size-chunk_overlap
    chunks=[]
    
    # brute force => iterate on each page and in that page itself iterate make them into chunks
    for page in pages:
        text=page["text"]
        page_num=page["page"]
        start= 0
        chunk_index= 0
        while start < len(text):
            chunk_text=text[start:start+chunk_size]
            chunks.append({
                "text":chunk_text,
                "chunk_index":chunk_index,
                "page":page_num
            })
            start+=step
            chunk_index+=1
    return chunks
    