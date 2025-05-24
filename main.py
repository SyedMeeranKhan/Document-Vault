import streamlit as st
from storage.db import add_document, get_all_documents
from parser.pdf_parser import extract_text_from_pdf
from parser.docx_parser import extract_text_from_docx
from parser.ocr import ocr_from_image
from search.indexer import search_documents
import io


st.title("📄 Document Vault")

# --- Upload section ---
uploaded = st.file_uploader("Upload a document", type=["pdf", "docx", "jpg", "png"])
tags_str = st.text_input("Tags (comma-separated):")
if uploaded:
    file_type = uploaded.type
    content = ""
    if file_type == "application/pdf":
        content = extract_text_from_pdf(uploaded)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        content = extract_text_from_docx(uploaded)
    elif file_type in ["image/png", "image/jpeg"]:
        img_bytes = uploaded.read()
        img_stream = io.BytesIO(img_bytes)
        content = ocr_from_image(img_stream)
    else:
        st.error("Unsupported file type.")
    if content:
        tags = [t.strip() for t in tags_str.split(",") if t.strip()] if tags_str else []
        add_document(uploaded.name, content, tags=tags)
        st.success(f"{uploaded.name} processed and stored!")

# --- Search section ---
st.header("🔍 Search Documents")
query = st.text_input("Enter keyword to search in documents:")
docs = get_all_documents()
if query:
    docs = search_documents(query, docs)
    st.write(f"Found {len(docs)} document(s) matching '{query}'.")

# --- Tag filter ---
all_tags = sorted(set(tag for doc in get_all_documents() for tag in doc['tags']))
selected_tag = st.selectbox("Filter by tag (optional):", [""] + all_tags)
if selected_tag:
    docs = [doc for doc in docs if selected_tag in doc['tags']]

# --- Display documents ---
for idx, doc in enumerate(docs):
    tag_str = ", ".join(doc['tags']) if doc['tags'] else "No tags"
    st.markdown(f"**{doc['title']}**  \n_Tags: {tag_str}_")
    st.text_area(
        "Content Preview", 
        doc['content'][:500] + "...", 
        height=100, 
        key=f"content-preview-{doc['title']}-{idx}"
    )