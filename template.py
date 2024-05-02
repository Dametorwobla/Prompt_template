from langchain_openai import ChatOpenAI
from langchain import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(key = api_key, model_name="text-davinci-003")

#FOR COMPLEX PROJECTS
#Prompt Templates help in keeping codes clean
#This is how to draft a prompt template for clean code purposes
template = """
{our_text}

Can you create a post for tweet in {wordsCount} words for the above?
"""

prompt = PromptTemplate(
    input_variables=["wordsCount","our_text"],
    template=template,
)

final_prompt = prompt.format(wordsCount='3',our_text="I love trips, and I have been to 6 countries. I plan to visit few more soon.")

print (llm(final_prompt))