from sentence_transformers import SentenceTransformer
import faiss, os, pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = []
for file in os.listdir("knowledge_base"):
    with open(f"knowledge_base/{file}", "r", encoding="utf-8") as f:
        docs.append(f.read())

embeddings = model.encode(docs)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embeddings)

faiss.write_index(index, "math.index")
pickle.dump(docs, open("docs.pkl", "wb"))

print("RAG index built successfully")
