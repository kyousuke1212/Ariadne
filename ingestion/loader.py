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

docs = load_markdown_dir("data")
print(len(docs), docs[0]["source"])