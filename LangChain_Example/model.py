import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

load_dotenv()

class ollamaAgent():
    def __init__(self, temperature: float = 0.77):
        self.model_name = "llama3"
        self.seed = 42
        self.temperature = temperature
        self.llm = ChatOllama(
            model = self.model_name,
            temperature = self.temperature,
            seed = self.seed
        )

    def set_temperature(self, temperature: float):
        self.temperature = temperature
        self.llm = ChatOllama(
            model = self.model_name,
            temperature = self.temperature,
            seed = self.seed
        )

    def invoke_model(self, message: str = None):
        result = self.llm.invoke(message)
        response = result.content
        total_tokens = result.usage_metadata['total_tokens']
        return response, total_tokens