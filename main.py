from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3")

template = (
    "You are an expert at answering questions about a product.\n"
    "Here are some relevant reviews: {reviews}\n"
    "Here is the question to answer: {question}"
)

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model
while True :
    print("\n\n---------------------------------------------------")
    question = input("Ask a question (q to quit): ")
    print("\n\n")
    if question =="q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({
    "reviews": [],
    "question": question})
    print(result)

