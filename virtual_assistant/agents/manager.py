from typing import Dict

from langchain.agents.agent import Agent, AgentExecutor
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.memory.chat_memory import BaseChatMemory

class AgentManager:
    def __init__(
        self,
        agent: Agent,
    ):
        self.agent: Agent = agent
        self.executors: Dict[str, AgentExecutor] = {}

    def create_memory(self) -> BaseChatMemory:
        return ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    def create_executor(self, key: str) -> AgentExecutor:
        memory = self.create_memory()
        return AgentExecutor.from_agent_and_tools(
            agent=self.agent,
            tools=[],
            memory=memory,
            verbose=True,
        )

    def get_or_create_executor(self, key: str) -> AgentExecutor:
        if not (key in self.executors):
            self.executors[key] = self.create_executor(key=key)
        return self.executors[key]

    def remove_executor(self, key: str) -> None:
        if key in self.executors:
            del self.executors[key]
