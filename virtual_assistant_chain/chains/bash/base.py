from langchain.chains import LLMBashChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

from virtual_assistant_chain.chains.bash.prompt import CREATE_FOLDER_TEMPLATE, CREATE_NEXT_APP_TEMPLATE, CREATE_POETRY_PYTHON_PROJECT

class BashChain:
    chain: LLMBashChain

    def __init__(self) -> None:
        llm = OpenAI(temperature=0.5)
        self.chain = LLMBashChain(llm=llm, verbose=True)

    def create_folder(self, folder_name: str, dest: str = "current directory"):
        input = PromptTemplate.from_template(CREATE_FOLDER_TEMPLATE).format(name=folder_name, dest=dest)
        return self.run(input)

    def create_next_app(self, app_name: str):
        input = PromptTemplate.from_template(CREATE_NEXT_APP_TEMPLATE).format(app_name=app_name)
        return self.run(input)

    def create_python_project(self, app_name: str):
        input = PromptTemplate.from_template(CREATE_POETRY_PYTHON_PROJECT).format(app_name=app_name)
        return self.run(input)

    def run(self, input: str):
        return self.chain.run(input)

if __name__ == "__main__":
    bash = BashChain()
    bash.create_python_project(app_name="test2")