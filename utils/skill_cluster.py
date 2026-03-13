from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def cluster_skills(skills):

    embeddings = model.encode(skills)

    kmeans = KMeans(n_clusters=3)

    labels = kmeans.fit_predict(embeddings)

    return list(zip(skills, labels))