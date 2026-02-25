from agent.retriever import get_retriever
from agent.prompt import build_prompt
from agent.llm import generate_response
from agent.memory import Memory
from agent.logger import logger
from agent.data_loader import load_faq_from_txt

#Read the FAQ file
faq_data = load_faq_from_txt("data/faq.txt")

memory = Memory()

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        logger.info("Session terminated by user.")
        print("Exiting...")
        break

    logger.info(f"User Query: {user_input}")

    retrieval_mode = "hybrid"
    retriever = get_retriever(mode=retrieval_mode, faq_data=faq_data)

    relevant = retriever(user_input)
    print("Retrieved: ", relevant)

    if not relevant:
        logger.info("No relevant FAQ retrieved.")
        print("LLM: I do not have information about that.")
        continue

    context = "\n\n".join(
    [f"Q: {item['question']}\nA: {item['answer']}" for item in relevant]
    )
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