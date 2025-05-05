# Chapter: GenAI - Parameters (Temperature, top_k, top_p, etc.)

## Introduction

Generative AI models use adjustable parameters to control the nature, diversity, and quality of their outputs. This chapter explores how parameters like `temperature`, `top_k`, `top_p`, and others influence a model's behavior, helping you optimize for creativity, precision, or stability.

---

## **Overview of Generation Parameters**

### **1. What are Generation Parameters?**
- **Definition**: Generation parameters define how AI models determine which words or tokens to select from their predictions during text generation.  
- **Core Idea**: They control randomness, creativity, and likelihood of responses.  

### **2. Why Do Parameters Matter?**
- **Impact**:  
  - Parameters affect text style, coherence, diversity, and accuracy.  
  - Selecting appropriate values ensures outputs match your project goals.  
- **Use Cases**:  
  - High creativity tasks like storytelling → More randomness.  
  - Precise tasks like summarization → Less randomness.

---

## **Key Parameters Explained**

### **1. Temperature**
- **Definition**: Temperature adjusts the randomness of the model's output by controlling token probabilities.  
- **Behavior**:  
  - Higher values (`1.0` or above): Increase randomness → More creative outputs.  
  - Lower values (`0.1` or near zero): Decrease randomness → Precise and deterministic outputs.  
- **Examples**:  
  - **High Temperature (Creative)**:  
    Input: *"Write a poem about the sunset."*  
    Temperature: `1.0`.  
    Output:  
    *"The sun fell tenderly, kissing the ocean's waves, a fiery bundle dissipating into shadows of the night."*  

  - **Low Temperature (Precise)**:  
    Input: *"Describe the sunset in one sentence."*  
    Temperature: `0.2`.  
    Output:  
    *"The sun sets over the horizon with hues of red and orange across the sky."*

- **When to Adjust Temperature**:  
  - Creative tasks: Use `0.8–1.5`.  
  - Factual tasks: Use `0.1–0.3`.

---

### **2. Top-k Sampling**
- **Definition**: Limits the model’s token selection to the top `k` most likely candidates.  
- **Behavior**:  
  - Higher `k` values: Allow wider diversity → Unexpected but interesting outputs.  
  - Lower `k` values: Narrow selection → Safer, more predictable responses.  
- **Examples**:  
  - **Top-k = 5 (More Diversity)**:  
    Input: *"Suggest colors for a tropical-themed living room."*  
    Top-k: `5`.  
    Output:  
    *"Try teal, coral pink, vibrant yellow, lime green, or aquamarine."*  

  - **Top-k = 1 (Restricted Diversity)**:  
    Input: *"Suggest colors for a tropical-themed living room."*  
    Top-k: `1`.  
    Output:  
    *"Teal."*  

- **When to Adjust Top-k**:  
  - Creative scenarios: Use `20–100`.  
  - Precise or repetitive tasks: Use `5–10`.

---

### **3. Top-p Sampling (Nucleus Sampling)**  
- **Definition**: Instead of limiting by `k`, `top-p` considers tokens with a cumulative probability `p`. Tokens are sampled until their combined likelihood reaches `p`.  
- **Behavior**:  
  - Lower `p` values (e.g., `0.2`): Force narrower token ranges.  
  - Higher `p` values (e.g., `0.9`): Allow broader token ranges.  

- **Examples**:  
  - **Top-p = 0.9 (Creative)**:  
    Input: *"Write an imaginative product description for a futuristic flying car."*  
    Top-p: `0.9`.  
    Output:  
    *"The SkyCruiser 3000 glides effortlessly like a bird, blending sleek edges, an AI navigation system, and zero-carbon propulsion for urban adventures."*  

  - **Top-p = 0.5 (Focused)**:  
    Input: *"Write an imaginative product description for a futuristic flying car."*  
    Top-p: `0.5`.  
    Output:  
    *"The SkyCruiser 3000 is a revolutionary transportation device for urban professionals."*  

- **When to Adjust Top-p**:  
  - For controlled creativity: Use `0.7–0.9`.  
  - For focused tasks: Use `0.3–0.5`.

---

### **4. Frequency and Presence Penalty**  
- **Definitions**:  
  - **Frequency Penalty**: Penalizes tokens repeated frequently to reduce redundancy.  
  - **Presence Penalty**: Penalizes tokens appearing early in the text to encourage variety.  

- **Examples**:  
  - **No Penalty (Default)**:  
    Input: *"What are popular programming languages?"*  
    Output:  
    *"Python, JavaScript, Python, Python."*  

  - **Frequency Penalty (Reduced Repeat)**:  
    Input: *"What are popular programming languages?"*  
    Frequency Penalty: `0.5`.  
    Output:  
    *"Python, JavaScript, Java, C++."*  

  - **Presence Penalty (Encourage Novelty)**:  
    Input: *"What are trending tech topics?"*  
    Presence Penalty: `0.5`.  
    Output:  
    *"AI innovations, robotics, blockchain, green energy solutions."*  

---

## **Parameter Interaction**

### **Adjusting Multiple Parameters Together**  
- Parameters can be used in combination for tailored output control.  
  - **Example**:  
    - Temperature: `0.7`.  
    - Top-p: `0.8`.  
    - Frequency Penalty: `0.3`.  
  - Input: *"Write a short story about a lonely robot."*  
    Output:  
    *"Rusty sat quietly by the cliff’s edge, scanning the horizon for signs of a friend, hoping the wind would carry company his way. Days passed, yet hope lingered like an unrelenting song."*

---

## **When to Use Parameters**

1. **Creative Tasks**:  
   - Writing stories or poetry → High temperature (`0.8–1.2`) + Top-p (`0.9`).  

2. **Analytical Tasks**:  
   - Summarizing articles → Low temperature (`0.1–0.3`) + Top-p (`0.5–0.7`).  

3. **Predictable Tasks**:  
   - Fact-based queries → Low temperature (`0.1`) + Top-k (`1`).  

---

## **Best Practices**

### **1. Start with Defaults**  
- Begin with standard API values (e.g., Temperature = `0.7`, Top-p = `0.8`) before modifying.  

### **2. Experiment Iteratively**  
- Test different combinations to fine-tune the output style. Use the results to identify optimal params.  

### **3. Assess Output Quality**  
- Evaluate the output’s relevance, coherence, and creativity based on your task requirements.  

### **4. Document Parameter Configurations**  
- Keep track of tested parameter setups for reproducibility.  
  - Example:  
    ```plaintext
    Task: Summarization  
    Temperature: 0.2  
    Top-p: 0.5  
    Frequency Penalty: 0.4  
    Success rate: 90%  
    ```

---

## **Learning Resources**

### **1. Tutorials**  
- OpenAI Guide on Sampling:  
  [https://platform.openai.com/docs/sample-gen-parameters](https://platform.openai.com/docs/sample-gen-parameters)  

### **2. Courses**  
- **Deep Learning Specialization** by Andrew Ng: Learn probability-based sampling techniques in NLP.  
  [https://www.coursera.org/specializations/deep-learning](https://www.coursera.org/specializations/deep-learning)

---

## **Conclusion**

Control over generative AI parameters like `temperature`, `top_k`, and `top_p` is critical for tailoring outputs to fit specific use cases. By understanding their mechanics and interactions, you can optimize model behaviors to balance creativity, precision, and predictability effectively.
