from .lexical import retrieve_lexical
# from .semantic import retrieve_semantic


def get_retriever(mode: str = "lexical"):
    if mode == "lexical":
        return retrieve_lexical
    # elif mode == "semantic":
    #     return retrieve_semantic
    else:
        raise ValueError(f"Unknown retrieval mode: {mode}")