def retrieve_lexical(query, faq_data, top_k=1):
    # Normalize query
    query_words = set(query.lower().split())

    scored = []

    for item in faq_data:
        question_words = set(item["question"].lower().split())
        score = len(query_words.intersection(question_words))

        scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [item for score, item in scored[:top_k]]