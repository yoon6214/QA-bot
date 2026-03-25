import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
# OpenAI 유료로 인해 무료버전 진행
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser



load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    # [ (시스템), (질문을 처리할 메세지) ]
    [ 
     ("system", "당신은 천문학 전문가입니다. 그리고 당신은 한국어로만 답변하는 AI입니다. "),
     ("user", "{input}")
     ]
)

llm = ChatOllama(model="llama3:8b")
output_parser = StrOutputParser()
# LCEL
chain = prompt | llm | output_parser


# user_input = input("질문을 입력하세요: ")

# response = chain.invoke({"input": user_input})
# print("Bot: ", response)



# gradio
import gradio as gr

def chat(user_input):
    return chain.invoke({"input": user_input})

demo = gr.Interface(fn=chat, inputs="text", outputs="text")
demo.launch()