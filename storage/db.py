# storage/db.py

document_store = []

def add_document(title, content, tags=None):
    document = {
        "title": title,
        "content": content,
        "tags": tags or []
    }
    document_store.append(document)

def get_all_documents():
    return document_store

def get_document_by_title(title):
    for doc in document_store:
        if doc["title"] == title:
            return doc
    return None
