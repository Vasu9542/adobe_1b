import os
import json
from text_extraction import extract_text_from_pdf, chunk_text
from embeddings import EmbeddingModel, rank_chunks
from rank_sections import create_output_json, save_json

def load_persona_job(input_dir):
    persona_file = os.path.join(input_dir, "persona.json")
    if not os.path.exists(persona_file):
        raise FileNotFoundError("persona.json not found in input directory")
    with open(persona_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["persona"], data["job_to_be_done"]

def process_documents(input_dir, output_dir):
    persona, job = load_persona_job(input_dir)
    query = f"Persona: {persona}. Task: {job}"
    embedder = EmbeddingModel()

    ranked_sections = []
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pdf"):
            path = os.path.join(input_dir, file_name)
            text_pages = extract_text_from_pdf(path)
            for page, text in text_pages:
                chunks = chunk_text(text)
                ranked = rank_chunks(query, chunks, embedder)
                for chunk, score in ranked[:3]:  # top 3 per page
                    ranked_sections.append((chunk, score, file_name, page))

    # Sort final combined ranking
    ranked_sections.sort(key=lambda x: x[1], reverse=True)

    output = create_output_json(
        documents=[f for f in os.listdir(input_dir) if f.endswith(".pdf")],
        persona=persona,
        job=job,
        ranked_sections=ranked_sections[:10]
    )
    save_json(output, os.path.join(output_dir, "output.json"))
    print("Processing complete. Output saved to output/output.json")

if __name__ == "__main__":
    input_dir = "./input"
    output_dir = "./output"
    process_documents(input_dir, output_dir)
