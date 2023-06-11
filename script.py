from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator

loader = PyPDFLoader("example_data/layout-parser-paper.pdf")

index = VectorstoreIndexCreator().from_loaders([loader])

query = ""

index.query(query)
