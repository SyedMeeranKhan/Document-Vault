def search_documents(query, documents):
    results = []
    query_lower = query.lower()
    for doc in documents:
        if query_lower in doc["content"].lower():
            results.append(doc)
    return results
