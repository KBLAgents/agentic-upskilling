# 🧩 Chapter 4: AI Agent Design Patterns

### 🎯 Lesson Objectives

By the end of this chapter, learners will be able to:

* Understand the core principles of agentic AI systems
* Identify and differentiate between key AI agent design patterns
* Implement tool-using and multi-agent workflows using frameworks like LangChain and Semantic Kernel
* Evaluate trade-offs in agent execution, memory, and orchestration strategies

---

### 📚 Prerequisites

* Intermediate understanding of Large Language Models (LLMs) and prompt engineering
* Familiarity with Retrieval-Augmented Generation (RAG) and context management
* Proficiency in Python programming
* Access to OpenAI or Azure OpenAI API keys
* Installed libraries: `langchain`, `semantic-kernel`, `openai`, `faiss` (optional)([The AiEdge Newsletter | Substack][1])

---

### ⏱️ Estimated Duration

* Lecture and Discussion: 90 minutes
* Hands-on Lab: 60 minutes

---

### 🧩 Topics Covered

* Introduction to AI Agents
* Anatomy of a Tool-Using LLM Agent
* Core Agent Design Patterns:

  * ReAct (Reason + Act)
  * Self-Ask with Search
  * Plan-and-Execute
  * Tool-Augmented Agents (Function Calling)
  * Multi-Agent Systems
* Role of Memory and Context in Agents
* Agent Orchestration Strategies([Introduction | 🦜️🔗 LangChain][2], [DEV Community][3], [Data Science Dojo][4])

---

### 🧠 Key Design Patterns Explained

#### 1. **ReAct Pattern (Reason + Act)**

* **Description**: Interleaves reasoning and acting steps, allowing the agent to generate thoughts, perform actions, and observe outcomes iteratively.
* **Use Case**: General-purpose agents reasoning through multi-step tasks.
* **Tools**: LangChain ReAct agent, AutoGen.
* **Example**:

  ```python
  from langchain.agents import initialize_agent, Tool
  from langchain.llms import OpenAI

  llm = OpenAI(temperature=0)

  tools = [
      Tool(name="Search", func=search_tool, description="Search the web"),
      Tool(name="Calculator", func=calculator_tool, description="Perform calculations")
  ]

  agent = initialize_agent(tools, llm, agent_type="react")
  response = agent.run("What is the population of France divided by the area of France?")
  print(response)
  ```



#### 2. **Self-Ask with Search**

* **Description**: The agent decomposes complex queries into sub-questions, answers them using search, and synthesizes the final answer.
* **Use Case**: Open-domain question answering.
* **Example**:

  ```python
  from langchain.agents import initialize_agent, Tool
  from langchain.llms import OpenAI

  llm = OpenAI(temperature=0)

  tools = [
      Tool(name="Search", func=search_tool, description="Search the web")
  ]

  agent = initialize_agent(tools, llm, agent_type="self-ask-with-search")
  response = agent.run("What is the capital of the country where the Eiffel Tower is located?")
  print(response)
  ```



#### 3. **Plan-and-Execute Agent**

* **Description**: Separates the planning and execution phases; the agent first creates a plan and then executes each step.
* **Use Case**: Workflow agents, automation pipelines.
* **Tools**: LangGraph (LangChain), Semantic Kernel planner.
* **Example**:

  ```python
  from langchain.agents import PlanAndExecuteAgent
  from langchain.llms import OpenAI

  llm = OpenAI(temperature=0)

  agent = PlanAndExecuteAgent(llm=llm)
  response = agent.run("Organize a birthday party for a 10-year-old.")
  print(response)
  ```



#### 4. **Tool-Augmented Agent (Function Calling)**

* **Description**: The agent invokes external tools or APIs to fetch data or perform actions.
* **Use Case**: Data lookup, email agents, automation.
* **Tools**: OpenAI Function Calling, LangChain Tools, Semantic Kernel Functions.
* **Example**:

  ```python
  from langchain.agents import initialize_agent, Tool
  from langchain.llms import OpenAI

  llm = OpenAI(temperature=0)

  tools = [
      Tool(name="WeatherAPI", func=weather_api_tool, description="Get weather information"),
      Tool(name="CalendarAPI", func=calendar_api_tool, description="Manage calendar events")
  ]

  agent = initialize_agent(tools, llm, agent_type="openai-functions")
  response = agent.run("Schedule a meeting on the next sunny day.")
  print(response)
  ```



#### 5. **Multi-Agent Systems**

