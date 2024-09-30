from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_experimental.tools import PythonREPLTool
load_dotenv()


def main():
    print("started")

    instruction = """
        You are an agent designed to write and execute python code to answer questions you hav access to a python REPL
        which you can use to execute python code.
        If you get an error debug your code and try again.
        Only use the output of your code to answer the questions.
        you might know the answer without running any code, but you should still run the code to get the answer
        If it does not seem like you can write code to answer the questions just return "I don't know the answer"
        """
    
    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions = instruction)
    tools = [PythonREPLTool()]

    agent = create_react_agent(
        prompt=prompt,
        llm = ChatOpenAI(
            temperature = 0,
            model = "gpt-4-turbo"
        ),
        tools = tools,
    )

    python_agent_exector = AgentExecutor(agent=agent, tools=tools,verbose=True) 
    python_agent_exector.invoke(
        input={
            "input":"""
            generate and save in current working directory 15 QRcodes that points to www.udemy.com/course/langchain , you have qrcode package installed already
            Also save the generated code with in qrcodegenerator.py               
"""
        }
    )

    csv_agent_executor= create_csv_agent(
        llm= ChatOpenAI(temperature=0, model="gpt-4"),
        path = "mascots.csv",
        verbose = True
    )
if __name__ == "__main__":
    main()