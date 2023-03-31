from typing import Any, List
from langchain.callbacks.base import BaseCallbackHandler, CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationChain
from langchain.agents import initialize_agent, Tool, AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.utilities import PythonREPL
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)

from virtual_assistant.chat.prompt import SYSTEM_MESSAGE_TEMPLATE, HUMAN_MESSAGE_TEMPLATE
from virtual_assistant.chat.chat_type_template import TYPE_TEMPLATES

python_repl = PythonREPL()

tools = [
    Tool(
        name = "Python REPL",
        func=python_repl.run,
        description="useful for when you can answer questions from execute python code. the input to this should be valid python code."
    ),
]

class ChatConversation:
    # conversation_agent: AgentExecutor
    conversation_chain: ConversationChain

    def __init__(self, callbacks: List[BaseCallbackHandler] =[], system_message_template: str = SYSTEM_MESSAGE_TEMPLATE, human_message_template: str = HUMAN_MESSAGE_TEMPLATE):
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(human_message_template)
        ])
        llm = ChatOpenAI(streaming=True, temperature=0.5, max_tokens=2048, callback_manager=CallbackManager(callbacks), verbose=True)
        memory = ConversationBufferWindowMemory(memory_key="chat_history", k=5, return_messages=True)
        # self.conversation_agent = initialize_agent(tools, llm, prompt=prompt, agent="chat-conversational-react-description", verbose=True, memory=memory) 
        self.conversation_chain = ConversationChain(memory=memory, prompt=prompt, llm=llm)

    def chat(self, input: str) -> str:
        return self.conversation_chain.predict(input=input)
        # return self.conversation_agent.run(input)

    def chat_with_type(self, type: str, **kwargs: Any) -> str:
        if type not in TYPE_TEMPLATES:
            raise KeyError(f"{type} does not have template")
        template = TYPE_TEMPLATES[type]
        input = PromptTemplate.from_template(template).format(**kwargs)
        return self.chat(input)

if __name__ == "__main__":
    chat = ChatConversation()
    # position = "Senior Frontend developer"
    # tech_stacks = "React, Antd, Redux Toolkit, axios"
    # query= "Create Pokemon App that lists pokemons with images that come from PokeAPI sprites endpoint"

    # resp1 = chat.chat_with_type(type="code_generation", position=position, tech_stacks=tech_stacks, query=query)
    # print(resp1)

    resp2 = chat.chat_with_type(type="translator", language="Chinese", query="I want you to act as an interviewer. I will be the candidate and you will ask me the interview questions for the position position. I want you to only reply as the interviewer. Do not write all the conservation at once. I want you to only do the interview with me. Ask me the questions and wait for my answers. Do not write explanations.")
    print(resp2)