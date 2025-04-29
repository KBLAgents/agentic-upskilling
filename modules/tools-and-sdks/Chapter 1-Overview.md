# Chapter 1: Tools & SDKs Overview

High-level overview of the AI tools and SDKs available, with a focus on **OpenAI**and **Microsoft**tools. This chapter will help you understand the landscape of AI tools and how they can be used together.

---

## 🔹 **OpenAI Ecosystem**

### 1. **OpenAI API & ChatGPT**

- **Platform / SDK**: `openai` Python SDK, Node.js SDK, REST API  
- **Purpose**: Access OpenAI’s core models for text, image, and audio generation  
- **Key Features**:  
  - Chat/completion (GPT-4, GPT-3.5)  
  - Function calling, JSON mode  
  - Embeddings and file uploads  
  - Assistants API (multi-turn agents with memory/tools)  
  - DALL·E (text-to-image + editing), Whisper (speech-to-text)  
- **Use Cases**: Conversational AI, content generation, code assistants, summarization, search  
- **Access / Languages**: Python, JavaScript/TypeScript, REST (community clients for Java, Go, etc.)

---

### 2. **Assistants API**

- **Platform / SDK**: Included in `openai` Python SDK (`openai.beta.assistants`)  
- **Purpose**: Build persistent, goal-driven AI agents with memory and tools  
- **Key Features**:  
  - Threads, messages, and runs for conversations  
  - Built-in tools: `code_interpreter`, `retrieval`, `function_calling`  
  - File upload and persistent assistant configuration  
- **Use Cases**: Dev copilots, research bots, customer support agents  
- **Access / Languages**: Python, Node.js, REST

---

### 3. **Whisper (Speech-to-Text)**

- **Platform / SDK**: `openai.Audio.transcribe()` in Python SDK; also open-source CLI  
- **Purpose**: Transcribe audio/video to text  
- **Key Features**:  
  - Multilingual speech recognition  
  - Available as API and open-source model  
  - High accuracy for noisy or accented speech  
- **Use Cases**: Voice interfaces, meeting transcription, video captioning  
- **Access / Languages**: Python SDK, CLI, direct model usage

---

### 4. **DALL·E**

- **Platform / SDK**: `openai.Image.create()` via API or in ChatGPT Pro  
- **Purpose**: Generate and edit images from natural language prompts  
- **Key Features**:  
  - Text-to-image  
  - Inpainting (image editing)  
  - Available within ChatGPT + API  
- **Use Cases**: Marketing, art generation, UI mockups, concept design  
- **Access / Languages**: Python SDK, Node.js SDK, ChatGPT UI

---

### 5. **Embeddings API**

- **Platform / SDK**: `openai.Embedding.create()`  
- **Purpose**: Create vector embeddings for semantic search and RAG  
- **Key Features**:  
  - Models: `text-embedding-3-small`, `text-embedding-3-large`  
  - Token-efficient and high-quality  
- **Use Cases**: Semantic search, document clustering, retrieval-augmented generation  
- **Access / Languages**: Python, Node.js, REST

---

## 🔹 **Microsoft AI Ecosystem**

Microsoft and OpenAI have a strategic partnership, so many OpenAI models are integrated into Microsoft products.

### 1. **Azure OpenAI Service**

- **Platform / SDK**: Azure SDKs (Python, .NET, JS, Java) + Azure AI Studio  
- **Purpose**: Access OpenAI models on Microsoft Azure infrastructure  
- **Key Features**:  
  - GPT-4, GPT-3.5, Codex, DALL·E, Whisper hosted in Azure  
  - RBAC, logging, enterprise security and compliance  
  - Integration with Azure tools and services  
- **Use Cases**: Secure LLM deployment, enterprise AI applications, regulated industries  
- **Access / Languages**: Python, JavaScript, .NET, Java, CLI

---

### 2. **Microsoft Copilot Stack**

- **Platform / SDK**: Built into Microsoft 365, GitHub, and Dynamics apps  
- **Purpose**: Augment productivity tools with LLM-based AI  
- **Key Features**:  
  - Word, Excel, PowerPoint Copilots  
  - GitHub Copilot (for code), CRM and business logic copilots  
  - Powered by OpenAI models and Microsoft Graph  
- **Use Cases**: Writing, analysis, summarization, software development, business intelligence  
- **Access / Languages**: No direct SDK (consumer + enterprise SaaS integration)

---

### 3. **Azure Cognitive Services**

- **Platform / SDK**: Azure SDKs + REST APIs  
- **Purpose**: Provide prebuilt AI services beyond LLMs  
- **Key Features**:  
  - Speech-to-text, text-to-speech  
  - Translator, OCR, image tagging, anomaly detection  
  - Language Understanding (LUIS)  
- **Use Cases**: Accessibility tools, real-time translation, computer vision apps  
- **Access / Languages**: Python, JavaScript, Java, C#, REST

---

### 4. **Semantic Kernel (SK)**

- **Platform / SDK**: Semantic Kernel SDK (C#, Python, Java)  
- **Purpose**: Build orchestrated, modular AI agents with memory and planning  
- **Key Features**:  
  - Native & semantic functions (prompt templates)  
  - Plugins, connectors, and memory store  
  - Planners for task decomposition  
- **Use Cases**: Custom AI workflows, autonomous agents, task automation  
- **Access / Languages**: C#, Python, Java (preview); open source on GitHub

---

### 5. **Microsoft Autogen**

- **Platform / SDK**: `pyautogen` (Python library)  
- **Purpose**: Create multi-agent systems that collaborate using LLMs  
- **Key Features**:  
  - Agent types (AssistantAgent, UserProxyAgent, etc.)  
  - Custom tool integration and function calling  
  - Conversation orchestration and memory  
- **Use Cases**: Simulated teams, planning systems, AI researchers, multi-role workflows  
- **Access / Languages**: Python; open source on [GitHub](https://github.com/microsoft/autogen)

---

## 🔹 **Other Interoperable Tools**

| Tool | Purpose | Compatible With |
|------|---------|-----------------|
| **LangChain** | LLM orchestration and agent framework | OpenAI, Azure OpenAI, Hugging Face |
| **LlamaIndex** | Retrieval-augmented generation (RAG) | OpenAI, vector DBs |
| **Hugging Face Transformers** | Open models and datasets | Interoperable via APIs or hosting |
| **Replicate** | Unified API for running ML models | OpenAI, SD, Whisper, etc. |

---
