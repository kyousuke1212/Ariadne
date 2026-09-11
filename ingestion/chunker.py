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

    tail = text[start:]                     # 尾巴
    if len(tail) > 2*overlap:
        result.append(tail)

    return result

print(chunk_text("ABCDEFGHIJKLM", 5, 2))
print(chunk_text("ABCDE", 5, 2))
print(chunk_text("ABC", 5, 2))
print(chunk_text("ABCDEF", 5, 2))