import os
from model import ollamaAgent

agent = ollamaAgent()

response, total_tokens = agent.invoke_model(message="What is capital of France?")
print(response)
print(total_tokens)