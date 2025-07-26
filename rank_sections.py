import json
from datetime import datetime

def create_output_json(documents, persona, job, ranked_sections):
    timestamp = datetime.utcnow().isoformat() + "Z"
    output = {
        "metadata": {
            "documents": documents,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": timestamp
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for rank, (text, score, doc_name, page) in enumerate(ranked_sections, start=1):
        output["extracted_sections"].append({
            "document": doc_name,
            "page": page,
            "section_title": text[:50] + "...",
            "importance_rank": rank
        })
        output["subsection_analysis"].append({
            "document": doc_name,
            "page": page,
            "refined_text": text,
            "importance_rank": rank
        })

    return output

def save_json(output, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
