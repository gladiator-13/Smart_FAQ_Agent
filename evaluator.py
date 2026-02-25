def recall_at_k(retrieved, ground_truth, k):
    top_k_questions = [item["question"] for item in retrieved[:k]]
    return int(ground_truth in top_k_questions)

def reciprocal_rank(retrieved, ground_truth):
    for idx, item in enumerate(retrieved):
        if item["question"] == ground_truth:
            return 1 / (idx + 1)
    return 0

def evaluate(retriever, evaluation_set):
    recall1 = 0
    recall3 = 0
    mrr = 0
    
    for sample in evaluation_set:
        retrieved = retriever(sample["query"])
        
        recall1 += recall_at_k(retrieved, sample["ground_truth"], 1)
        recall3 += recall_at_k(retrieved, sample["ground_truth"], 3)
        mrr += reciprocal_rank(retrieved, sample["ground_truth"])
    
    n = len(evaluation_set)
    
    return {
        "Recall@1": recall1 / n,
        "Recall@3": recall3 / n,
        "MRR": mrr / n
    }