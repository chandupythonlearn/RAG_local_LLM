from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain_community.llms import Ollama
from langchain.agents import AgentExecutor, create_react_agent
from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.agents import tool


def query_agent(data, query):

    # Parse the csv file and creata Pandas Dataframe from it's content
    df = pd.read_csv(data)
   
    # llm = Ollama(model="mixtral:latest")
    llm = Ollama(model="mistral:latest")
    # tools = tool("python_repl")

    # Create a Pandas dataframe agent
    agent = create_pandas_dataframe_agent(llm, df, verbose=True,handle_parsing_errors=True)

    # agent_executor = AgentExecutor (
    # agent=agent, tool="python_repl",verbose=True, handle_parsing_errors=True
    # )

    #Python REPL: A Python shell used to evaluating and executing python commands.
    #It takes python code as input and outputs the result. The input python code can be generated from tool in the Langchain
    # return agent_executor.invoke(query,config={"callbacks":[ConsoleCallbackHandler()]})
    return agent.invoke(query,config={"callbacks":[ConsoleCallbackHandler()]})
