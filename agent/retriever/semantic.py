import numpy as np
from sentence_transformers import SentenceTransformer

class SemanticRetriever:

    def __init__(self, faq_data, model_name="all-MiniLM-L6-v2"):
        """
        faq_data: list of dicts like:
        [
            {"question":"....", "answer":"..."},
            ...
        ]
        """
        self.faq_data = faq_data
        self.model = SentenceTransformer(model_name)

        # Precompute FAQ embeddings
        self.questions = [item["question"] for item in faq_data]
        self.embeddings = self.model.encode(self.questions, convert_to_numpy=True)

    def cosine_similarity(self, vec1, vec2):
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1)*np.linalg.norm(vec2))

    def retrieve_semantic(self, query, top_k=3):
        query_embedding = self.model.encode([query], convert_to_numpy=True)[0]

        similarities = [
            self.cosine_similarity(query_embedding, faq_embedding)
            for faq_embedding in self.embeddings
        ]

        top_indices = np.argsort(similarities)[-top_k:][::-1]

        for i in top_indices:
            print("Score:", similarities[i], "| Question:", self.faq_data[i]["question"])

        return [self.faq_data[i] for i in top_indices]
    