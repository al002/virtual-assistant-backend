from typing import Any, List
from langchain.callbacks.base import BaseCallbackHandler, CallbackManager
from langchain.callbacks import StdOutCallbackHandler
from langchain.agents import initialize_agent, load_tools, AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from virtual_assistant.latest_chat.prompt import SYSTEM_MESSAGE_TEMPLATE, HUMAN_MESSAGE_TEMPLATE

class LatestChatConversation:
    conversation_agent: AgentExecutor

    def __init__(self, callbacks: List[BaseCallbackHandler] =[], system_message_template: str = SYSTEM_MESSAGE_TEMPLATE, human_message_template: str = HUMAN_MESSAGE_TEMPLATE):
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(human_message_template)
        ])
        tool_names = ['google-serper']
        llm = ChatOpenAI(temperature=0.5, max_tokens=2048, verbose=True)
        tools = load_tools(tool_names, llm=llm)
        memory = ConversationBufferWindowMemory(memory_key="chat_history", k=5, return_messages=True)
        callbacks.append(StdOutCallbackHandler())
        self.conversation_agent = initialize_agent(
            tools,
            llm,
            prompt=prompt,
            agent="chat-conversational-react-description",
            verbose=True,
            memory=memory,
            callback_manager=CallbackManager(callbacks)
            ) 

    def chat(self, input: str) -> str:
        return self.conversation_agent.run(input)

if __name__ == "__main__":
    chat = LatestChatConversation()
    resp1 = chat.chat(input='Oscar best movie in 2023')
    print(resp1)