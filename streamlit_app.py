import streamlit as st
import spacy
from transformers import pipeline
from PyPDF2 import PdfReader

# Load NLP model
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

# Title
st.title("AI-powered Legal Document Analyzer")
st.write("Upload a legal document (PDF or TXT) to extract clauses, entities, and summarize key content.")

# File upload
uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])
text = ""

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")

    if text:
        st.subheader("Named Entity Recognition")
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        for entity, label in entities:
            st.write(f"{entity} — {label}")

        st.subheader("Summarization")
        if len(text) > 1000:
            text = text[:1000]  # Limit text length for summarization
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        st.success(summary[0]['summary_text'])