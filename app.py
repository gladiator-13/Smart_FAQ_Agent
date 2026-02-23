from agent.retriever import get_retriever
from agent.prompt import build_prompt
from agent.llm import generate_response
from agent.memory import Memory
from agent.logger import logger

#Read the FAQ file
with open("data/faq.txt", "r", encoding="utf-8") as file:
    faq_content = file.read()

memory = Memory()

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        logger.info("Session terminated by user.")
        print("Exiting...")
        break

    logger.info(f"User Query: {user_input}")

    retrieval_mode = "lexical"
    retriever = get_retriever(mode=retrieval_mode)

    relevant = retriever(user_input, faq_content)

    if not relevant:
        logger.info("No relevant FAQ retrieved.")
        print("LLM: I do not have information about that.")
        continue

    context = "\n\n".join(relevant)
    logger.info(f"Retrieved Context: {context}")

    prompt = build_prompt(context, user_input)

    try:
        response = generate_response(prompt)
        logger.info(f"LLM Response: {response}")
    except Exception as e:
        logger.error(f"LLM Error: {str(e)}")
        print("LLM: Something went wrong.")
        continue

    memory.add(user_input, response)
    
    print("LLM: ", response)