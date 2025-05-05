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
- **Resources**:
  - [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
  - [OpenAI Python SDK](https://pypi.org/project/openai/)
  - [OpenAI Node.js SDK](https://www.npmjs.com/package/openai)
  - [OpenAI REST API](https://platform.openai.com/docs/api-reference/introduction)

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
- **Resources**:
  - [ChatGPT Documentation](https://platform.openai.com/docs/guides/gpt/chatgpt)
  - [ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction)

---

### 3. Embeddings API

- **Purpose**: Create vector embeddings for semantic search and RAG  
- **Key Features**:
  - Models: `text-embedding-3-small`, `text-embedding-3-large`
  - Token-efficient and high-quality
- **Use Cases**: Semantic search, document clustering, retrieval-augmented generation
- **SDKs**: `openai.Embedding.create()` in Python/Node.js SDK
- **Access / Languages**: Python, JavaScript, REST
- **Resources**:
  - [Embeddings API Documentation](https://platform.openai.com/docs/guides/embeddings/introduction)

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
- **Resources**:
  - [Whisper API Documentation](https://platform.openai.com/docs/guides/speech-to-text/introduction)
  - [Whisper GitHub Repository](https://github.com/openai/whisper)
  - [API Reference: Transcription](https://platform.openai.com/docs/api-reference/audio)

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
- **Resources**:
  - [DALL·E API Documentation](https://platform.openai.com/docs/api-reference/images)
  - [DALL·E GitHub Repository](https://github.com/openai/dall-e)

---

### 6. Agents

- **Purpose**: Enable multi-step reasoning and decision-making by delegating tasks to tools or calling functions dynamically
- **Key Features**:
  - Tool use and function-calling via natural language
  - Memory and context management
  - Modular agent architecture using tools, functions, and retrieval systems
  - Custom workflows via OpenAI Assistants API (beta)
- **Use Cases**: Task automation, dynamic workflows, research assistants, coding copilots, customer service agents
- **SDKs**: `openai.beta.assistants` via Python SDK
- **Access / Languages**: Python, REST API, supported via LangChain and other orchestration frameworks
- **Resources**:
  - [OpenAI Function Calling](https://platform.openai.com/docs/guides/gpt/function-calling)
  - [LangChain Agents Documentation](https://python.langchain.com/docs/modules/agents/)

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
- **Resources**:
  - [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
  - [Azure OpenAI Python SDK](https://learn.microsoft.com/en-us/azure/ai-services/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-secure%2Ccommand&pivots=programming-language-python)
  - [Azure OpenAI REST API](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)

---

### 2. Azure AI Foundry

- **Purpose**: Unified platform for designing, customizing, and managing AI solutions  
- **Key Features**:
  - Model catalog with OpenAI and third-party models
  - Prompt engineering, evaluation, deployment, monitoring
  - Integration with Azure services
  - Playground for evaluating models
- **Use Cases**: End-to-end AI application development, enterprise AI workflows
- **SDKs**: Azure AI Foundry SDK, integrated with Azure SDKs
- **Access / Languages**: Python, C#, JavaScript (coming soon), Azure Portal
- **Resources**:
  - [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
  - [Azure AI Foundry SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview?tabs=sync&pivots=programming-language-python)
  - [Azure AI Foundry REST API](https://learn.microsoft.com/en-us/rest/api/aifoundry/?view=rest-aifoundry-model-inference-2024-05-01-preview)

---

### 3. Azure AI Services

- **Purpose**: Prebuilt AI services for language, vision, speech, and decision-making  
- **Key Features**:
  - Speech-to-text, text-to-speech, OCR, image tagging
  - Language Understanding (LUIS), translation, anomaly detection
- **Use Cases**: Accessibility, translation, CV apps, voice bots
- **SDKs**: Azure SDKs (Python, JavaScript, Java, .NET), REST APIs
- **Access / Languages**: Python, JavaScript, Java, C#, REST
- **Resources**:
  - [Azure AI Services Overview](https://learn.microsoft.com/en-us/azure/cognitive-services/)
  - [Azure SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/?view=azure-python)

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
- **Resources**:
  - [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
  - [Semantic Kernel GitHub Repository](https://github.com/microsoft/semantic-kernel)
  - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-python)

---

### 5. Microsoft Autogen

- **Purpose**: Create multi-agent systems that collaborate via LLMs  
- **Key Features**:
  - Agents: AssistantAgent, UserProxyAgent, etc.
  - Supports tools, custom APIs, memory, orchestration
- **Use Cases**: Multi-agent simulations, planning systems, AI research tools
- **SDKs**: [autogenstudio](https://github.com/microsoft/autogen) Python SDK
- **Access / Languages**: Python; open source on GitHub
- **Resources**:
  - [Microsoft Autogen Documentation](https://www.microsoft.com/en-us/research/project/autogen/)
  - [Autogen GitHub Repository](https://github.com/microsoft/autogen)

---

### 6. Microsoft Copilot Stack

- **Purpose**: Augment Microsoft 365, GitHub, and Dynamics apps with LLM-based AI  
- **Key Features**:
  - Word, Excel, PowerPoint, Outlook, Teams copilots
  - GitHub Copilot for code generation
  - CRM copilots in Dynamics
- **Use Cases**: Writing, analysis, coding, summarization, CRM workflows
- **DKs**: N/A (integrated into Microsoft SaaS products)
- **Access / Languages**: No direct SDK access; SaaS integration only
- **Resources**:
  - [Microsoft Copilot Overview](https://www.microsoft.com/en-us/microsoft-365/copilot)

### 7. Github Copilot

- **Purpose**: AI-powered code completion and suggestions
- **Key Features**:
  - Context-aware code suggestions
  - Support for multiple programming languages
  - Integration with popular IDEs (VS Code, JetBrains, etc.)
  - Agent mode for vibe coding
  - MCP (Model Context Protocol) support
- **Use Cases**: Code generation, debugging, learning new languages
- **SDKs**: N/A (integrated into VSCode)
- **Access / Languages**: No direct SDK access; IDE integration only
- **Resources**:
  - [VS Code Agent Mode](https://www.youtube.com/watch?v=dutyOc_cAEU)
  - [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

---

## Model Context Protocol (MCP)

- **Purpose**: A protocol designed to standardize communication between AI models and their execution environments, enabling consistent context management, memory, and tool use
- **Key Features**:
  - Defines how context (messages, tools, memory, functions) is structured and passed to models
  - Aims to enable interoperability across AI platforms, tools, and agents
  - Focused on separating orchestration from model inference
  - Backed by OpenAI and other ecosystem partners
- **Use Cases**:
  - Building interoperable agent frameworks
  - Integrating custom tools, memory stores, and APIs with LLMs
  - Supporting multi-model environments
- **SDKs / Tools**:
  - Reference implementations under development (e.g., mcp-agent from OpenAI Labs)
  - JSON-based protocol: open standard meant to be adopted across frameworks (LangChain, Semantic Kernel, etc.)
  - Early alignment seen in OpenAI Assistants API, LangChain, and other orchestration layers
- **Access / Languages**:
  - No official SDK yet, but open standard is in discussion on GitHub
  - Intended to be language-agnostic and backend-neutral
- **Resources**:
  - [Model Context Protocol Overview](https://github.com/modelcontextprotocol)
  - [Anthropic - Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)

---

## Other Tools

| Tool                        | Purpose                                          | Compatible With                                     |
|-----------------------------|--------------------------------------------------|-----------------------------------------------------|
| [**LangChain**](https://www.langchain.com/)             | LLM orchestration and agent framework           | OpenAI, Azure OpenAI, Anthropic, Hugging Face       |
| [**LlamaIndex**](https://www.llamaindex.ai/)             | Retrieval-augmented generation (RAG)            | OpenAI, Anthropic, vector DBs                       |
| [**Hugging Face Transformers**](https://huggingface.co/docs/transformers/en/index) | Open models and datasets                      | Interoperable via APIs or local hosting             |
| [**Anthropic Claude API**](https://docs.anthropic.com/en/home)   | Conversational and agentic LLMs with long context | LangChain, LlamaIndex, REST-based apps              |

---
