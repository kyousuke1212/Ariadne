def chunk_text(text, size=500, overlap=50):
    if size<=overlap :
        raise ValueError("size必须大于overlap")

    if len(text) <= size:
        return [text] 
     
    result = []
    start = 0
    while start + size <= len(text):      
        result.append(text[start : start + size])  
        start += size - overlap

    tail = text[start:]                     
    if len(tail) > overlap:
        result.append(tail)

    return result

#print(chunk_text("ABCDEFGHIJKLM", 5, 2))