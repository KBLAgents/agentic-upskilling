# 🧩 **Chapter 3: Retrieval-Augmented Generation (RAG)**

### 🎯 Learning Objectives:
By the end of this module, learners will be able to:
- Understand the limitations of LLM context windows and static knowledge
- Implement a RAG system combining LLMs and external document stores
- Optimize chunking, embeddings, and semantic retrieval for better grounding
- Evaluate and debug relevance in responses

---

### 📌 Topics Covered

#### 3.1 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique that enhances an LLM’s output by retrieving relevant context from an external knowledge base (e.g., PDFs, documents, web pages) and injecting it into the model’s prompt.

> 🔁 Instead of asking the model to remember everything, we **retrieve** supporting content and let the model **generate** responses based on that context.

---

#### 3.2 Why Use RAG?

| Problem                     | Solution via RAG                       |
|----------------------------|----------------------------------------|
| LLMs hallucinate answers   | Add real-world grounding documents     |
| Model lacks recent updates | Retrieve dynamic data on demand        |
| High model token cost      | Store and search instead of re-ingesting |

---

#### 3.3 RAG Architecture Components

| Component            | Role                                            | Tools                                |
|----------------------|--------------------------------------------------|--------------------------------------|
| **Data Ingestion**   | Load docs, clean, chunk                        | LangChain, Haystack, custom scripts  |
| **Embedding**        | Convert chunks to vectors                      | `text-embedding-ada-002`, BGE, Cohere |
| **Vector Store**     | Search for semantic matches                    | Pinecone, Azure AI Search, FAISS     |
| **Retriever**        | Query store for top-N similar chunks           | LangChain retriever, Azure hybrid search |
| **LLM**              | Generate answers using retrieved context       | OpenAI, Anthropic, Azure OpenAI      |

---

#### 3.4 Chunking & Embedding Strategies

**Chunking Approaches:**
- Fixed-length window (e.g., 500 tokens)
- Sentence-aware split (LangChain’s `RecursiveCharacterTextSplitter`)
- Overlapping windows (helps preserve continuity)

**Embedding Models:**
- OpenAI `text-embedding-ada-002`
- Cohere multilingual embeddings
- BAAI BGE models (very strong on open-source)

> 💡 **Tip**: Always normalize text and remove boilerplate before embedding.

---

### 🔍 Example: Azure AI Search + OpenAI RAG Pipeline

1. Upload PDFs to Azure Blob Storage  
2. Use Azure Cognitive Search to index with semantic enrichment  
3. Create a Python app to:
   - Accept user queries  
   - Use Azure Search to find relevant chunks  
   - Add chunks to GPT prompt  
   - Return grounded response

---

### 🧪 Hands-On Lab: Build a RAG-Powered Q&A Bot

**Goal:**  
Create a document-based question answering bot using Azure AI Search and GPT-4.

**Steps:**

1. **Prepare your document corpus**
   - Upload sample PDFs (e.g., policies, FAQs) to Azure Blob Storage

2. **Set up Azure AI Search**
   - Create an index and enable semantic search
   - Configure skillset for metadata extraction

3. **Embed documents using Python**  
```python
from openai import OpenAIEmbeddings
from langchain.vectorstores.azuresearch import AzureSearch
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load and chunk
loader = PyPDFLoader("handbook.pdf")
pages = loader.load_and_split()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(pages)

# Embed
embeddings = OpenAIEmbeddings()
vectorstore = AzureSearch(azure_search_config, embeddings)
vectorstore.add_documents(chunks)
```

4. **Query pipeline**
```python
retrieved_docs = vectorstore.similarity_search("What’s our refund policy?", k=3)
context = "\n".join([doc.page_content for doc in retrieved_docs])

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": f"Answer based on:\n{context}"}]
)
print(response['choices'][0]['message']['content'])
```

---

### 📘 Resources
- [Azure AI Search + OpenAI RAG](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)
- [LangChain RAG Cookbook](https://python.langchain.com/docs/use_cases/question_answering/)
- [Pinecone Docs](https://docs.pinecone.io/)
- [OpenAI Embedding Guide](https://platform.openai.com/docs/guides/embeddings)

---

### ⚖️ Trade-offs and Challenges

| Challenge                    | Mitigation |
|-----------------------------|------------|
| Chunk size too small → LLM misses context | Use overlap & semantic splits |
| Irrelevant results in retrieval | Tune top-K, use hybrid search |
| Embedding drift (semantic mismatch) | Evaluate embedding quality + retrain |
| Input token limit exceeded | Rank & filter top documents carefully |

---

### ✅ Check Your Understanding

- What’s the difference between RAG and fine-tuning?
- Why are overlapping chunks often used in RAG pipelines?
- When would you use hybrid search (keyword + vector) over pure vector?

---