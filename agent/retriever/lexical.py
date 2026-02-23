def retrieve_lexical(query, faq_text, top_k=3):
    # Normalize query
    query_words = set(query.lower().split())

    # Split FAQ into blocks (Q/A pairs)
    faq_block = faq_text.strip().split("\n\n")

    scored_blocks = []

    for block in faq_block:
        block_lower = block.lower()
        block_words = set(block_lower.split())

        # Keyword overlap score
        score = len(query_words.intersection(block_words))

        scored_blocks.append((score, block))
    
    # Sort by score descending order
    scored_blocks.sort(key=lambda x: x[0], reverse=True)

    # Return top_k matches with score > 0
    top_matches = [block for score, block in scored_blocks if score>0][:top_k]

    return top_matches