from jiwer import wer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_wer(original, transcript):
    return wer(original, transcript)

def semantic_similarity(text1, text2):
    emb1 = model.encode(text1)
    emb2 = model.encode(text2)

    sim = cosine_similarity([emb1], [emb2])[0][0]
    return float(sim)

def hallucination_rate(similarity, threshold=0.6):
    if similarity < threshold:
        return 1
    return 0
    