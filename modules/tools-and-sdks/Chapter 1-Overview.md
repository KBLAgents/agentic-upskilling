# Chapter 1: Tools & SDKs Overview

High-level overview of the AI tools and SDKs available. This chapter will help you understand the landscape of AI tools, when to use or not use each one as well as how they can be used together.

>Disclaimer: This is not an exhaustive list of tools and SDKs available in the AI landscape.

---

## Table of Contents

- [Foundation Models](#foundation-models)
  - [ChatGPT series](#chatgpt-series)
  - [Whisper](#whisper)
  - [DALL·E](#dalle)
  - [Embeddings API](#embeddings-api)
  - [OpenAI API](#openai-api)
  - [Claude 3.7 Sonnet (Anthropic)](#claude-37-sonnet-anthropic)
  - [Other Foundation Models](#other-foundation-models)
- [Retrieval-Augmented Generation (RAG)](#retrieval-augmented-generation-rag)
  - [Azure AI Search](#azure-ai-search)
  - [LlamaIndex](#llamaindex)
- [LLM Orchestration & Agent/Workflow Automation](#llm-orchestration--agentworkflow-automation)
  - [LangChain](#langchain)
  - [Microsoft AutoGen](#microsoft-autogen)
  - [Semantic Kernel (Microsoft)](#semantic-kernel-microsoft)
  - [Model Context Protocol (MCP)](#model-context-protocol-mcp)
  - [OpenAI Assistants / Agents](#openai-assistants--agents)
- [Cloud GenAI Platforms](#cloud-genai-platforms)
  - [Azure OpenAI Service](#azure-openai-service)
  - [Azure AI Foundry](#azure-ai-foundry)
  - [Azure AI Services](#azure-ai-services)
  - [Other Cloud GenAI Platforms](#other-cloud-genai-platforms)
- [Code Generation](#code-generation)
  - [GitHub Copilot](#github-copilot)
  - [Microsoft Copilot Stack](#microsoft-copilot-stack)

---

## Foundation Models

### ChatGPT series

- **Purpose**: Conversational AI with memory and plugins
- **Key Features**:
  - Chat interface with memory
  - Plugin ecosystem (web browsing, code interpreter, etc.)
  - Custom GPTs (fine-tuned models)
- **SDKs**: `openai.ChatCompletion.create()` in Python SDK; also available in ChatGPT UI
- **Access / Languages**: Python, JavaScript, ChatGPT UI
- **Resources**:
  - [ChatGPT Documentation](https://platform.openai.com/docs/guides/gpt/chatgpt)
  - [ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction)
- **When to Use**: Customer support, personal assistants, interactive applications
- **When Not to Use**: If open-source or on-premise solutions are required.

---

### Whisper

- **Purpose**: Transcribe audio/video to text  
- **Key Features**:
  - Multilingual speech transcription
  - Available as API and open-source model
  - High accuracy for noisy or accented speech
- **SDKs**: `openai.Audio.transcribe()` in Python SDK; also open-source CLI
- **Access / Languages**: Python, CLI, model weights
- **Resources**:
  - [Whisper API Documentation](https://platform.openai.com/docs/guides/speech-to-text/introduction)
  - [Whisper GitHub Repository](https://github.com/openai/whisper)
  - [API Reference: Transcription](https://platform.openai.com/docs/api-reference/audio)
- **When to Use**: Voice UI, meeting transcription, video captioning, multilingual input.
- **When Not to Use**: Real-time, low-latency applications with custom vocabularies.

---

### DALL·E

- **Purpose**: Generate and edit images from natural language prompts  
- **Key Features**:
  - Text-to-image
  - In-painting (natural language image editing)
  - Available within ChatGPT + API
- **SDKs**: `openai.Image.create()` via Python SDK and Node.js SDK
- **Access / Languages**: Python, Node.js, ChatGPT UI
- **Resources**:
  - [DALL·E API Documentation](https://platform.openai.com/docs/api-reference/images)
  - [DALL·E GitHub Repository](https://github.com/openai/dall-e)
- **When to Use**: Marketing, art generation, UI mockups, concept design
- **When Not to Use**: High-resolution, photorealistic tasks (Midjourney/SD may outperform).

---

### Embeddings API

- **Purpose**: Create vector embeddings for semantic search and RAG  
- **Key Features**:
  - Models: `text-embedding-3-small`, `text-embedding-3-large`
  - Token-efficient and high-quality
- **SDKs**: `openai.Embedding.create()` in Python/Node.js SDK
- **Access / Languages**: Python, JavaScript, REST
- **Resources**:
  - [Embeddings API Documentation](https://platform.openai.com/docs/guides/embeddings/introduction)
- **When to Use**: Semantic search, document clustering, retrieval-augmented generation

---

### OpenAI API

- **Purpose**: Access foundation models for text, image, and audio generation  
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
- **When to Use**: General-purpose AI applications, chat bots, content generation, Retrieval-Augmented Generation (RAG), code assistants.
- **When Not to Use**: If constrained by data locality or seeking open-source alternatives.

---

### Claude 3.7 Sonnet (Anthropic)

- **Purpose**: Conversational AI with long context understanding.
- **Key Features**:
  - High-quality responses
  - safety-focused design
- **SDKs**: [`anthropic`](https://pypi.org/project/anthropic/)
- **Resources**: 
  - [Anthropic Claude API](https://docs.anthropic.com/en/api/getting-started)
- **When to Use**: For applications needing extended context and safety.
- **When Not to Use**: If specific integrations with OpenAI tools are required.

---

### Other Foundation Models

Other models like Mistral, LLaMA, DeepSeek, Gemini etc. are available and can be used as alternatives.
They are not covered in this chapter as they are not related to the targeted upskilling.

---

## Retrieval-Augmented Generation (RAG)

### Azure AI Search

- **Purpose**: Enterprise-grade vector and hybrid search engine used to power RAG pipelines by indexing and retrieving relevant documents or chunks.
- **Key Features**:
  - Native vector search with support for [HNSW algorithm](https://en.wikipedia.org/wiki/Hierarchical_Navigable_Small_World)
  - Semantic ranking and hybrid search ([BM25](https://python.langchain.com/docs/integrations/retrievers/bm25/) + embeddings)
  - Built-in integration with Azure OpenAI for RAG
  - Indexers for data sources (blob storage, SQL, etc.)
  - Enrichment pipeline (OCR, entity recognition, key phrases)
  - Role-based access and encryption
  - Multi-lingual support and custom analyzers
- **SDKs / Tools**:
  - Azure SDKs for Python, .NET, JavaScript, Java, REST API, Azure AI Studio integration
- **Resources**:
  - [Azure AI Search Docs](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search)
- **When to Use**: enterprise RAG with Azure-hosted data, needing tight integration with Azure OpenAI, RBAC, security, hybrid or semantic search
- **When Not to Use**: For lightweight/local projects where Elastic or open-source tools are simpler

---

### LlamaIndex

- **Purpose**: Framework for building RAG applications.
- **Key Features**: Data connectors, indexing, query engines.
- **SDKs**: Python
- **Resources**:
  - [**LlamaIndex Documentation**](https://www.llamaindex.ai/)
- **When to Use**: For applications needing integration of external data sources.
- **When Not to Use**: For applications not requiring external data retrieval.

---

## LLM Orchestration & Agent/Workflow Automation

### LangChain

- **Purpose**: Framework for developing applications powered by language models.
- **Key Features**: Modular components, integration with various models and tools.
- **SDKs**: Python, JavaScript.
- **Resources**:
  - LangChain Documentation
- **When to Use**: For building complex LLM applications with multiple components.
- **When Not to Use**: For simple, single-function applications.

---

### Microsoft AutoGen

- **Purpose**: Multi-agent orchestration framework.
- **Key Features**:
  - Collaborative agents
  - function calling
  - simulation of social dynamics
- **SDKs**: Python
- **Resources**:
  - [Microsoft Autogen Documentation](https://www.microsoft.com/en-us/research/project/autogen/)
  - [Autogen GitHub Repository](https://github.com/microsoft/autogen)
- **When to Use**: For applications requiring multiple interacting agents, planning systems, AI research tools.
- **When Not to Use**: For single-agent or simple task automation.

---

### Semantic Kernel (Microsoft)

- **Purpose**: Build orchestrated, modular AI agents with memory, tools, and planning.
- **Key Features**:
  - Semantic + native functions
  - Memory and skills management
  - Planner and workflow orchestration
- **SDKs**: [Semantic Kernel SDKs](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide?pivots=programming-language-python) (C#, Python, Java)
- **Resources**:
  - [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
  - [Semantic Kernel GitHub Repository](https://github.com/microsoft/semantic-kernel)
  - [Semantic Kernel Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-python)de AI applications with complex workflows.
- **When to Use**: For building orchestrated Agents and AI applications with modular components, memory, and planning.
- **When Not to Use**: For lightweight or prototype applications.

---

### Model Context Protocol (MCP)

- **Purpose**: A protocol designed to standardize communication between AI models and their execution environments, enabling consistent context management, memory, and tool use
- **Key Features**:
  - Defines how context (messages, tools, memory, functions) is structured and passed to models
  - Aims to enable interoperability across AI platforms, tools, and agents
  - Focused on separating orchestration from model inference
  - Backed by OpenAI and other ecosystem partners
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
- **When to Use**:
  - Building interoperable agent frameworks
  - Integrating custom tools, memory stores, and APIs with LLMs
  - Supporting multi-model environments
- **When Not to Use**: If you are using a single model or framework without the need for interoperability

---

### OpenAI Assistants / Agents

- **Purpose**: Enable multi-step reasoning and decision-making by delegating tasks to tools or calling functions dynamically
- **Key Features**:
  - Tool use and function-calling via natural language
  - Memory and context management
  - Modular agent architecture using tools, functions, and retrieval systems
  - Custom workflows via OpenAI Assistants API (beta)
- **SDKs**: `openai.beta.assistants` via Python SDK
- **Access / Languages**: Python, REST API, supported via LangChain and other orchestration frameworks
- **Resources**:
  - [OpenAI Function Calling](https://platform.openai.com/docs/guides/gpt/function-calling)
  - [LangChain Agents Documentation](https://python.langchain.com/docs/modules/agents/)
- **When to Use**: Task automation, dynamic workflows, research assistants, coding copilots, customer service agents
- **When Not to Use**: For simple, single-step tasks

---

## Cloud GenAI Platforms

### Azure OpenAI Service

- **Purpose**: Access OpenAI models on Microsoft Azure infrastructure  
- **Key Features**:
  - GPT-4, GPT-3.5, Codex, DALL·E, Whisper hosted in Azure
  - RBAC, logging, enterprise security and compliance
  - Integration with Azure tools and services
- **SDKs**: `openai`, Azure SDKs (Python, .NET, JavaScript, Java), REST API, CLI
- **Access / Languages**: Python, .NET, JavaScript, Java, Azure Portal
- **Resources**:
  - [Azure OpenAI Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
  - [Azure OpenAI Python SDK](https://learn.microsoft.com/en-us/azure/ai-services/openai/supported-languages?tabs=dotnet-secure%2Csecure%2Cpython-secure%2Ccommand&pivots=programming-language-python)
  - [Azure OpenAI REST API](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
- **When to Use**: Secure LLM deployment, enterprise AI applications, regulated industries
- **When Not to Use**: If you need a lightweight or open-source solution, or if you want to use models outside Azure.

---

### Azure AI Foundry

- **Purpose**: Unified platform for designing, customizing, and managing AI solutions  
- **Key Features**:
  - Model catalog with OpenAI and third-party models
  - Prompt engineering, evaluation, deployment, monitoring
  - Integration with Azure services
  - Playground for evaluating models
  - Built-in automated evaluations: grounding, relevance, hallucination detection
- **SDKs**: Azure AI Foundry SDK, integrated with Azure SDKs
- **Access / Languages**: Python, C#, JavaScript (coming soon), Azure Portal
- **Resources**:
  - [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
  - [Azure AI Foundry SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview?tabs=sync&pivots=programming-language-python)
  - [Azure AI Foundry REST API](https://learn.microsoft.com/en-us/rest/api/aifoundry/?view=rest-aifoundry-model-inference-2024-05-01-preview)
- **When to Use**: End-to-end AI application development, enterprise AI workflows
- **When Not to Use**: You use models outside Azure, You want complete control over infrastructure or lightweight experimentation

---

### Azure AI Services

- **Purpose**: Prebuilt AI services for language, vision, speech, and decision-making  
- **Key Features**:
  - Speech-to-text, text-to-speech, OCR, image tagging
  - Language Understanding (LUIS), translation, anomaly detection
- **SDKs**: Azure SDKs (Python, JavaScript, Java, .NET), REST APIs
- **Access / Languages**: Python, JavaScript, Java, C#, REST
- **Resources**:
  - [Azure AI Services Overview](https://learn.microsoft.com/en-us/azure/cognitive-services/)
  - [Azure SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/?view=azure-python)
- **When to Use**: Accessibility, translation, CV apps, voice bots
- **When Not to Use**: If you need custom models or deep learning frameworks, or if you want to work outside of Azure.

---

### Other Cloud GenAI Platforms

Other cloud platforms like AWS, Google Cloud, and IBM Watson also offer AI services and models.
They are not covered in this chapter as they are not related to the targeted upskilling.

---

## Code generation

### Github Copilot

- **Purpose**: AI-powered code completion and suggestions
- **Key Features**:
  - Context-aware code suggestions
  - Support for multiple programming languages
  - Integration with popular IDEs (VS Code, JetBrains, etc.)
  - Agent mode for vibe coding
  - MCP (Model Context Protocol) support
  - Copilot customization
- **SDKs**: N/A (integrated into VSCode)
- **Access / Languages**: No direct SDK access; IDE integration only
- **Resources**:
  - [VS Code Agent Mode](https://www.youtube.com/watch?v=dutyOc_cAEU)
  - [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
  - [Copilot Customization](https://code.visualstudio.com/docs/copilot/copilot-customization)
- **When to Use**: Code generation, debugging, learning new languages
- **When Not to Use**: N/A `:)`

---

### Microsoft Copilot Stack

- **Purpose**: Augment Microsoft 365, GitHub, and Dynamics apps with LLM-based AI  
- **Key Features**:
  - Word, Excel, PowerPoint, Outlook, Teams copilots
  - GitHub Copilot for code generation
  - CRM copilots in Dynamics
- **DKs**: N/A (integrated into Microsoft SaaS products)
- **Access / Languages**: No direct SDK access; SaaS integration only
- **Resources**:
  - [Microsoft Copilot Overview](https://www.microsoft.com/en-us/microsoft-365/copilot)
- **When to Use**: Writing, analysis, coding, summarization, CRM workflows. For users of Microsoft 365, GitHub, and Dynamics looking for AI enhancements
- **When Not to Use**: If you prefer open-source or non-Microsoft tools, or if you need custom integrations outside the Microsoft ecosystem.
