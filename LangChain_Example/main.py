import os
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import JasonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

llm = Ollama(model="gemma2:latest")

class Topic(BaseModel):
    description: str = Field(description="주제에 대한 간결한 설명")
    hashtags: str = Field(description="해시태그 형식의 키워드(2개 이상)")

question = "지구 온난화의 심각성에 대해 알려주세요"

parser = JasonOutputParser(pydantic_object = Topic)

prompt = ChatPromptTemplate.from_template(
    [
        ("system", "당신은 친절한 AI 어시스턴트입니다. 질문에 간결하게 답변하세요."),
        ("user", "#Format: {format_instructions}\n\#Question: {question}")
    ]
)

prompt = prompt.partial(format_instructions = parser.get_format_instructions())

chain = prompt | llm | parser

response = chain.invoke({"question" : question})
print(response)