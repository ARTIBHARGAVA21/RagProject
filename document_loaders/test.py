from langchain_community.document_loaders import TextLoader


data = TextLoader("Microsoft Azure Documentation.txt")

docs = data.load()
print(len(docs))