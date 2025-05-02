# 🧩 **Chapter 1: Foundations of Generative AI Systems**

### 🎯 Learning Objectives:
By the end of this chapter, learners will be able to:
- Describe the different types of generative AI modalities (text, image, code, multimodal)
- Identify the core components required to build GenAI applications
- Compare major GenAI platforms and tools (OpenAI, Azure, Hugging Face, Anthropic, etc.)
- Set up a simple GenAI application using a hosted LLM

---

### 📌 Topics Covered

#### 1.1 Generative AI Modalities
Generative AI can create a wide range of content types:
- **Text** – Language models like GPT-4, Claude, LLaMA, Gemini
- **Image** – DALL·E, Stable Diffusion, Midjourney
- **Code** – Codex, GitHub Copilot, StarCoder
- **Audio** – ElevenLabs, OpenAI’s Whisper, Bark
- **Multimodal** – GPT-4V (vision), Gemini 1.5, CLIP

> **Use Case Example:**
> - **Text**: Automatic report generation for analysts
> - **Image**: Marketing banner generation for eCommerce
> - **Code**: Writing unit tests from functions
> - **Multimodal**: Extracting insights from PDFs or screenshots

---

#### 1.2 Core Building Blocks of GenAI Applications
| Component              | Description                                                  | Examples                                                  |
|------------------------|--------------------------------------------------------------|------------------------------------------------------------|
| **LLMs**               | Generate output from user prompts                            | OpenAI GPT-4, Claude, LLaMA                                |
| **Embedding Models**   | Convert data into vector space for semantic comparison       | `text-embedding-ada-002`, HuggingFace's BERT              |
| **Vector Stores**      | Store and retrieve embeddings for semantic search            | FAISS, Pinecone, Azure AI Search, Weaviate                 |
| **Prompt Orchestration** | Structure multi-step tasks with tools and memory          | LangChain, Semantic Kernel, LangGraph                      |
| **Storage & Retrieval**| Fetch documents or context for grounding generation          | Azure Blob, CosmosDB, PostgreSQL with pgvector            |
| **Model Hosting**      | Host inference endpoints on the cloud or edge                | Azure OpenAI, Hugging Face Inference Endpoints, AWS Bedrock |

---

#### 1.3 Overview of Key Platforms

| Provider        | Notable Capabilities | URL |
|----------------|----------------------|-----|
| **OpenAI**     | GPT-4, DALL·E, Assistants API | [OpenAI Platform](https://platform.openai.com/) |
| **Azure OpenAI** | Microsoft-hosted OpenAI APIs, Azure AI Search integration | [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview) |
| **Anthropic**  | Claude LLMs, safety-first design | [Anthropic](https://www.anthropic.com/index/claude) |
| **Hugging Face** | Open-source models, inference endpoints, AutoTrain | [Hugging Face](https://huggingface.co/) |
| **AWS Bedrock** | Foundation model APIs from various providers | [AWS Bedrock](https://aws.amazon.com/bedrock/) |

---

### 🧪 Hands-On Lab: Build Your First GenAI App

**Objective:**  
Build a basic GenAI-powered chat with [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview).

**Instructions:**
1. [Follow this guide to create a simple chat application using chat completions with Azure OpenAI Service Python SDK.](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?source=recommendations&tabs=keyless%2Ctypescript-keyless%2Cpython-new%2Ccommand-line&pivots=programming-language-python)

---

### 📘 Suggested Readings & Resources
- [Emerging Patterns in Building GenAI Products](https://martinfowler.com/articles/gen-ai-patterns/)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Microsoft Learn: Azure OpenAI](https://learn.microsoft.com/en-us/training/paths/get-started-azure-openai/)
- [Hugging Face Course](https://huggingface.co/learn/nlp-course/chapter1/1)
- [LangChain Quickstart](https://docs.langchain.com/docs/get_started/introduction)

---

### ✅ Check Your Understanding
- What are the core differences between an embedding model and a generative model?
- How does a vector store assist in grounding model responses?
- What are the trade-offs of using OpenAI vs Hugging Face?

---