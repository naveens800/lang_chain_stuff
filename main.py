from dotenv import load_dotenv
load_dotenv(override=True)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

prompt = PromptTemplate(template="Question: {question}\nAnswer:", input_variables=["question"])

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)
chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run("what is the meaning of life?")
print(response)