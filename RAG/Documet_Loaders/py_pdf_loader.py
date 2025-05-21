## Limitation of PyPDFLoader 
## * for pdf of scanned PDF's or complex layouts, PyPDFLoader may not extract text accurately.
## Other pdf loaders like PyMuPDFLoader or PDFPlumberLoader may be more suitable for such cases.
## Check Langchain documentation for more details.

from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('./books/report_main.pdf')
docs= loader.load()
print(docs[0].page_content)
print(docs[0].metadata)