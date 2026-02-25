from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sentence_transformers import SentenceTransformer


def lexical_score(query, text):
    q_tokens = set(query.lower().split())
    t_tokens = set(query.lower().split())

    if not q_tokens or not t_tokens:
        return 0.0
    
    intersection = q_tokens.intersection(t_tokens)
    union = q_tokens.union(t_tokens)

    return len(intersection) / len(union)

def semantic_scores(query_embedding, faq_embeddings):
    scores = cosine_similarity(
        [query_embedding], faq_embeddings
    )[0]
    return scores

def hybrid_retrieve(query, faq_data, alpha=0.7, beta=0.3, top_k=3):
    #Encode query once
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode(query)

    # Precomputed faq_embeddings
    faq_questions = [faq["question"] for faq in faq_data]
    faq_embeddings = model.encode(faq_questions)

    sem_scores = semantic_scores(query_embedding, faq_embeddings)

    results = []

    for i, faq in enumerate(faq_data):
        lex_score = lexical_score(query, faq["question"])
        final_score = alpha * sem_scores[i] + beta * lex_score 

        results.append({
            "question": faq["question"],
            "answer": faq["answer"],
            "score": float(final_score)
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:top_k]