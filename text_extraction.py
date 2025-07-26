import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extract text page by page using pdfplumber"""
    text_pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            text_pages.append((page_num, text))
    return text_pages

def chunk_text(text, max_chunk_size=300):
    """Split text into chunks of ~max_chunk_size words."""
    words = text.split()
    chunks, current_chunk = [], []
    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= max_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks
