# Chapter 1: Tools & SDKs Overview

High-level overview of the AI tools and SDKs available, with a focus on **OpenAI** and **Microsoft** tools. This chapter will help you understand the landscape of AI tools and how they can be used together.

---

## OpenAI Ecosystem

### 1. OpenAI API

- **Purpose**: Access OpenAI’s core models for text, image, and audio generation  
- **Key Features**:
  - Chat/completion (GPT-4, GPT-3.5)
  - Function calling, JSON mode
  - Embeddings and file uploads
  - DALL·E (text-to-image + editing), Whisper (speech-to-text)
- **Use Cases**: Conversational AI, content generation, code assistants, summarization, search
- **SDKs**: `openai` Python SDK, Node.js SDK, REST API
- **Access / Languages**: Python, JavaScript/TypeScript, REST

---

### 2. ChatGPT

- **Purpose**: Conversational AI with memory and plugins
- **Key Features**:
  - Chat interface with memory
  - Plugin ecosystem (web browsing, code interpreter, etc.)
  - Custom GPTs (fine-tuned models)
- **Use Cases**: Customer support, personal assistants, interactive applications
- **SDKs**: `openai.ChatCompletion.create()` in Python SDK; also available in ChatGPT UI
- **Access / Languages**: Python, JavaScript, ChatGPT UI

---

### 3. Embeddings API

- **Purpose**: Create vector embeddings for semantic search and RAG  
- **Key Features**:
  - Models: `text-embedding-3-small`, `text-embedding-3-large`
  - Token-efficient and high-quality
- **Use Cases**: Semantic search, document clustering, retrieval-augmented generation
- **SDKs**: `openai.Embedding.create()` in Python/Node.js SDK
- **Access / Languages**: Python, JavaScript, REST

---

### 4. Whisper

- **Purpose**: Transcribe audio/video to text  
- **Key Features**:
  - Multilingual speech recognition
  - Available as API and open-source model
  - High accuracy for noisy or accented speech
- **Use Cases**: Voice interfaces, meeting transcription, video captioning
- **SDKs**: `openai.Audio.transcribe()` in Python SDK; also open-source CLI
- **Access / Languages**: Python, CLI, model weights

---

### 5. DALL·E

- **Purpose**: Generate and edit images from natural language prompts  
- **Key Features**:
  - Text-to-image
  - Inpainting (image editing)
  - Available within ChatGPT + API
- **Use Cases**: Marketing, art generation, UI mockups, concept design
- **SDKs**: `openai.Image.create()` via Python SDK and Node.js SDK
- **Access / Languages**: Python, Node.js, ChatGPT UI

---

### 6. Agents

- **Purpose**: Create vector embeddings for semantic search and RAG  
- **Key Features**:
  - Models: `text-embedding-3-small`, `text-embedding-3-large`
  - Token-efficient and high-quality
- **Use Cases**: Semantic search, document clustering, retrieval-augmented generation
- **SDKs**: `openai-agents` in Python SDK
- **Access / Languages**: Python, JavaScript, REST

---

## Microsoft AI Ecosystem

### 1. Azure OpenAI Service

- **Purpose**: Access OpenAI models on Microsoft Azure infrastructure  
- **Key Features**:
  - GPT-4, GPT-3.5, Codex, DALL·E, Whisper hosted in Azure
  - RBAC, logging, enterprise security and compliance
  - Integration with Azure tools and services
- **Use Cases**: Secure LLM deployment, enterprise AI applications, regulated industries
- **SDKs**: `openai`, Azure SDKs (Python, .NET, JavaScript, Java), REST API, CLI
- **Access / Languages**: Python, .NET, JavaScript, Java, Azure Portal

---

### 2. Azure AI Foundry

- **Purpose**: Unified platform for designing, customizing, and managing AI solutions  
- **Key Features**:
  - Model catalog with OpenAI and third-party models
  - Prompt engineering, evaluation, deployment, monitoring
  - Integration with Azure services
- **Use Cases**: End-to-end AI application development, enterprise AI workflows
- **SDKs**: Azure AI Foundry SDK, integrated with Azure SDKs
- **Access / Languages**: Python, C#, JavaScript (coming soon), Azure Portal

---

### 3. Azure AI Services

- **Purpose**: Prebuilt AI services for language, vision, speech, and decision-making  
- **Key Features**:
  - Speech-to-text, text-to-speech, OCR, image tagging
  - Language Understanding (LUIS), translation, anomaly detection
- **Use Cases**: Accessibility, translation, CV apps, voice bots
- **SDKs**: Azure SDKs (Python, JavaScript, Java, .NET), REST APIs
- **Access / Languages**: Python, JavaScript, Java, C#, REST

---

### 4. Semantic Kernel

- **Purpose**: Build orchestrated, modular AI agents with memory, tools, and planning  
- **Key Features**:
  - Semantic + native functions
  - Memory and skills management
  - Planner and workflow orchestration
- **Use Cases**: Task automation, AI agents, workflow builders
- **SDKs**: [Semantic Kernel SDKs](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide?pivots=programming-language-python) (C#, Python, Java - preview)
- **Access / Languages**: C#, Python, Java; open source on GitHub

---

### 5. Microsoft Autogen

- **Purpose**: Create multi-agent systems that collaborate via LLMs  
- **Key Features**:
  - Agents: AssistantAgent, UserProxyAgent, etc.
  - Supports tools, custom APIs, memory, orchestration
- **Use Cases**: Multi-agent simulations, planning systems, AI research tools
- **SDKs**: [autogenstudio](https://github.com/microsoft/autogen) Python SDK
- **Access / Languages**: Python; open source on GitHub

---

### 6. Microsoft Copilot Stack

- **Purpose**: Augment Microsoft 365, GitHub, and Dynamics apps with LLM-based AI  
- **Key Features**:
  - Word, Excel, PowerPoint, Outlook, Teams copilots
  - GitHub Copilot for code generation
  - CRM copilots in Dynamics
- **Use Cases**: Writing, analysis, coding, summarization, CRM workflows
- **SDKs**: N/A (integrated into Microsoft SaaS products)
- **Access / Languages**: No direct SDK access; SaaS integration only

---

## Other Tools

| Tool                        | Purpose                                          | Compatible With                                     |
|-----------------------------|--------------------------------------------------|-----------------------------------------------------|
| [**LangChain**](https://www.langchain.com/)             | LLM orchestration and agent framework           | OpenAI, Azure OpenAI, Anthropic, Hugging Face       |
| [**LlamaIndex**](https://www.llamaindex.ai/)             | Retrieval-augmented generation (RAG)            | OpenAI, Anthropic, vector DBs                       |
| [**Hugging Face Transformers**](https://huggingface.co/docs/transformers/en/index) | Open models and datasets                      | Interoperable via APIs or local hosting             |
| [**Anthropic Claude API**](https://docs.anthropic.com/en/home)   | Conversational and agentic LLMs with long context | LangChain, LlamaIndex, REST-based apps              |

---
