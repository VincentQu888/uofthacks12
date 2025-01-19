from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()

def teacher_generator_llm(prompt):
    chat = ChatGroq(temperature=0.5, model_name="llama-3.3-70b-versatile")
    system = "Pretend you are a music theory teacher making music theory questions"
    human = "{text}" 
    prompt_template = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt_template | chat
    response = chain.invoke({"text": prompt}) 
    return response.content


def student_generator_llm(prompt):
    chat = ChatGroq(temperature=0.5, model_name="llama-3.3-70b-versatile")
    system = "Pretend you are a music theory student making music theory questions to test your friends"
    human = "{text}" 
    prompt_template = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt_template | chat
    response = chain.invoke({"text": prompt}) 
    return response.content


def pro_generator_llm(prompt):
    chat = ChatGroq(temperature=0.5, model_name="llama-3.3-70b-versatile")
    system = "Pretend you are a music theory expert making music theory questions"
    human = "{text}" 
    prompt_template = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt_template | chat
    response = chain.invoke({"text": prompt}) 
    return response.content