* **Description**: Comprises multiple specialized agents that communicate or collaborate to perform complex tasks.
* **Use Case**: Modular systems with separate retriever, summarizer, generator agents.
* **Example**:

  ```python
  from langchain.agents import initialize_agent, Tool
  from langchain.llms import OpenAI

  llm = OpenAI(temperature=0)

  retriever_tool = Tool(name="Retriever", func=retriever_agent, description="Retrieve relevant documents")
  summarizer_tool = Tool(name="Summarizer", func=summarizer_agent, description="Summarize documents")
  generator_tool = Tool(name="Generator", func=generator_agent, description="Generate responses")

  tools = [retriever_tool, summarizer_tool, generator_tool]

  agent = initialize_agent(tools, llm, agent_type="multi-agent")
  response = agent.run("Provide a summary of the latest research on AI agents.")
  print(response)
  ```



---

### ⚙️ Tools & Frameworks

* **LangChain Agents**: Supports ReAct, Plan-and-Execute, Tool Agents.
* **Semantic Kernel Planners**: Goal-oriented planning with skill execution.
* **AutoGen**: Framework for building collaborative, tool-using AI agents.
* **Azure AI Agents**: Agent orchestration platform (Preview).([LangChain Blog][5])

---

### 🛠️ Hands-On Lab: Building a Tool-Using Support Agent

#### Lab Objective:

Build a support chatbot that utilizes:

* LLM reasoning
* Tools to retrieve knowledge (e.g., FAQ database)
* Tools to update user status
* Short-term memory to maintain context([YouTube][6])

#### Lab Tools:

* LangChain (Python)
* FAISS (for document retrieval)
* OpenAI GPT-4 (for agent reasoning)

#### Lab Tasks:

1. Define two tools:

   * `get_faq_answer(question)`
   * `update_user_status(user_id, status)`
2. Use LangChain's `initialize_agent` with the ReAct or OpenAI function-based agent.
3. Add a simple in-memory buffer for chat history.
4. Run an interactive agent loop with sample user queries.

#### Sample Code Snippet:

```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

def get_faq_answer(question):
    # Implement retrieval logic here
    return "This is a placeholder answer to your FAQ."

def update_user_status(user_id, status):
    # Implement status update logic here
    return f"User {user_id} status updated to {status}."

llm = OpenAI(temperature=0)

tools = [
    Tool(name="GetFAQAnswer", func=get_faq_answer, description="Lookup product FAQ"),
    Tool(name="UpdateUserStatus", func=update_user_status, description="Update user status in CRM")
]

agent = initialize_agent(tools, llm, agent_type="openai-functions")

response = agent.run("A customer says their order is delayed. What should I do?")
print(response)
```



---

### 📈 Outcome

By the end of this module, learners will be able to:

* Design agents that use reasoning and tools to accomplish complex tasks.
* Select appropriate patterns (ReAct, Plan-and-Execute, Multi-Agent) based on specific requirements.
* Implement agents using frameworks like LangChain, Semantic Kernel, or AutoGen.
* Extend agent capabilities through external tools and memory management.

---

### 🔗 Resources

* [LangChain Agents Documentation](https://docs.langchain.com/docs/components/agents)
* [AutoGen by Microsoft](https://github.com/microsoft/autogen)
* [Semantic Kernel Planners](https://github.com/microsoft/semantic-kernel)
* [ReAct Paper](https://arxiv.org/abs/2210.03629)
* [OpenAI Function Calling Documentation](https://platform.openai.com/docs/guides/function-calling)

---

[1]: https://newsletter.theaiedge.io/p/introduction-to-langchain-prompt?utm_source=chatgpt.com "Introduction to LangChain: Prompt Engineering Fundamentals"
[2]: https://python.langchain.com/v0.1/docs/modules/agents/agent_types/react/?utm_source=chatgpt.com "ReAct - ️ LangChain"
[3]: https://dev.to/jamesli/react-vs-plan-and-execute-a-practical-comparison-of-llm-agent-patterns-4gh9?utm_source=chatgpt.com "ReAct vs Plan-and-Execute: A Practical Comparison of LLM Agent ..."
[4]: https://datasciencedojo.com/newsletter/ai-agents-llms/?utm_source=chatgpt.com "AI Agents - The Next Big Leap of Generative AI in 2024"
[5]: https://blog.langchain.dev/planning-agents/?utm_source=chatgpt.com "Plan-and-Execute Agents - LangChain Blog"
[6]: https://www.youtube.com/watch?v=f7DBBeMFlTk&utm_source=chatgpt.com "5 AI Agent design patterns to use in your next app - YouTube"
