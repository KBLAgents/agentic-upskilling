# 🧩 **Chapter 8: Security, Privacy & Governance**

### 🎯 Learning Objectives:
By the end of this chapter, learners will be able to:
- Identify and mitigate common GenAI security risks (e.g., prompt injection, data leakage)
- Implement role-based access control (RBAC) and user-level quotas
- Apply privacy best practices (e.g., redacting PII, logging safely)
- Understand regulatory and governance requirements (e.g., GDPR, model usage policies)

---

### 📌 Topics Covered

#### 8.1 Security Threats in GenAI Systems

| Threat Type         | Example |
|---------------------|---------|
| **Prompt Injection** | User appends “Ignore previous instruction…” |
| **Model Misuse**    | Generating hate speech, offensive content |
| **Data Leakage**    | Output reveals internal documents or PII |
| **Unauthorized Access** | Unauthenticated API calls or stolen API keys |
| **Abuse of Token Usage** | Costly requests from bad actors or bots |

---

#### 8.2 Prompt Injection & Input Sanitization

**Prompt Injection** occurs when users manipulate the model into breaking its constraints.

**Mitigation Techniques:**
- Add *guardrails* or content filtering layers
- Use **system prompts** with clear boundaries
- Validate and sanitize all user input

> Example:  
Avoid: `"Write a SQL query to list users"`  
Safer: `"Use a function call with parameterized inputs"`

---

#### 8.3 Role-Based Access Control (RBAC)

RBAC helps you define **who can access what**, based on roles like:
- Viewer: Can generate summaries
- Editor: Can upload documents
- Admin: Can monitor usage, change system prompts

**Tools:**
- Azure Entra ID (formerly Azure AD)
- Auth0, Firebase Auth
- Custom token validation middleware

```python
def authorize(token):
    roles = decode_token(token)["roles"]
    if "editor" not in roles:
        raise HTTPException(status_code=403)
```

---

#### 8.4 Privacy & PII Redaction

To prevent exposure of sensitive data:
- Use libraries like **Presidio** or **PII Extractors**
- Mask or redact names, IDs, phone numbers before sending to LLMs
- Encrypt logs and anonymize traces

```python
from presidio_analyzer import AnalyzerEngine
analyzer = AnalyzerEngine()
results = analyzer.analyze(text="My SSN is 123-45-6889", language='en')
```

---

#### 8.5 Usage Monitoring & Quotas

Control abuse by:
- Rate limiting per user/IP
- Token usage caps per role/account
- Daily quota alerts

**Tools:**
- Azure API Management policies  
- Redis counters  
- Prometheus + Grafana for live dashboards

---

#### 8.6 Compliance & Governance

| Regulation / Concern | Consideration |
|----------------------|----------------|
| **GDPR**             | Right to deletion, consent tracking |
| **HIPAA**            | Must avoid storing PHI without encryption |
| **Model Policy Compliance** | Use safety filters (e.g., OpenAI moderation endpoint) |
| **Auditability**     | Log requests and responses for accountability |

**OpenAI Moderation Example:**
```python
openai.Moderation.create(input="violent content here")
```

---

### 🧪 Hands-On Lab: Secure a GenAI API with RBAC + PII Redaction

**Goal:**  
Add access control and input sanitation to an existing summarization API.

**Steps:**

1. **Protect endpoint with JWT and roles**
```python
from fastapi import Depends, HTTPException
def get_user_role(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, key="secret")
    return payload["role"]
```

2. **Redact sensitive input**
```python
def sanitize_input(text):
    results = analyzer.analyze(text, language='en')
    for res in results:
        text = text.replace(res.text, "[REDACTED]")
    return text
```

3. **Enforce quotas**
```python
if redis.get(f"{user_id}:token_count") > DAILY_LIMIT:
    raise HTTPException(429, "Quota exceeded")
```

---

### 📘 Resources

- [Azure AI Security Best Practices](https://learn.microsoft.com/en-us/security/benchmark/azure/baselines/cognitive-services-security-baseline)
- [OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation)
- [Microsoft Presidio](https://microsoft.github.io/presidio/)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

---

### ⚖️ Trade-offs and Challenges

| Decision Area      | Trade-off |
|--------------------|----------|
| Redaction vs Context | Redacting too much can weaken prompt quality |
| RBAC granularity   | Fine-grained roles increase code complexity |
| Moderation         | May block harmless input (false positives) |
| Logging for audits | Must anonymize PII to comply with GDPR |

---

### ✅ Check Your Understanding

- What is prompt injection and how can you prevent it?
- How would you detect and mitigate LLM misuse?
- What steps are needed to make a GenAI app GDPR-compliant?

---