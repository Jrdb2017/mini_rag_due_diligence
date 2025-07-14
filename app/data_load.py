import os

def load_documents(docs_path=None):
    # Priority: explicit arg > env var > default for Docker > default for local dev
    docs_path = (
        docs_path or
        os.environ.get("DOCS_PATH") or
        "/app/docs" if os.path.exists("/app/docs") else "../docs"
    )
    documents = []
    for filename in os.listdir(docs_path):
        if filename.endswith(".txt"):
            with open(os.path.join(docs_path, filename), "r", encoding="utf-8") as f:
                documents.append(f.read())
    return documents 