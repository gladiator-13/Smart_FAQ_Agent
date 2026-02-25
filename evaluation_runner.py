from agent.retriever import get_retriever
from evaluation_data import evaluation_set
from evaluator import evaluate
from agent.data_loader import load_faq_from_txt
from sentence_transformers import SentenceTransformer

faq_data = load_faq_from_txt("data/faq.txt")
model = SentenceTransformer("all-MiniLM-L6-v2")

modes = ["lexical", "semantic", "hybrid"]

for mode in modes:
    retriever = get_retriever(mode, faq_data=faq_data)
    results = evaluate(retriever, evaluation_set)
    
    print(f"\nMode: {mode}")
    for metric, value in results.items():
        print(f"{metric}: {value:.3f}")