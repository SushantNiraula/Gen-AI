from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader= DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader,
)

docs= loader.load()
print(len(docs))
print(docs[22].page_content)
print(docs[22].metadata)