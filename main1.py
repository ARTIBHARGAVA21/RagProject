from dotenv import load_dotenv 
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


data = PyPDFLoader("document_loaders/AWS Documentation.pdf")
docs = data.load()

template=ChatPromptTemplate.from_messages(
    [("system","You are a AI that summarizes  the text"),
      ("human","{data}")]
)
model = ChatMistralAI(model="mistral-small-2603")


prompt = template.format_messages(data = docs[0].page_content)

result = model.invoke(prompt)

print(result.content)