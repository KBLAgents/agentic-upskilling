# 🧩 **Module 5: Model Context Protocol (MCP)**

### 🎯 Learning Objectives:
By the end of this module, learners will be able to:
- Understand what the Model Context Protocol (MCP) is and why it matters in GenAI systems
- Use MCP to normalize inputs and outputs across different LLMs and providers
- Implement structured prompt and response handling
- Design GenAI systems that can switch between OpenAI, Azure, Hugging Face, etc., without rewriting logic

---

### 📌 Topics Covered

#### 5.1 What is the Model Context Protocol (MCP)?

[**MCP**](https://www.anthropic.com/news/model-context-protocol) is a design pattern that standardizes how prompts and responses are structured, parsed, and executed across different models and providers.

> Think of MCP as a **schema** for LLM interactions—like using GraphQL or gRPC instead of raw HTTP.

---

### 🧱 Why MCP is Important

| Problem | Without MCP | With MCP |
|--------|-------------|----------|
| Vendor lock-in | Switching models requires prompt re-engineering | One prompt schema for many backends |
| Lack of structure | Parsing raw text is error-prone | Responses are schema-aligned |
| Inconsistent tools | Each model has its own JSON, function-calling style | Unified tool interface |

---

### 📐 MCP Core Concepts

| Concept        | Description |
|----------------|-------------|
| **Inputs**     | Prompt format, parameters, tool calls |
| **Schema**     | Defines how the prompt is constructed and parsed |
| **Context**    | User history, function registry, embeddings, memory |
| **Output Format** | Defined structure for function return, JSON payloads |
| **Interoperability Layer** | Abstracts model-specific syntax differences (e.g., function_call for OpenAI vs tool_use for Claude) |

---

### 🔍 Example: Unified Prompt Across Providers

**MCP-style prompt (abstracted):**
```json
{
  "function": {
    "name": "GetWeather",
    "description": "Get current weather for a city",
    "parameters": {
      "city": "London"
    }
  }
}
```

- For **OpenAI**, MCP maps this to a `function_call`
- For **Claude**, MCP maps this to `tool_use`
- For **LLaMA or Hugging Face**, it’s converted to a natural language template:  
  _"Please get the current weather in London and respond with a JSON object."_

---

### ⚙️ Implementation Approaches

#### 1. **Using Semantic Kernel Function Schema**

```python
from semantic_kernel.functions import kernel_function

class WeatherPlugin:
    @kernel_function(name="GetWeather", description="Get weather")
    def get_weather(self, city: str) -> str:
        return f"The weather in {city} is sunny."
```

- This method abstracts the input/output schema via decorators and enables dynamic function routing.
- Plug it into OpenAI or Azure OpenAI seamlessly.

#### 2. **Manual Adapter Layer**

```python
def build_prompt(model, request_obj):
    if model == "openai":
        return {"function_call": {...}}
    elif model == "claude":
        return {"tool_use": {...}}
    else:
        return {"prompt": render_natural_language(request_obj)}
```

---

### 🧪 Hands-On Lab: MCP Server

**Goal:**  
[Create a simple MCP weather server and connect it to a host.](https://modelcontextprotocol.io/quickstart/server)
---

### 💡 Use Cases for MCP

| Use Case | Value |
|----------|-------|
| Multi-cloud LLM routing (Azure vs Bedrock vs OpenAI) | Reduced code duplication |
| Pluggable local and hosted models | Same business logic, different model |
| Unified evaluation and testing framework | Structured logs, test harnessing |

---

### ⚖️ Trade-offs and Challenges

| Challenge | Mitigation |
|----------|-------------|
| Abstraction overhead | Use templates and decorators |
| Loss of model-specific optimizations | Allow fallbacks for advanced use |
| Schema drift between tools | Use test cases + contract validation |

---

### 📘 Resources
- [Semantic Kernel Function Schema](https://learn.microsoft.com/en-us/semantic-kernel/functions/function-schema)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tool Use Guide](https://docs.anthropic.com/claude/docs/tool-use)
- [AWS Bedrock Schema Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)

---

### ✅ Check Your Understanding

- What’s the benefit of using MCP across different LLMs?
- How does MCP simplify debugging and scaling?
- What happens if one provider doesn’t support structured tool calling?

---