from typing import Any, List
from langchain.callbacks.base import BaseCallbackHandler 
from langchain.agents import initialize_agent, load_tools, AgentExecutor
from langchain.llms import OpenAI
from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)

from virtual_assistant.latest_chat.prompt import SYSTEM_MESSAGE_TEMPLATE, HUMAN_MESSAGE_TEMPLATE

class Repl:
    agent_executor: AgentExecutor

    def __init__(self, callbacks: List[BaseCallbackHandler] =[], system_message_template: str = SYSTEM_MESSAGE_TEMPLATE, human_message_template: str = HUMAN_MESSAGE_TEMPLATE):
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_message_template),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template(human_message_template)
        ])
        tool_names = ['python_repl']
        llm = OpenAI(temperature=0.5, max_tokens=2048, verbose=True)
        tools = load_tools(tool_names, llm=llm)
        self.agent_executor = initialize_agent(
            tools,
            llm,
            prompt=prompt,
            agent="zero-shot-react-description",
            verbose=True,
            ) 

    def run(self, input: str) -> str:
        return self.agent_executor.run(input)

if __name__ == "__main__":
    chat = Repl()
    resp1 = chat.run(input='add from 1 to 5')
    print(resp1)