# Adobe Hackathon – Round 1B: Persona-Driven Document Intelligence

## Overview

This project implements an AI-powered document intelligence system for Adobe's Connecting the Dots Hackathon – Round 1B.  
It extracts and ranks relevant sections from multiple PDFs based on:

- A persona (who is reading)  
- A job-to-be-done (what they need)

The output is a structured JSON highlighting top relevant sections and sub-sections.  
The pipeline runs fully offline and is Docker-compatible.

---

## Key Features

- Handles multiple PDF files (3–10 documents)  
- Accepts a persona.json describing the persona and task  
- Extracts PDF text (using pdfplumber)  
- Computes semantic similarity using Sentence Transformers (offline)  
- Outputs ranked relevant sections and refined sub-sections in JSON format  
- Docker-ready, runs in an isolated environment without internet access

---

## Input Format

Place input files inside the input/ folder:

input/
├── doc1.pdf

├── doc2.pdf

└── persona.json


Example persona.json:

```json
{
  "persona": "PhD Researcher in Computational Biology",
  "job_to_be_done": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"
}

{
  "metadata": {
    "documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks",
    "timestamp": "2025-07-25T14:30:00Z"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "page": 4,
      "section_title": "Graph Neural Network Methodologies...",
      "importance_rank": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "page": 5,
      "refined_text": "GNNs have shown remarkable performance...",
      "importance_rank": 1
    }
  ]
}


