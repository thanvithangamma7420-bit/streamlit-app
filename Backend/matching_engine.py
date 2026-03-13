from sklearn.metrics.pairwise import cosine_similarity
from models.sbert_model import get_embedding

def calculate_similarity(resume_text, job_description):

    resume_embedding = get_embedding(resume_text)
    job_embedding = get_embedding(job_description)

    similarity = cosine_similarity(resume_embedding, job_embedding)

    return similarity[0][0] * 100