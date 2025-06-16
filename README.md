# AI-powered Legal Document Analyzer

This app allows you to upload legal documents (PDF or TXT), extracts important entities using spaCy, and generates a summary using Hugging Face's T5-small model.

## Features
- Named Entity Recognition (parties, dates, locations, laws, etc.)
- LLM-based summarization of contracts
- Streamlit UI for ease of use

## How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Demo

Use the Hugging Face Spaces deployment or run it locally.