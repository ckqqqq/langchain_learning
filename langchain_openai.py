import os 
from langchain.llms import OpenAI
from langchain import LLMChain
os.environ['OPENAI_API_TOKEN']="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"
davinci=OpenAI(model_name='text-davinci-003')

llm_chain=LLMChain(
    prompt=prompt,
    llm=davinci
)