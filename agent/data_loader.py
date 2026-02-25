def load_faq_from_txt(filepath):
    faq_data = []

    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    current_question = None
    current_answer = None

    for line in lines:
        line = line.strip()

        # Skip empty lines or section headers
        if not line or line.startswith("🔹"):
            continue

        # Detect numbered question line
        if line[0].isdigit() and "." in line:
            question_part = line.split(".", 1)[1].strip()
            current_question = question_part

        elif current_question and (current_answer is None):
            current_answer = line
            faq_data.append({
                "question": current_question,
                "answer": current_answer
            })
            current_question = None
            current_answer = None

    return faq_data