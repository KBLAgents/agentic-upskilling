# 🧩 **Chapter 4: Orchestration & Planning Agents**

### 🎯 Learning Objectives:
By the end of this chapter, learners will be able to:
- Differentiate between simple prompting, prompt chaining, and agentic orchestration
- Implement planning agents that use tools and memory to solve multi-step problems
- Compare different frameworks (Semantic Kernel, LangChain, ReAct, LangGraph)
- Build an agent that performs multi-turn interactions using tool calls

---

### 📌 Topics Covered

#### 4.1 What is Orchestration in GenAI?

**Orchestration** refers to structuring how an LLM interacts with:
- **Tools** (e.g., calculator, search engine, APIs)
- **Memory** (e.g., user preferences, chat history)
- **Multi-step tasks** (e.g., plan a trip, extract + summarize + format)

---

#### 4.2 Orchestration Patterns

| Pattern                  | Description                                                         | Example                          |
|--------------------------|---------------------------------------------------------------------|----------------------------------|
| **Prompt Chaining**      | Output of one prompt is input to the next                          | Multi-step content pipelines     |
| **Tool-Calling Agents**  | Use external APIs/tools in reasoning                               | Search → Get Weather → Summarize |
| **Planning Agents**      | Create sub-tasks and execute them in order                         | Semantic Kernel Planner          |
| **Stateful Agents**      | Maintain user-specific memory and history                          | Personal assistant or chatbot    |

---

#### 4.3 Orchestration Frameworks

| Framework         | Description                                                              | Links |
|------------------|--------------------------------------------------------------------------|-------|
| **Semantic Kernel** | Modular orchestration with planners, memory, skills                    | [Docs](https://learn.microsoft.com/en-us/semantic-kernel/) |
| **LangChain**        | Agents, tools, memory, chains, retrievers                             | [LangChain](https://docs.langchain.com/) |
| **LangGraph**        | Visual state machine for LLM-based agents                             | [LangGraph](https://www.langgraph.dev/) |
| **ReAct Pattern**    | Combines reasoning and action iteratively                             | [ReAct Paper](https://arxiv.org/abs/2210.03629) |

---

### 🔍 Example: Planner with Semantic Kernel

**Use Case:**  
A task-oriented assistant that gets news from the web, extracts summaries, and emails them.

**Flow:**
1. User: “Send me a 3-bullet summary of today's tech news.”
2. Planner creates:
   - `SearchForNews(topic="tech")`
   - `Summarize(text)`
   - `SendEmail(to, summary)`

> 🛠️ This is done using Semantic Kernel’s Planner + Skills.

---

### 🔍 Example: LangChain Tool-Using Agent

```python
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI

tools = [
    Tool(name="Calculator", func=lambda x: eval(x), description="Performs math"),
]

agent = initialize_agent(
    tools, OpenAI(temperature=0),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("What's 4.5 times 11, then add 32?")
```

---

### 🧪 Hands-On Lab: Build a Planner Agent with Semantic Kernel

**Goal:**  
Build a multi-skill AI assistant that uses a planner to decide between searching, summarizing, or generating emails.

**Step-by-Step:**

1. **Install Semantic Kernel SDK (Python):**
```bash
pip install semantic-kernel
```

2. **Define your skills**:
```python
# skills/search.py
def search_news(topic: str) -> str:
    return f"Fake search results for {topic}"

# skills/summarize.py
def summarize(text: str) -> str:
    return f"3-bullet summary of: {text}"
```

3. **Use Planner to orchestrate tasks**
```python
from semantic_kernel.planning.basic_planner import BasicPlanner
planner = BasicPlanner(kernel)
plan = planner.create_plan("Give me a short summary of recent AI news")

result = await kernel.run_async(plan)
print(result)
```

---

### 🧠 Agent Use Cases

| Use Case                       | Tools/Patterns Used                      |
|--------------------------------|------------------------------------------|
| Personal AI assistant          | Memory + Search + Summarization          |
| Research Co-Pilot              | ReAct + Web scraping + PDF tools         |
| Legal Document Assistant       | RAG + Planner + Form-filling tool        |
| Automated Report Generator     | Data scraping + Analysis + GPT formatting|

---

### ⚖️ Trade-offs and Challenges

| Challenge                      | Solution                                |
|-------------------------------|-----------------------------------------|
| Agents get stuck or loop      | Add max iterations, stop conditions     |
| Cost from too many tool calls | Use cache, optimize tool triggers       |
| Tool integration complexity   | Use well-typed skill APIs, SDKs         |
| Long prompt history limits    | Summarize intermediate outputs          |

---

### 📘 Resources
- [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)
- [LangChain Agent Docs](https://python.langchain.com/docs/modules/agents/)
- [LangGraph Examples](https://docs.langgraph.dev/)
- [OpenAI Tool Use Docs](https://platform.openai.com/docs/guides/function-calling)

---

### ✅ Check Your Understanding

- What’s the difference between a planner and a tool-using agent?
- Why is memory important in orchestrated agents?
- How can you control costs in agent-based GenAI systems?

---