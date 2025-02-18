###########################################
#  Testing LLM Models : Llamo 
#
###########################################
# pip install unstructured[docx] langchain langchainhub langchain_community langchain-chroma
# pip install ollama
# PS C:\WINDOWS\system32> ollama run llama3
# https://www.datacamp.com/tutorial/run-llama-3-locally

import ollama
import asyncio
from ollama import AsyncClient


def ask_llm():
    print("ASK LLM.....")
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": "How minorities contibute to bring great talent to companies?",
            },
        ],
    )
    print(response["message"]["content"])
    print("*"*100)



async def chat():
    """
    Stream a chat from Llama using the AsyncClient.
    """
    message = {
        "role": "user",
        #"content": "How minorities contibute to bring great talent to companies?"
        "content": "What is Python?"

    }
    async for part in await AsyncClient().chat(
        model="llama3", messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)


def test():
    print('testing')


if __name__ == '__main__' :
    test()
    #ask_llm()
    asyncio.run(chat())




