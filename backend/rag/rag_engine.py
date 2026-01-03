import faiss, pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("backend/rag/math.index")
docs = pickle.load(open("backend/rag/docs.pkl", "rb"))

def retrieve_context(query, k=2):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k)
    return [docs[i] for i in I[0]]
