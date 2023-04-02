from typing import Any, List
from langchain.callbacks.base import BaseCallbackHandler, CallbackManager
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)

from virtual_assistant.chat.prompt import SYSTEM_MESSAGE_TEMPLATE, HUMAN_MESSAGE_TEMPLATE

class ChatConversation:
    conversation_chain: ConversationChain

    def __init__(self, callbacks: List[BaseCallbackHandler] =[], system_message_template: str = SYSTEM_MESSAGE_TEMPLATE, human_message_template: str = HUMAN_MESSAGE_TEMPLATE):
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(human_message_template)
        ])
        llm = ChatOpenAI(streaming=True, temperature=0.5, max_tokens=2048, callback_manager=CallbackManager(callbacks), verbose=True)
        memory = ConversationBufferWindowMemory(memory_key="chat_history", k=5, return_messages=True)
        self.conversation_chain = ConversationChain(memory=memory, prompt=prompt, llm=llm)

    def chat(self, input: str) -> str:
        return self.conversation_chain.predict(input=input)
