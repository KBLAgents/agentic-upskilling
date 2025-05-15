# AI Agent Design Patterns

---
![](https://markovate.com/wp-content/uploads/2024/06/Understanding-AI-Agents-1.webp)
## 🧠 Key Design Patterns Explained

### 1. **Chain of Thought Prompting**

* **Description**: Encourages the agent to think step-by-step by explicitly generating intermediate reasoning steps before arriving at a final answer.
* **Use Case**: Solving complex problems that require logical reasoning or multi-step calculations.
* **Example**:

  ```python
  from langchain.llms import OpenAI

  llm = OpenAI(temperature=0)

  prompt = """
  Solve the following problem step-by-step:
  If a train travels 60 miles per hour for 2 hours, then 30 miles per hour for 1 hour, how far does it travel in total?
  """

  response = llm(prompt)
  print(response)
  ```
### 2. **ReAct Pattern (Reason + Act)**

* **Description**: Interleaves reasoning and acting steps, allowing the agent to generate thoughts, perform actions, and observe outcomes iteratively.
* **Use Case**: General-purpose agents reasoning through multi-step tasks.
* **Tools**: LangChain ReAct agent, AutoGen.
* **Example**:

  ```python
  from langchain.agents import initialize_agent, Tool
  from langchain.llms import OpenAI

  # Placeholder implementation for search_tool and calculator_tool

  def search_tool(query):
      # Simulate a search operation
      return f"Search results for: {query}"

  def calculator_tool(expression):
      # Simulate a calculation operation
      try:
          return eval(expression)
      except Exception as e:
          return f"Error in calculation: {e}"

  llm = OpenAI(temperature=0)

  tools = [
      Tool(name="Search", func=search_tool, description="Search the web"),
      Tool(name="Calculator", func=calculator_tool, description="Perform calculations")
  ]

  agent = initialize_agent(tools, llm, agent_type="react")
  response = agent.run("What is the population of France divided by the area of France?")
  print(response)
  ```

### 3. **Self-Reflection with Search**

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



### 4. **Plan-and-Execute Agent**

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


### 5. **Tool-Augmented Agent (Function Calling)**

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
---

## 🛠️ Hands-On Lab: Building a Tool-Using Support Agent

[Build an Agent using File Search Tool](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/examples/example-assistant-search?pivots=programming-language-python)

---

## 🔗 Resources

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
