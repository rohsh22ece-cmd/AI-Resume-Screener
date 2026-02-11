from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# In-memory storage
resume_store = {}

def add_resume(resume_id, text):
    embedding = model.encode(text)
    resume_store[resume_id] = embedding

def search_resume(job_description):
    job_embedding = model.encode(job_description)

    results = []
    for resume_id, resume_embedding in resume_store.items():
        score = np.dot(job_embedding, resume_embedding) / (
            np.linalg.norm(job_embedding) * np.linalg.norm(resume_embedding)
        )
        results.append((resume_id, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results
