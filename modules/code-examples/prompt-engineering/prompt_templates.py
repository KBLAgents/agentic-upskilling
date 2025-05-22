"""
Prompt Engineering Best Practices - Example Implementation
---------------------------------------------------------

This module demonstrates the implementation of prompt templating and management
techniques described in the Prompt Engineering Best Practices guide.
"""

import os
import json
import datetime
from typing import Dict, List, Any, Optional, Union


class PromptTemplate:
    """
    A class for managing and versioning prompt templates with parameter substitution.
    """
    
    def __init__(self, template: str, metadata: Optional[Dict[str, Any]] = None):
        """
        Initialize a prompt template.
        
        Args:
            template: The template string with placeholders for parameters
            metadata: Optional metadata about the template (version, author, etc.)
        """
        self.template = template
        self.metadata = metadata or {
            "version": "1.0.0",
            "created_at": datetime.datetime.now().isoformat(),
            "author": "AI Team",
            "description": "Generic prompt template"
        }
    
    def format(self, **kwargs) -> str:
        """
        Format the template by substituting parameters.
        
        Args:
            **kwargs: Key-value pairs for parameter substitution
        
        Returns:
            The formatted prompt string
        """
        try:
            return self.template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required parameter: {e}")
    
    def save(self, path: str) -> None:
        """
        Save the template to a file with its metadata.
        
        Args:
            path: The file path to save the template
        """
        with open(path, 'w') as f:
            json.dump({
                "template": self.template,
                "metadata": self.metadata
            }, f, indent=2)
    
    @classmethod
    def load(cls, path: str) -> 'PromptTemplate':
        """
        Load a template from a file.
        
        Args:
            path: The file path to load the template from
        
        Returns:
            A PromptTemplate instance
        """
        with open(path, 'r') as f:
            data = json.load(f)
        return cls(template=data["template"], metadata=data["metadata"])


class PromptLibrary:
    """
    A library for managing multiple prompt templates organized by category and purpose.
    """
    
    def __init__(self, library_path: Optional[str] = None):
        """
        Initialize the prompt library.
        
        Args:
            library_path: Optional path to a directory containing prompt templates
        """
        self.templates = {}
        if library_path and os.path.exists(library_path):
            self._load_from_directory(library_path)
    
    def _load_from_directory(self, directory: str) -> None:
        """
        Load templates from a directory structure.
        
        Args:
            directory: Path to directory containing prompt templates
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.json'):
                    path = os.path.join(root, file)
                    relative_path = os.path.relpath(path, directory)
                    category_path = os.path.dirname(relative_path).replace(os.sep, '.')
                    template_name = os.path.splitext(os.path.basename(file))[0]
                    
                    # Create nested dictionary structure based on directory path
                    current = self.templates
                    if category_path and category_path != '.':
                        for category in category_path.split('.'):
                            if category not in current:
                                current[category] = {}
                            current = current[category]
                    
                    # Load the template
                    current[template_name] = PromptTemplate.load(path)
    
    def get_template(self, template_path: str) -> PromptTemplate:
        """
        Get a template by its path in the library.
        
        Args:
            template_path: Path to the template (e.g., "financial.company_overview")
        
        Returns:
            The prompt template
            
        Raises:
            KeyError: If the template path doesn't exist
        """
        current = self.templates
        for part in template_path.split('.'):
            current = current[part]
        
        if not isinstance(current, PromptTemplate):
            raise KeyError(f"Path '{template_path}' does not lead to a template")
        
        return current
    
    def add_template(self, template_path: str, template: PromptTemplate) -> None:
        """
        Add a template to the library.
        
        Args:
            template_path: Path where the template should be stored
            template: The prompt template to add
        """
        parts = template_path.split('.')
        current = self.templates
        
        # Navigate to the right location in the nested dictionary
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        
        # Add the template
        current[parts[-1]] = template
    
    def save_library(self, directory: str) -> None:
        """
        Save the entire library to a directory structure.
        
        Args:
            directory: Directory to save the library to
        """
        os.makedirs(directory, exist_ok=True)
        self._save_category(self.templates, directory, [])
    
    def _save_category(self, category: Dict, base_dir: str, path_parts: List[str]) -> None:
        """
        Recursively save a category and its templates.
        
        Args:
            category: Dictionary of templates or subcategories
            base_dir: Base directory for the library
            path_parts: Current path parts in the category hierarchy
        """
        current_dir = os.path.join(base_dir, *path_parts)
        os.makedirs(current_dir, exist_ok=True)
        
        for key, value in category.items():
            if isinstance(value, PromptTemplate):
                # Save template
                file_path = os.path.join(current_dir, f"{key}.json")
                value.save(file_path)
            else:
                # Recurse into subcategory
                self._save_category(value, base_dir, path_parts + [key])


# Example usage

# 1. Company Overview Template
company_overview_template = PromptTemplate(
    template="""
