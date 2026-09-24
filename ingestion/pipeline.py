from dataclasses import dataclass
@dataclass
class Chunk:
    chunk_id: str        
    text: str            
    tokens: list[str]
    heading: str   
    source: str          

import jieba
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
    if len(tail) > overlap:
        result.append(tail)

    return result

#print(chunk_text("ABCDEFGHIJKLM", 5, 2))

import os
def load_markdown_dir(dir_path) -> list[dict]:
    result = []
    filenames = os.listdir(dir_path) 
    for filename in filenames :
        if filename.endswith(".md") :
            file_path = os.path.join(dir_path,filename)
            text = open(file_path,encoding="utf-8").read()
            result.append({"text": text, "source": filename})
    return result

def find_heading(piece:str) -> str :
    for line in piece.split("\n"):        
        if line.startswith("#"):          
            return line.lstrip("#").strip()   
    return ""         
                   
def build_chunks(data_dir) -> list[Chunk] :
    chunks = []
    for doc in load_markdown_dir(data_dir):
        for i, piece in enumerate(chunk_text(doc["text"])):
            chunks.append(Chunk(
                chunk_id=f"{doc['source']}-{i}",     
                text=piece,
                tokens=[w for w in jieba.cut(piece) if w.strip()],
                heading=find_heading(piece),         
                source=doc["source"],
            ))
    return chunks
