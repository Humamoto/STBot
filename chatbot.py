import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatBot:
    def __init__(self, feedback_processor, knowledge_base):
        self.feedback_processor = feedback_processor
        self.knowledge_base = knowledge_base

    def get_response(self, messages):
        context = self.knowledge_base.search(messages[-1]["content"])
        
        system_message = f"""Você é um assistente amigável chamado Senffinho que trabalha na empresa chamada Senff. 
        Utilize as seguintes informações para formular suas respostas, sem se apresentar novamente:
        Contexto: {context}
        
        Instruções:
        1. Baseie suas respostas no conteúdo do documento fornecido.
        2. Se a pergunta não puder ser respondida diretamente pelo documento, diga isso claramente.
        3. Use informações específicas e detalhadas do documento sempre que possível.
        4. Se houver ambiguidade na pergunta, peça esclarecimentos.
        5. Mantenha a continuidade da conversa, lembrando-se das perguntas e respostas anteriores."""

        messages = [{"role": "system", "content": system_message}] + messages

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return response.choices[0].message['content']