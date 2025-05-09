# 🧩 **Chapter 7: Scaling and Infrastructure Design**

### 🎯 Learning Objectives:
By the end of this module, learners will be able to:
- Design scalable infrastructure for GenAI services using cloud-native tools
- Apply performance and cost optimizations (token usage, caching, streaming)
- Use containerization and autoscaling to handle variable workloads
- Implement fallback strategies and observability for high-availability

---

### 📌 Topics Covered

#### 7.1 Scaling Challenges in GenAI Systems

| Challenge                         | Description |
|----------------------------------|-------------|
| **Token-based Pricing**          | Cost increases linearly with token volume |
| **Cold Starts in Serverless**    | Latency spikes on first request or during scale-up |
| **Context Limit Bottlenecks**    | LLMs have token limits (e.g., 8k, 17k, 128k) |
| **High-Latency Tool Chains**     | Multiple chained calls (RAG, planner, memory) increase round-trip time |
| **Non-deterministic Responses**  | Results vary per invocation, complicating caching |

---

#### 7.2 Infrastructure Models

| Model                  | When to Use | Tools |
|------------------------|-------------|-------|
| **Serverless Functions** | Low-throughput or bursty traffic | Azure Functions, AWS Lambda |
| **Containerized APIs**  | Moderate throughput, stable traffic | Azure Container Apps, AWS ECS |
| **Kubernetes (K8s)**    | High-scale, multi-service orchestration | AKS, EKS, GKE |
| **Edge Inference**      | Latency-sensitive apps (e.g., mobile) | NVIDIA Triton, ONNX, Hugging Face Transformers on device |

---

### 🏗️ Reference Architecture

```text
User → API Gateway → GenAI Inference Service
                         ↓
                Retrieval (Vector DB)
                         ↓
              Caching Layer (Redis)
                         ↓
               Logging + Monitoring (App Insights, Prometheus)
```

---

### 🧠 Key Design Techniques

#### 1. **Token Optimization**
- Limit prompt verbosity and use summarization
- Use truncation for memory/context windows
- Avoid unnecessary tool calls

#### 2. **Streaming Responses**
- Use `stream=True` in OpenAI/Anthropic APIs
- Improves perceived performance
```python
response = openai.ChatCompletion.create(
    stream=True,
    model="gpt-4",
    messages=[...]
)
for chunk in response:
    print(chunk['choices'][0]['delta'].get('content', ''), end="")
```

#### 3. **Caching & Deduplication**
- Use Redis to store:
  - Repeated prompts and completions
  - Frequently accessed document chunks
  - Session metadata

#### 4. **Fallback Models**
- Set up routing logic:
```python
try:
    response = call_openai()
except RateLimitError:
    response = call_anthropic()
```

---

### 🛠️ Tools for Scaling

| Functionality | Tools |
|---------------|-------|
| **Caching**   | Redis, Azure Cache for Redis |
| **Autoscaling** | Azure Container Apps (KEDA), AKS Horizontal Pod Autoscaler |
| **Load Balancing** | Azure Front Door, NGINX, Envoy |
| **Monitoring & Logs** | Azure Monitor, App Insights, Grafana, OpenTelemetry |
| **API Management** | Azure API Management, Kong, Tyk |

---

### 🧪 Hands-On Lab: Deploy Scalable GenAI API on Azure Container Apps

**Goal:**  
Deploy a containerized OpenAI-powered summarization service that supports streaming and caching.

**Steps:**

1. **Create FastAPI container**
```bash
pip install fastapi uvicorn openai redis
```

```python
# app.py
from fastapi import FastAPI
from redis import Redis
import openai

openai.api_key = "your-api-key"
redis_client = Redis(host="redis-host", port=6379)

app = FastAPI()

@app.get("/summarize")
def summarize(text: str):
    if redis_client.get(text):
        return {"summary": redis_client.get(text).decode()}

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    )
    summary = response['choices'][0]['message']['content']
    redis_client.set(text, summary)
    return {"summary": summary}
```

2. **Dockerize**
```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
```

3. **Deploy to Azure Container Apps**
```bash
az containerapp up \
  --name genai-summarizer \
  --source . \
  --resource-group your-rg \
  --location your-location
```

---

### 📘 Resources
- [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/)
- [KEDA Autoscaler](https://keda.sh/)
- [OpenAI Streaming Guide](https://platform.openai.com/docs/guides/text-generation/streaming)
- [Redis for Caching](https://redis.io/docs/getting-started/)

---

### ⚖️ Trade-offs and Challenges

| Decision Area | Trade-off |
|---------------|-----------|
| **Streaming vs Non-streaming** | Better UX vs harder UI implementation |
| **Serverless vs Containers** | Cheap at low traffic vs consistent performance |
| **Multi-provider fallback** | Resilience vs increased code complexity |
| **Autoscaling** | Needs observability + custom metrics tuning |

---

### ✅ Check Your Understanding

- How does Redis help in GenAI systems?
- What’s the difference between container-based vs serverless deployment for LLMs?
- Why is token optimization critical in cost-sensitive deployments?