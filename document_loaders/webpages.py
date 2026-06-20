from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv


load_dotenv()


url = "https://www.apple.com/iphone/"

data =WebBaseLoader(url)


docs = data.load()
print(docs[0].page_content)