You are a professional business analyst providing objective company information.

Given the following data about {company_name}:
{company_data}

Create a comprehensive company overview that includes:
- Core business operations and revenue streams (1-2 paragraphs)
- Key financial metrics with year-over-year comparisons
- Major products/services organized by business segment
- Notable recent developments or strategic shifts (past 12 months)
- Market position relative to industry

Present this information in a factual, balanced tone without marketing language.
Cite specific metrics where available. Format as a professional business brief.
""",
    metadata={
        "version": "1.2.1",
        "author": "Financial Analysis Team",
        "description": "Generates comprehensive company overviews for financial analysis",
        "use_case": "company_analysis",
        "parameters": {
            "company_name": "Name of the company to analyze",
            "company_data": "JSON object containing financial and operational data"
        },
        "version_history": [
            {"version": "1.0.0", "changes": "Initial version"},
            {"version": "1.1.0", "changes": "Added market position section"},
            {"version": "1.2.0", "changes": "Improved financial metrics formatting"},
            {"version": "1.2.1", "changes": "Added guidance for handling missing financial data"}
        ]
    }
)

# 2. Peer Comparison Template with Few-Shot Examples
peer_comparison_template = PromptTemplate(
    template="""
You are a market research analyst conducting comparative analysis.

Compare the following companies: {company_list} based on the data provided:
{companies_data}

Create a balanced comparison focusing on:
- Market share and competitive positioning
- Financial performance (revenue, profit margins, growth rates)
- Product/service portfolio strengths and weaknesses
- Strategic initiatives and innovation focus
- Key differentiators between each company

Format as a comparison table followed by 2-3 paragraphs of analytical insights.
Maintain objectivity by supporting claims with specific metrics where available.
Avoid making judgments about which company is "better" overall.

Examples of well-formatted comparisons:

Example 1:
{example_comparison}
""",
    metadata={
        "version": "2.0.0",
        "author": "Competitive Analysis Team",
        "description": "Generates peer comparisons between multiple companies",
        "use_case": "competitive_analysis",
        "parameters": {
            "company_list": "List of company names to compare",
            "companies_data": "JSON object containing data for each company",
            "example_comparison": "Optional example of a well-formatted comparison"
        }
    }
)

# 3. Financial Report Summarization Template
financial_report_template = PromptTemplate(
    template="""
You are a financial analyst summarizing quarterly earnings reports.

Based on the following financial report excerpt:
{report_text}

Create a concise summary that highlights:
1. Key performance metrics (revenue, EPS, operating margin)
2. Year-over-year and quarter-over-quarter changes
3. Management's forward-looking statements
4. Significant risk factors or challenges mentioned
5. Notable accounting changes or one-time events impacting results

Format the summary as bullet points under each category.
Prioritize information that would impact investment decisions.
Include specific numbers and percentages when available.
""",
    metadata={
        "version": "1.0.0",
        "author": "Financial Reporting Team",
        "description": "Summarizes quarterly financial reports into key points",
        "use_case": "financial_analysis",
        "parameters": {
            "report_text": "Text excerpt from a financial report to summarize"
        }
    }
)

# Example of using the library
if __name__ == "__main__":
    # Create a library
    library = PromptLibrary()
    
    # Add templates to the library
    library.add_template("financial.company_overview", company_overview_template)
    library.add_template("financial.peer_comparison", peer_comparison_template)
    library.add_template("financial.report_summary", financial_report_template)
    
    # Use a template
    template = library.get_template("financial.company_overview")
    formatted_prompt = template.format(
        company_name="Acme Technologies, Inc.",
        company_data="""
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
        """
    )
    
    print("Example formatted prompt:")
    print("-" * 80)
    print(formatted_prompt)
    print("-" * 80)
    
    # Save the library to a directory
    # Uncomment to save to disk
    # library.save_library("prompt_library")