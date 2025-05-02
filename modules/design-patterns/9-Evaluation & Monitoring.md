# 🧩 **Chapter 9: Evaluation & Monitoring**

### 🎯 Learning Objectives:
By the end of this module, learners will be able to:
- Define appropriate evaluation metrics for GenAI outputs (e.g., accuracy, relevance, toxicity)
- Track and visualize usage, cost, latency, and response quality
- Implement continuous evaluation pipelines for prompt and model tuning
- Use observability tools (e.g., PromptFlow, LangSmith, Azure Monitor) to gain insights

---

### 📌 Topics Covered

#### 9.1 Why Evaluate GenAI Outputs?

LLMs are **non-deterministic** — the same prompt can produce different results. So we must evaluate for:
- **Correctness**: factual accuracy
- **Relevance**: context matching
- **Coherence**: logical flow and tone
- **Toxicity/Safety**: inappropriate or biased responses
- **Latency & Cost**: performance and operational efficiency

---

#### 9.2 Evaluation Dimensions

| Dimension         | Example Metric             | Tools                         |
|------------------|----------------------------|-------------------------------|
| **Quality**       | BLEU, ROUGE, semantic similarity | Azure Eval API, LangChain Eval |
| **Latency**       | Time to first token, response duration | App Insights, Prometheus     |
| **Cost**          | Tokens per call, $/completion       | Custom logging, OpenAI usage reports |
| **User Feedback** | Thumbs up/down, comments    | Feedback widgets, log enrichment |
| **Prompt Robustness** | Variation across re-prompts  | PromptFlow, LangSmith         |

---

#### 9.3 Evaluation Techniques

- **Static Evaluation**: Predefined inputs → expected outputs (e.g., summarization, classification)
- **Dynamic Evaluation**: Real user input logged and reviewed periodically
- **Human-in-the-Loop (HITL)**: Review queue, scoring, feedback
- **Model-vs-Model**: Use one model to judge another's output

---

#### 9.4 Tools for Evaluation

| Tool              | Description                                      |
|------------------|--------------------------------------------------|
| **PromptFlow (Azure)** | Prompt versioning, evaluation, logging, feedback |
| **LangSmith**     | Trace visualization, eval agents, retry chains  |
| **OpenAI Usage Logs** | Token counts, model usage per endpoint      |
| **App Insights**  | End-to-end telemetry for latency, errors, tracing |
| **HumanLoop / Evals** | Review, rank, or approve model outputs       |

---

### 🔍 Example: Semantic Similarity Scoring with OpenAI Embeddings

```python
from openai.embeddings_utils import cosine_similarity, get_embedding

truth = "The capital of France is Paris."
response = "Paris is the capital of France."

score = cosine_similarity(get_embedding(response), get_embedding(truth))
```

- **High cosine similarity** → good factual alignment
- Automate this across datasets to detect regressions

---

### 🧪 Hands-On Lab: Evaluate a Q&A Bot Using PromptFlow

**Goal:**  
Track and visualize performance of a document-based Q&A bot using Azure PromptFlow.

**Steps:**

1. **Install PromptFlow CLI**
```bash
pip install promptflow
```

2. **Create Evaluation Pipeline**
```yaml
# eval_pipeline.yaml
inputs:
  - question: "What’s the refund policy?"
  - document: "Refunds are given if returned in 30 days."
eval:
  - metric: semantic_similarity
    reference_field: "expected"
    response_field: "generated"
```

3. **Run and visualize results**
```bash
promptflow run --entry eval_pipeline.yaml --input data.csv --output results.json
```

4. **Review logs in Azure AI Studio**

---

#### 9.5 Logging and Monitoring

**Metrics to track:**
- Input/output size (tokens)
- Latency by endpoint
- Number of retries
- Failure modes (timeouts, validation failures)
- Unsafe responses flagged

**Azure Example:**
```python
from opencensus.ext.azure.log_exporter import AzureLogHandler
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string="InstrumentationKey=..."))
logger.warning("Prompt took 3.4s with 84 tokens")
```

---

### ⚖️ Trade-offs and Challenges

| Challenge           | Consideration |
|---------------------|---------------|
| Manual eval is costly | Use automation + HITL selectively |
| Quality scoring is subjective | Use consistent rubric or embeddings |
| Cost tracking may lag | Set soft and hard quotas per user/model |
| Tracing tools can expose PII | Anonymize or mask logs before indexing |

---

### 📘 Resources

- [Azure PromptFlow](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview)
- [LangSmith](https://smith.langchain.com/)
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- [OpenAI Usage Dashboard](https://platform.openai.com/account/usage)

---

### ✅ Check Your Understanding

- Why is semantic evaluation preferred over keyword matching in GenAI?
- What are the pros/cons of human vs automatic evaluation?
- How can you use metrics to inform model switching or prompt tuning?

---

✅ This concludes the core modules.

Would you now like help structuring the **Capstone Project**, or should we generate:
- Slide decks for each module
- Labs as downloadable notebooks/scripts
- Certification exam-style questions per module?