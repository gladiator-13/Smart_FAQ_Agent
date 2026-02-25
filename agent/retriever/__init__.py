from .lexical import retrieve_lexical
from .semantic import SemanticRetriever
from .hybrid import hybrid_retrieve


def get_retriever(mode, faq_data):
    if mode == "lexical":
        return lambda query: retrieve_lexical(query, faq_data)
    elif mode == "semantic":
        semantic = SemanticRetriever(faq_data)
        return lambda query: semantic.retrieve_semantic(query, top_k=3)
    elif mode == "hybrid":
        return lambda query: hybrid_retrieve(query, faq_data)
    else:
        raise ValueError(f"Unknown retrieval mode: {mode}")