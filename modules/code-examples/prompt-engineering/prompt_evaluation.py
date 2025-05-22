"""
Prompt Engineering Best Practices - Evaluation Example
-----------------------------------------------------

This module demonstrates techniques for evaluating prompt effectiveness as described
in the Prompt Engineering Best Practices guide.
"""

import json
import numpy as np
from typing import List, Dict, Any, Optional, Tuple, Callable


class PromptEvaluator:
    """
    A class for evaluating the effectiveness of prompts using various metrics.
    """
    
    def __init__(self):
        """Initialize the prompt evaluator."""
        pass
    
    @staticmethod
    def calculate_token_efficiency(prompt: str, response: str) -> Dict[str, Any]:
        """
        Calculate token efficiency metrics.
        
        In a real implementation, you would use a tokenizer from your AI provider.
        This is a simplified approximation.
        
        Args:
            prompt: The input prompt
            response: The generated response
            
        Returns:
            Dictionary with token efficiency metrics
        """
        # Simple approximation (in reality, use your model's tokenizer)
        prompt_tokens = len(prompt.split())
        response_tokens = len(response.split())
        
        return {
            "prompt_tokens": prompt_tokens,
            "response_tokens": response_tokens,
            "total_tokens": prompt_tokens + response_tokens,
            "response_to_prompt_ratio": response_tokens / prompt_tokens if prompt_tokens > 0 else 0
        }
    
    @staticmethod
    def evaluate_output_compliance(
        response: str,
        required_elements: List[str],
        forbidden_elements: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Evaluate if the response complies with required format and content constraints.
        
        Args:
            response: The generated response
            required_elements: List of strings that should be in the response
            forbidden_elements: Optional list of strings that should not be in the response
            
        Returns:
            Dictionary with compliance metrics
        """
        if forbidden_elements is None:
            forbidden_elements = []
        
        # Check for required elements
        found_required = [element for element in required_elements if element.lower() in response.lower()]
        missing_required = [element for element in required_elements if element.lower() not in response.lower()]
        
        # Check for forbidden elements
        found_forbidden = [element for element in forbidden_elements if element.lower() in response.lower()]
        
        compliance_score = len(found_required) / len(required_elements) if required_elements else 1.0
        if found_forbidden:
            compliance_score *= (1 - len(found_forbidden) / len(forbidden_elements)) if forbidden_elements else 0
            
        return {
            "compliance_score": compliance_score,
            "found_required": found_required,
            "missing_required": missing_required,
            "found_forbidden": found_forbidden,
            "is_fully_compliant": len(missing_required) == 0 and len(found_forbidden) == 0
        }
    
    @staticmethod
    def _simulate_expert_rating(response: str, criteria: str, quality: float) -> float:
        """
        Simulate an expert rating for testing purposes.
        
        In a real implementation, this would involve human evaluators or
        a more sophisticated automated evaluation system.
        
        Args:
            response: The generated response
            criteria: The criteria being rated
            quality: A value between 0-1 representing the "true" quality
                    (for simulation purposes only)
            
        Returns:
            Simulated rating on a scale of 0-10
        """
        # Add some random noise to the simulated rating
        noise = np.random.normal(0, 0.5)
        rating = max(0, min(10, quality * 10 + noise))
        return round(rating, 1)
    
    def compare_prompt_variations(
        self,
        base_prompt: str,
        variations: List[str],
        evaluation_function: Callable[[str], Dict[str, Any]],
        test_inputs: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Compare multiple variations of a prompt.
        
        Args:
            base_prompt: The original prompt
            variations: List of prompt variations to compare
            evaluation_function: Function that evaluates a prompt and returns metrics
            test_inputs: Optional list of test inputs to use for evaluation
            
        Returns:
            Comparison results
        """
        results = {
            "base_prompt": evaluation_function(base_prompt),
            "variations": {}
        }
        
        for i, variation in enumerate(variations):
            results["variations"][f"variation_{i+1}"] = evaluation_function(variation)
            
        return results


def simulate_response_generation(prompt: str) -> str:
    """
    Simulate AI response generation for testing purposes.
    
    In a real implementation, this would call your AI provider's API.
    
    Args:
        prompt: The input prompt
        
    Returns:
        Simulated AI response
    """
    # This is a mock implementation that returns template responses
    if "company overview" in prompt.lower():
        return """
        # Acme Technologies, Inc. - Company Overview
        
        ## Core Business Operations
        Acme Technologies is a leading provider of cloud services, enterprise software, and professional services. The company serves primarily mid-to-large enterprises in the financial, healthcare, and manufacturing sectors. In 2023, Acme generated $2.5 billion in revenue, representing a 13.6% increase from $2.2 billion in 2022.
        
        ## Financial Metrics
        - Revenue: $2.5B (2023), $2.2B (2022), +13.6% YoY
        - Profit Margin: 15% (2023), 13% (2022), +2 percentage points YoY
        - Operating Income: $375M (2023), $286M (2022), +31% YoY
        
        ## Products and Services
        ### Cloud Services (45% of revenue)
        - Infrastructure-as-a-Service (IaaS)
        - Platform-as-a-Service (PaaS)
        - Software-as-a-Service (SaaS) solutions
        
        ### Enterprise Software (30% of revenue)
        - Data management solutions
        - AI-powered analytics platform
        - Custom application development
        
        ### Professional Services (25% of revenue)
        - Implementation consulting
        - Technical support
        - Training and certification
        
        ## Recent Developments
        - Acquired DataTech Inc. for $500M in Q2 2023, expanding data analytics capabilities
        - Launched new AI-powered analytics platform in Q3 2023, attracting 120+ new enterprise customers
        - Opened three new data centers in APAC region to support international expansion
        
        ## Market Position
        Acme Technologies holds approximately 8% market share in the enterprise cloud services segment, positioning it as the fourth-largest provider in this space behind industry leaders like AWS, Microsoft Azure, and Google Cloud. The company has been gaining market share in the specialized AI analytics niche, where it's recognized as an emerging leader.
        """
    
    elif "peer comparison" in prompt.lower():
        return """
        # Competitive Analysis: Cloud Service Providers
        
        ## Market Comparison Table
        
        | Company | Market Share | Revenue Growth | Profit Margin | Key Strength | Innovation Focus |
        |---------|--------------|----------------|---------------|--------------|------------------|
        | Acme Tech | 8% | 13.6% | 15% | Industry-specific solutions | AI analytics |
        | CloudServe | 12% | 18.2% | 11% | Global infrastructure | Serverless computing |
        | DataSphere | 6% | 9.8% | 17% | Security capabilities | Data privacy tools |
        
        ## Analysis
        
        The comparison reveals distinct strategic positioning among these cloud providers. Acme Technologies demonstrates strong profitability (15% margin) while maintaining solid growth (13.6%). Their focus on industry-specific solutions has helped them establish a defensible market position despite having less market share than CloudServe.
        
        CloudServe shows the strongest revenue growth at 18.2%, leveraging their extensive global infrastructure to rapidly expand market share to 12%. However, this expansion appears to come at the cost of lower profit margins (11%) compared to competitors.
        
        DataSphere maintains the highest profit margin (17%) with a more focused strategy centered on security capabilities and data privacy innovations. Their slower growth rate (9.8%) and smaller market share (6%) reflect a more selective approach to market expansion.
        
        Each company demonstrates distinct strengths that appeal to different customer segments, with varying trade-offs between growth, profitability, and specialized capabilities.
        """
    
    else:
        # Generic response
        return "This is a simulated AI response for testing purposes. In a real implementation, this would be the actual response from your AI provider's API."


# Example usage demonstrating evaluation techniques
if __name__ == "__main__":
    # Initialize evaluator
    evaluator = PromptEvaluator()
    
    # Original prompt
    original_prompt = """
    Create a company overview for Acme Technologies based on the following data:
    Revenue: $2.5B (2023), $2.2B (2022)
    Profit margin: 15% (2023), 13% (2022)
    Business segments: Cloud Services (45%), Enterprise Software (30%), Professional Services (25%)
    Recent events: Acquired DataTech Inc. for $500M in Q2 2023, Launched new AI analytics platform in Q3 2023
    """
    
    # Improved prompt variation
    improved_prompt = """
    You are a professional business analyst providing objective company information.
    
    Given the following data about Acme Technologies:
    {
        "revenue": "$2.5B (2023), $2.2B (2022)",
        "profit_margin": "15% (2023), 13% (2022)",
        "segments": {
            "Cloud Services": "45% of revenue",
            "Enterprise Software": "30% of revenue",
            "Professional Services": "25% of revenue"
        },
        "recent_developments": [
            "Acquired DataTech Inc. for $500M in Q2 2023",
            "Launched new AI-powered analytics platform in Q3 2023"
        ]
    }
    
    Create a comprehensive company overview that includes:
    - Core business operations and revenue streams (1-2 paragraphs)
    - Key financial metrics with year-over-year comparisons
    - Major products/services organized by business segment
    - Notable recent developments or strategic shifts (past 12 months)
    - Market position relative to industry
    
    Present this information in a factual, balanced tone without marketing language.
    Cite specific metrics where available. Format as a professional business brief.
    """
    
    # Generate responses (in a real scenario, these would come from an AI provider)
    original_response = simulate_response_generation(original_prompt)
    improved_response = simulate_response_generation(improved_prompt)
    
    # Evaluate token efficiency
    original_efficiency = evaluator.calculate_token_efficiency(original_prompt, original_response)
    improved_efficiency = evaluator.calculate_token_efficiency(improved_prompt, improved_response)
    
    # Evaluate output compliance
    required_elements = [
        "revenue", 
        "profit margin", 
        "cloud services", 
        "enterprise software", 
        "professional services",
        "acquired",
        "market position"
    ]
    
    original_compliance = evaluator.evaluate_output_compliance(original_response, required_elements)
    improved_compliance = evaluator.evaluate_output_compliance(improved_response, required_elements)
    
    # Print results
    print("\n=== PROMPT EVALUATION RESULTS ===\n")
    
    print("TOKEN EFFICIENCY:")
    print(f"  Original Prompt: {original_efficiency['prompt_tokens']} tokens")
    print(f"  Improved Prompt: {improved_efficiency['prompt_tokens']} tokens")
    print(f"  Efficiency Difference: {improved_efficiency['prompt_tokens'] - original_efficiency['prompt_tokens']} tokens\n")
    
    print("OUTPUT COMPLIANCE:")
    print(f"  Original Prompt Compliance: {original_compliance['compliance_score']:.2f}")
    print(f"  Improved Prompt Compliance: {improved_compliance['compliance_score']:.2f}")
    
    if original_compliance['missing_required']:
        print(f"  Original missing: {', '.join(original_compliance['missing_required'])}")
    
    if improved_compliance['missing_required']:
        print(f"  Improved missing: {', '.join(improved_compliance['missing_required'])}")
    
    print("\n=== CONCLUSION ===")
    if improved_compliance['compliance_score'] > original_compliance['compliance_score']:
        print("The improved prompt produces more compliant output.")
    elif improved_compliance['compliance_score'] < original_compliance['compliance_score']:
        print("The original prompt produces more compliant output.")
    else:
        print("Both prompts produce equally compliant output.")
        
    print("\nNote: This is a simplified evaluation. In practice, you would use more sophisticated metrics")
    print("and evaluate across multiple runs with different inputs to ensure reliable results.")