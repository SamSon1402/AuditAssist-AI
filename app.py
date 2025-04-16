import streamlit as st
import pandas as pd
import numpy as np
import re
from io import StringIO
import altair as alt
import time

# Set page configuration
st.set_page_config(
    page_title="AuditAssist AI: Compliance Check", 
    page_icon="🤖",
    layout="wide"
)

# Apply futuristic CSS
def apply_futuristic_styles():
    st.markdown(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
        
        <style>
        /* Global Styles */
        .main {
            background-color: #0a0a18;
            background-image: linear-gradient(0deg, rgba(5, 5, 20, 0.9) 0%, rgba(10, 12, 35, 0.9) 100%), 
                              url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h100v100H0z' fill='none'/%3E%3Cpath d='M0 0h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 99h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M10 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M10 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M20 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M20 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M30 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M30 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M40 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M40 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M50 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M50 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M60 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M60 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M70 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M70 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M80 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M80 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M90 0h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M90 99h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 10h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 10h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 20h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 20h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 30h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 30h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 40h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 40h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 50h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 50h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 60h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 60h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 70h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 70h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 80h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 80h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M0 90h1v1H0z' fill='%230f41a3' fill-opacity='0.05'/%3E%3Cpath d='M99 90h1v1h-1z' fill='%230f41a3' fill-opacity='0.05'/%3E%3C/svg%3E");
            color: #ffffff;
        }
        
        .main .block-container {
            padding-top: 1rem;
        }
        
        /* Futuristic Title */
        .cyber-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 3.5em;
            color: #00bfff;
            text-align: center;
            margin-bottom: 0px;
            text-shadow: 0 0 10px rgba(0, 191, 255, 0.7), 0 0 20px rgba(0, 191, 255, 0.5);
            position: relative;
            letter-spacing: 2px;
        }
        
        .cyber-title:before {
            content: attr(data-text);
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            text-shadow: -2px 0 #ff00ff, 2px 0 #00ffff;
            opacity: 0.5;
            animation: glitch 2s infinite linear alternate-reverse;
        }
        
        @keyframes glitch {
            0%, 94%, 100% {
                transform: translate(0);
                opacity: 0.2;
            }
            95% {
                transform: translate(-5px, 0);
                opacity: 0.6;
            }
            96% {
                transform: translate(5px, 0);
                opacity: 0.6;
            }
            97% {
                transform: translate(0, 2px);
                opacity: 0.6;
            }
            98% {
                transform: translate(0, -2px);
                opacity: 0.6;
            }
        }
        
        /* Cyber Subtitle */
        .cyber-subtitle {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5em;
            color: #bd00ff;
            text-align: center;
            margin-bottom: 20px;
            letter-spacing: 1px;
            text-shadow: 0 0 10px rgba(189, 0, 255, 0.5);
        }
        
        /* Section Headers */
        .cyber-header {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8em;
            color: #0cebeb;
            margin: 20px 0 10px 0;
            border-top: 1px solid rgba(12, 235, 235, 0.3);
            border-bottom: 1px solid rgba(12, 235, 235, 0.3);
            padding: 5px 0;
            position: relative;
            text-shadow: 0 0 5px rgba(12, 235, 235, 0.5);
        }
        
        .cyber-header:before, .cyber-header:after {
            content: "";
            position: absolute;
            top: 0;
            width: 15px;
            height: 100%;
            border-top: 1px solid rgba(12, 235, 235, 0.8);
            border-bottom: 1px solid rgba(12, 235, 235, 0.8);
        }
        
        .cyber-header:before {
            left: -15px;
            border-left: 1px solid rgba(12, 235, 235, 0.8);
        }
        
        .cyber-header:after {
            right: -15px;
            border-right: 1px solid rgba(12, 235, 235, 0.8);
        }
        
        /* Section Sub-headers */
        .cyber-subheader {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.2em;
            color: #ff9e00;
            margin: 15px 0 10px 0;
            background-color: rgba(10, 10, 25, 0.7);
            padding: 5px 10px;
            display: inline-block;
            border-left: 2px solid #ff9e00;
            text-shadow: 0 0 5px rgba(255, 158, 0, 0.5);
        }
        
        /* Neon Container */
        .cyber-container {
            background-color: rgba(10, 12, 40, 0.8);
            border: 1px solid transparent;
            border-image: linear-gradient(to bottom right, #0cebeb, #bd00ff);
            border-image-slice: 1;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 0 10px rgba(12, 235, 235, 0.2), 0 0 20px rgba(189, 0, 255, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        .cyber-container:before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(to right, transparent, #0cebeb, transparent);
        }
        
        .cyber-container:after {
            content: "";
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(to right, transparent, #bd00ff, transparent);
        }
        
        /* Holographic Text Display */
        .holo-display {
            font-family: 'Space Mono', monospace;
            background-color: rgba(5, 7, 25, 0.9);
            color: #ffffff;
            padding: 15px;
            border: 1px solid #0cebeb;
            line-height: 1.5;
            position: relative;
            box-shadow: 0 0 10px rgba(12, 235, 235, 0.3);
            overflow-y: auto;
            max-height: 400px;
        }
        
        .holo-display:before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(180deg, 
                rgba(12, 235, 235, 0.1) 0%, 
                rgba(12, 235, 235, 0) 5%, 
                rgba(12, 235, 235, 0) 95%, 
                rgba(12, 235, 235, 0.1) 100%);
            pointer-events: none;
        }
        
        /* Scanner Lines Animation */
        .holo-display:after {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(180deg, 
                rgba(120, 255, 255, 0) 0%, 
                rgba(120, 255, 255, 0.1) 50%, 
                rgba(120, 255, 255, 0) 100%);
            background-size: 100% 20px;
            pointer-events: none;
            animation: scanlines 8s linear infinite;
        }
        
        @keyframes scanlines {
            0% {
                background-position: 0 0;
            }
            100% {
                background-position: 0 100%;
            }
        }
        
        /* Highlight Styles */
        .highlight-high {
            background-color: rgba(255, 0, 128, 0.25);
            border-bottom: 2px solid #ff0080;
            padding: 0 2px;
            animation: pulse-high 2s infinite;
        }
        
        @keyframes pulse-high {
            0%, 100% {
                background-color: rgba(255, 0, 128, 0.25);
            }
            50% {
                background-color: rgba(255, 0, 128, 0.4);
            }
        }
        
        .highlight-medium {
            background-color: rgba(255, 165, 0, 0.25);
            border-bottom: 2px solid #ffa500;
            padding: 0 2px;
            animation: pulse-medium 2s infinite;
        }
        
        @keyframes pulse-medium {
            0%, 100% {
                background-color: rgba(255, 165, 0, 0.25);
            }
            50% {
                background-color: rgba(255, 165, 0, 0.4);
            }
        }
        
        .highlight-low {
            background-color: rgba(12, 235, 235, 0.25);
            border-bottom: 2px solid #0cebeb;
            padding: 0 2px;
            animation: pulse-low 2s infinite;
        }
        
        @keyframes pulse-low {
            0%, 100% {
                background-color: rgba(12, 235, 235, 0.25);
            }
            50% {
                background-color: rgba(12, 235, 235, 0.4);
            }
        }
        
        /* Metrics */
        .metric-good {
            color: #00ff9f;
            text-shadow: 0 0 10px rgba(0, 255, 159, 0.7);
        }
        
        .metric-medium {
            color: #ffa500;
            text-shadow: 0 0 10px rgba(255, 165, 0, 0.7);
        }
        
        .metric-poor {
            color: #ff0080;
            text-shadow: 0 0 10px rgba(255, 0, 128, 0.7);
        }
        
        /* Issue Cards */
        .cyber-issue {
            background-color: rgba(10, 12, 40, 0.8);
            border: 1px solid;
            padding: 10px;
            margin-bottom: 15px;
            position: relative;
            overflow: hidden;
        }
        
        .cyber-issue:before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, 
                rgba(255, 255, 255, 0) 0%, 
                rgba(255, 255, 255, 0.03) 50%, 
                rgba(255, 255, 255, 0) 100%);
            pointer-events: none;
        }
        
        .cyber-issue-high {
            border-color: #ff0080;
            box-shadow: 0 0 10px rgba(255, 0, 128, 0.3);
        }
        
        .cyber-issue-medium {
            border-color: #ffa500;
            box-shadow: 0 0 10px rgba(255, 165, 0, 0.3);
        }
        
        .cyber-issue-low {
            border-color: #0cebeb;
            box-shadow: 0 0 10px rgba(12, 235, 235, 0.3);
        }
        
        /* Progress Bar Animation */
        @keyframes cyber-progress {
            0% {
                background-position: 0% 50%;
            }
            100% {
                background-position: 100% 50%;
            }
        }
        
        /* Futuristic buttons */
        .stButton > button {
            font-family: 'Orbitron', sans-serif !important;
            background: linear-gradient(90deg, #0cebeb, #0072ff) !important;
            color: white !important;
            border: none !important;
            padding: 0.5em 1em !important;
            position: relative !important;
            box-shadow: 0 0 10px rgba(12, 235, 235, 0.5) !important;
            transition: all 0.3s !important;
            border-radius: 4px !important;
            text-shadow: 0 0 5px rgba(255, 255, 255, 0.5) !important;
        }
        
        .stButton > button:hover {
            box-shadow: 0 0 15px rgba(12, 235, 235, 0.8) !important;
            text-shadow: 0 0 8px rgba(255, 255, 255, 0.8) !important;
            transform: translateY(-2px) !important;
        }
        
        .stButton > button:active {
            box-shadow: 0 0 5px rgba(12, 235, 235, 0.3) !important;
            transform: translateY(1px) !important;
        }
        
        /* Override Streamlit elements for better visibility */
        .stSelectbox > div > div > div {
            background-color: rgba(10, 12, 40, 0.8) !important;
            color: white !important;
            border: 1px solid #0cebeb !important;
        }
        
        .stTextArea > div > div > textarea {
            background-color: rgba(10, 12, 40, 0.8) !important;
            color: white !important;
            border: 1px solid #0cebeb !important;
            font-family: 'Space Mono', monospace !important;
        }
        
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #0cebeb, #bd00ff) !important;
            background-size: 200% 100% !important;
            animation: cyber-progress 2s linear infinite !important;
        }
        
        /* Special scanner animation for document analysis */
        @keyframes scan-animation {
            0% {
                background-position: 0% 0%;
            }
            100% {
                background-position: 0% 100%;
            }
        }
        
        .scanning-overlay {
            position: relative;
        }
        
        .scanning-overlay:after {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(to bottom, 
                rgba(12, 235, 235, 0) 0%, 
                rgba(12, 235, 235, 0.2) 50%, 
                rgba(12, 235, 235, 0) 100%);
            background-size: 100% 20px;
            animation: scan-animation 1.5s linear infinite;
            pointer-events: none;
            z-index: 1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_futuristic_styles()

# Initialize session state
if 'analyzed' not in st.session_state:
    st.session_state.analyzed = False
if 'compliance_score' not in st.session_state:
    st.session_state.compliance_score = 0
if 'issues_found' not in st.session_state:
    st.session_state.issues_found = 0
if 'document_text' not in st.session_state:
    st.session_state.document_text = ""
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = []
if 'compliance_type' not in st.session_state:
    st.session_state.compliance_type = "Policy Clause Verification"
if 'scanning' not in st.session_state:
    st.session_state.scanning = False

# Function to simulate NLP analysis
def analyze_document(text, compliance_type):
    """Simulate NLP analysis of document text based on compliance type"""
    # This is a simulation for prototype purposes
    issues = []
    compliance_score = 0
    
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    if compliance_type == "Policy Clause Verification":
        # Check for key policy elements
        rules = [
            {"term": "compliance", "required": True, "found": "compliance" in text_lower},
            {"term": "risk assessment", "required": True, "found": "risk assessment" in text_lower},
            {"term": "policy", "required": True, "found": "policy" in text_lower},
            {"term": "data protection", "required": True, "found": "data protection" in text_lower},
            {"term": "shall", "warning": "Use mandatory language", "found": "shall" in text_lower},
            {"term": "must", "warning": "Use mandatory language", "found": "must" in text_lower},
            {"term": "required", "warning": "Use mandatory language", "found": "required" in text_lower},
            {"term": "may", "warning": "Avoid ambiguous language", "found": "may" in text_lower},
            {"term": "should", "warning": "Avoid ambiguous language", "found": "should" in text_lower},
            {"term": "can", "warning": "Avoid ambiguous language", "found": "can" in text_lower}
        ]
        
        # Process rules
        for rule in rules:
            if "required" in rule and rule["required"] and not rule["found"]:
                issues.append({
                    "term": rule["term"],
                    "issue": f"Required term '{rule['term']}' is missing",
                    "severity": "high",
                    "position": None
                })
            elif "warning" in rule and rule["found"]:
                # Find positions of warning terms
                pattern = r'\b' + re.escape(rule["term"]) + r'\b'
                for match in re.finditer(pattern, text_lower):
                    issues.append({
                        "term": rule["term"],
                        "issue": rule["warning"],
                        "severity": "medium",
                        "position": match.span()
                    })
                
        # Calculate compliance score
        required_count = sum(1 for rule in rules if "required" in rule and rule["required"])
        found_required_count = sum(1 for rule in rules if "required" in rule and rule["required"] and rule["found"])
        
        if required_count > 0:
            compliance_score = int((found_required_count / required_count) * 100)
        else:
            compliance_score = 100
            
    elif compliance_type == "Regulatory Disclosure Check":
        # Check for regulatory disclosure elements
        rules = [
            {"term": "disclosure", "required": True, "found": "disclosure" in text_lower},
            {"term": "regulation", "required": True, "found": "regulation" in text_lower or "regulatory" in text_lower},
            {"term": "compliance", "required": True, "found": "compliance" in text_lower},
            {"term": "risk", "required": True, "found": "risk" in text_lower},
            {"term": "management", "required": True, "found": "management" in text_lower},
            {"term": "control", "required": True, "found": "control" in text_lower},
            {"term": "approve", "required": False, "found": "approve" in text_lower or "approval" in text_lower},
            {"term": "review", "required": False, "found": "review" in text_lower},
            {"term": "annually", "required": True, "found": "annually" in text_lower or "annual" in text_lower},
            {"term": "board", "required": True, "found": "board" in text_lower}
        ]
        
        # Process rules
        for rule in rules:
            if rule["required"] and not rule["found"]:
                issues.append({
                    "term": rule["term"],
                    "issue": f"Required disclosure term '{rule['term']}' is missing",
                    "severity": "high",
                    "position": None
                })
                
        # Calculate compliance score
        required_count = sum(1 for rule in rules if rule["required"])
        found_required_count = sum(1 for rule in rules if rule["required"] and rule["found"])
        
        if required_count > 0:
            compliance_score = int((found_required_count / required_count) * 100)
        else:
            compliance_score = 100
            
    elif compliance_type == "Risk Factor Identification":
        # Check for risk factors
        risk_factors = [
            "market risk",
            "credit risk",
            "operational risk",
            "liquidity risk",
            "strategic risk",
            "cybersecurity risk",
            "regulatory risk",
            "reputation risk",
            "climate risk"
        ]
        
        found_risks = []
        for risk in risk_factors:
            if risk in text_lower:
                found_risks.append(risk)
            else:
                issues.append({
                    "term": risk,
                    "issue": f"Risk factor '{risk}' not identified",
                    "severity": "medium",
                    "position": None
                })
                
        # Check for risk analysis patterns
        if "probability" not in text_lower and "likelihood" not in text_lower:
            issues.append({
                "term": "probability/likelihood",
                "issue": "No risk probability/likelihood analysis found",
                "severity": "high",
                "position": None
            })
            
        if "impact" not in text_lower:
            issues.append({
                "term": "impact",
                "issue": "No risk impact analysis found",
                "severity": "high",
                "position": None
            })
            
        if "mitigation" not in text_lower:
            issues.append({
                "term": "mitigation",
                "issue": "No risk mitigation strategies found",
                "severity": "high",
                "position": None
            })
            
        # Calculate compliance score
        expected_items = len(risk_factors) + 3  # risks + probability + impact + mitigation
        found_items = len(found_risks)
        if "probability" in text_lower or "likelihood" in text_lower:
            found_items += 1
        if "impact" in text_lower:
            found_items += 1
        if "mitigation" in text_lower:
            found_items += 1
            
        compliance_score = int((found_items / expected_items) * 100)
    
    # Add some random variations to make the prototype more interesting
    compliance_score = min(100, max(0, compliance_score + np.random.randint(-5, 6)))
    
    return {
        "compliance_score": compliance_score,
        "issues_found": len(issues),
        "issues": issues
    }

# Function to highlight issues in text
def highlight_issues_in_text(text, issues):
    """Add HTML highlighting to issues found in text"""
    # Create a copy of the text for highlighting
    highlighted_text = text
    
    # Create spans for highlighting (only for issues with positions)
    position_issues = [issue for issue in issues if issue["position"] is not None]
    
    # Sort issues by position in reverse order to avoid offset issues
    sorted_issues = sorted(position_issues, key=lambda x: x["position"][0], reverse=True)
    
    for issue in sorted_issues:
        start, end = issue["position"]
        term = text[start:end]
        
        if issue["severity"] == "high":
            highlight_class = "highlight-high"
        elif issue["severity"] == "medium":
            highlight_class = "highlight-medium"
        else:
            highlight_class = "highlight-low"
            
        highlighted_term = f'<span class="{highlight_class}">{term}</span>'
        highlighted_text = highlighted_text[:start] + highlighted_term + highlighted_text[end:]
    
    return highlighted_text

# Function for sample document templates
def get_document_template(template_name):
    """Return sample document text based on template name"""
    templates = {
        "Policy Document": """
ACME CORPORATION
CYBERSECURITY POLICY

1. PURPOSE
This policy establishes the requirements for maintaining cybersecurity compliance across all ACME Corporation operations.

2. SCOPE
This policy applies to all employees, contractors, and third-party vendors who have access to ACME systems or data.

3. POLICY STATEMENTS
3.1 Data Protection
All sensitive data must be encrypted both in transit and at rest.

3.2 Access Control
Access to systems and data should be based on the principle of least privilege.

3.3 Risk Assessment
Risk assessments may be conducted annually to identify vulnerabilities and threats.

4. COMPLIANCE
4.1 All employees are required to comply with this policy.
4.2 Violations can result in disciplinary action.

5. REVIEW
This policy shall be reviewed annually by the Security Team.
        """,
        
        "Regulatory Disclosure": """
ACME CORPORATION
REGULATORY DISCLOSURE STATEMENT

In accordance with Regulation XYZ, ACME Corporation discloses the following information:

1. RISK MANAGEMENT FRAMEWORK
The company has implemented a comprehensive risk management framework that addresses market risk, credit risk, and operational risk.

2. CONTROL ENVIRONMENT
Our control environment includes policies, procedures, and technologies designed to mitigate risks.

3. BOARD OVERSIGHT
The Board reviews and approves all major risk policies quarterly.

4. COMPLIANCE ACTIVITIES
Compliance with applicable regulations is monitored through our compliance program.

5. FUTURE OUTLOOK
We anticipate changes to the regulatory landscape and are preparing accordingly.
        """,
        
        "Risk Assessment": """
ACME CORPORATION
ENTERPRISE RISK ASSESSMENT

EXECUTIVE SUMMARY
This document outlines the key risks facing ACME Corporation and our strategies for managing them.

KEY RISK FACTORS:
1. Market Risk: Volatility in key markets could impact revenue
   Probability: Medium
   Impact: High
   Mitigation: Diversification of revenue streams

2. Operational Risk: System failures could disrupt services
   Probability: Low
   Impact: High
   Mitigation: Redundant systems and business continuity planning

3. Credit Risk: Customer defaults could increase
   Probability: Low
   Impact: Medium
   Mitigation: Enhanced credit monitoring

4. Regulatory Risk: Changes in regulations could require operational adjustments
   Probability: Medium
   Impact: Medium
   Mitigation: Active monitoring of regulatory developments

CONCLUSION
Management has reviewed this assessment and believes the company is well-positioned to address these risks.
        """
    }
    
    return templates.get(template_name, "")

# Main application header
st.markdown('<div class="cyber-title" data-text="AUDITASSIST AI">AUDITASSIST AI</div>', unsafe_allow_html=True)
st.markdown('<div class="cyber-subtitle">NLP COMPLIANCE CHECK PROTOTYPE</div>', unsafe_allow_html=True)

st.markdown('<div class="cyber-container"><p>Welcome to AuditAssist AI, your automated compliance analysis tool. Upload documents to check for compliance with predefined rules and standards.</p><p>This prototype demonstrates how Natural Language Processing (NLP) can assist AXA\'s Internal Audit function with document review.</p></div>', unsafe_allow_html=True)

# Main application layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="cyber-header">CONFIGURATION</div>', unsafe_allow_html=True)
    
    # Compliance check type selection
    st.markdown('<div class="cyber-subheader">SELECT COMPLIANCE CHECK</div>', unsafe_allow_html=True)
    
    compliance_type = st.selectbox(
        "Compliance Check Type",
        ["Policy Clause Verification", "Regulatory Disclosure Check", "Risk Factor Identification"],
        key="compliance_selector",
        label_visibility="collapsed"
    )
    st.session_state.compliance_type = compliance_type
    
    # Rule set explanation based on selected compliance type
    if compliance_type == "Policy Clause Verification":
        st.markdown('''
            <div class="cyber-container">
                <h3 style="font-family: 'Orbitron', sans-serif; color: #0cebeb; margin-top: 0;">POLICY CLAUSE RULES</h3>
                <p style="color: #ffffff;">Checks policy documents for:</p>
                <ul style="color: #ffffff;">
                    <li>Required terms: compliance, risk assessment, policy, data protection</li>
                    <li>Mandatory language (shall, must, required)</li>
                    <li>Ambiguous language (may, should, can)</li>
                </ul>
            </div>
        ''', unsafe_allow_html=True)
    elif compliance_type == "Regulatory Disclosure Check":
        st.markdown('''
            <div class="cyber-container">
                <h3 style="font-family: 'Orbitron', sans-serif; color: #0cebeb; margin-top: 0;">REGULATORY DISCLOSURE RULES</h3>
                <p style="color: #ffffff;">Checks disclosure documents for:</p>
                <ul style="color: #ffffff;">
                    <li>Required disclosure terms</li>
                    <li>Regulatory compliance references</li>
                    <li>Annual review mentions</li>
                    <li>Board oversight statements</li>
                </ul>
            </div>
        ''', unsafe_allow_html=True)
    elif compliance_type == "Risk Factor Identification":
        st.markdown('''
            <div class="cyber-container">
                <h3 style="font-family: 'Orbitron', sans-serif; color: #0cebeb; margin-top: 0;">RISK FACTOR RULES</h3>
                <p style="color: #ffffff;">Checks risk documents for:</p>
                <ul style="color: #ffffff;">
                    <li>Key risk categories (market, credit, operational, etc.)</li>
                    <li>Risk probability/likelihood statements</li>
                    <li>Impact analysis</li>
                    <li>Mitigation strategies</li>
                </ul>
            </div>
        ''', unsafe_allow_html=True)
    
    # Document upload section
    st.markdown('<div class="cyber-header">DOCUMENT INPUT</div>', unsafe_allow_html=True)
    
    # Sample templates option
    st.markdown('<div class="cyber-subheader">LOAD SAMPLE TEMPLATE</div>', unsafe_allow_html=True)
    
    template_options = ["None", "Policy Document", "Regulatory Disclosure", "Risk Assessment"]
    template_choice = st.selectbox("Template", template_options, index=0, label_visibility="collapsed")
    
    if template_choice != "None":
        st.session_state.document_text = get_document_template(template_choice)
        st.session_state.analyzed = False
    
    # Manual text entry
    st.markdown('<div class="cyber-subheader">OR ENTER TEXT MANUALLY</div>', unsafe_allow_html=True)
    
    manual_text = st.text_area("Enter document text", height=150, label_visibility="collapsed")
    if manual_text:
        st.session_state.document_text = manual_text
        st.session_state.analyzed = False
    
    # Upload file option
    st.markdown('<div class="cyber-subheader">OR UPLOAD DOCUMENT</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload a document (.txt, .csv)", type=["txt", "csv"], label_visibility="collapsed")
    
    if uploaded_file is not None:
        try:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            st.session_state.document_text = stringio.read()
            st.session_state.analyzed = False
        except Exception as e:
            st.error(f"Error reading file: {e}")
    
    # Analyze button - made larger and more prominent
    if st.button("INITIATE COMPLIANCE SCAN", key="analyze_btn", use_container_width=True, 
                help="Run compliance check on the document"):
        if st.session_state.document_text:
            st.session_state.scanning = True
            
            # Create a cool futuristic scanning animation
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(101):
                # Update progress bar
                progress_bar.progress(i)
                
                # Update status messages to look like a futuristic scan
                if i < 20:
                    status_text.markdown(f'<div style="font-family: \'Space Mono\', monospace; color: #0cebeb;">Initializing document scan... {i}%</div>', unsafe_allow_html=True)
                elif i < 40:
                    status_text.markdown(f'<div style="font-family: \'Space Mono\', monospace; color: #0cebeb;">Analyzing semantic structure... {i}%</div>', unsafe_allow_html=True)
                elif i < 60:
                    status_text.markdown(f'<div style="font-family: \'Space Mono\', monospace; color: #0cebeb;">Detecting compliance patterns... {i}%</div>', unsafe_allow_html=True)
                elif i < 80:
                    status_text.markdown(f'<div style="font-family: \'Space Mono\', monospace; color: #0cebeb;">Verifying regulatory alignment... {i}%</div>', unsafe_allow_html=True)
                else:
                    status_text.markdown(f'<div style="font-family: \'Space Mono\', monospace; color: #0cebeb;">Finalizing compliance assessment... {i}%</div>', unsafe_allow_html=True)
                
                time.sleep(0.03)  # Simulate processing time
                
                if i == 100:
                    # Simulate NLP analysis
                    analysis_result = analyze_document(st.session_state.document_text, st.session_state.compliance_type)
                    
                    # Store results in session state
                    st.session_state.compliance_score = analysis_result["compliance_score"]
                    st.session_state.issues_found = analysis_result["issues_found"]
                    st.session_state.analysis_results = analysis_result["issues"]
                    st.session_state.analyzed = True
                    st.session_state.scanning = False
                    
                    # Show completion message and clear
                    status_text.markdown(f'<div style="font-family: \'Space Mono\', monospace; color: #00ff9f;">Scan complete! Analysis results ready.</div>', unsafe_allow_html=True)
                    time.sleep(1)
                    status_text.empty()
        else:
            st.warning("Please enter or upload a document first.")

with col2:
    st.markdown('<div class="cyber-header">ANALYSIS RESULTS</div>', unsafe_allow_html=True)
    
    if st.session_state.analyzed:
        # Display compliance score with cool futuristic style
        score_color = "good" if st.session_state.compliance_score >= 80 else "medium" if st.session_state.compliance_score >= 50 else "poor"
        
        col_score, col_issues = st.columns(2)
        
        with col_score:
            st.markdown(f'''
                <div class="cyber-container" style="text-align: center; padding: 15px;">
                    <div style="font-family: 'Orbitron', sans-serif; font-size: 20px; color: #ffffff;">COMPLIANCE SCORE</div>
                    <div style="font-family: 'Orbitron', sans-serif; font-size: 48px;" class="metric-{score_color}">{st.session_state.compliance_score}%</div>
                </div>
            ''', unsafe_allow_html=True)
            
        with col_issues:
            issue_color = "good" if st.session_state.issues_found == 0 else "medium" if st.session_state.issues_found <= 3 else "poor"
            st.markdown(f'''
                <div class="cyber-container" style="text-align: center; padding: 15px;">
                    <div style="font-family: 'Orbitron', sans-serif; font-size: 20px; color: #ffffff;">COMPLIANCE ISSUES</div>
                    <div style="font-family: 'Orbitron', sans-serif; font-size: 48px;" class="metric-{issue_color}">{st.session_state.issues_found}</div>
                </div>
            ''', unsafe_allow_html=True)
        
        # Status message with futuristic styling
        if st.session_state.compliance_score >= 80:
            st.markdown('<div style="background-color: rgba(0, 255, 159, 0.1); border-left: 4px solid #00ff9f; padding: 10px; font-family: \'Orbitron\', sans-serif; color: #00ff9f; margin: 15px 0; text-shadow: 0 0 5px rgba(0, 255, 159, 0.5);">✓ DOCUMENT PASSES COMPLIANCE CHECK</div>', unsafe_allow_html=True)
        elif st.session_state.compliance_score >= 50:
            st.markdown('<div style="background-color: rgba(255, 165, 0, 0.1); border-left: 4px solid #ffa500; padding: 10px; font-family: \'Orbitron\', sans-serif; color: #ffa500; margin: 15px 0; text-shadow: 0 0 5px rgba(255, 165, 0, 0.5);">⚠ DOCUMENT NEEDS REVIEW</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="background-color: rgba(255, 0, 128, 0.1); border-left: 4px solid #ff0080; padding: 10px; font-family: \'Orbitron\', sans-serif; color: #ff0080; margin: 15px 0; text-shadow: 0 0 5px rgba(255, 0, 128, 0.5);">✗ DOCUMENT FAILS COMPLIANCE CHECK</div>', unsafe_allow_html=True)
        
        # Document view with highlighted issues
        st.markdown('<div class="cyber-subheader">DOCUMENT TEXT</div>', unsafe_allow_html=True)
        
        highlighted_text = highlight_issues_in_text(st.session_state.document_text, st.session_state.analysis_results)
        st.markdown(f'<div class="holo-display">{highlighted_text}</div>', unsafe_allow_html=True)
        
        # Issues list
        st.markdown('<div class="cyber-subheader">COMPLIANCE ISSUES</div>', unsafe_allow_html=True)
        
        if st.session_state.issues_found > 0:
            # Create a custom issue display
            for i, issue in enumerate(st.session_state.analysis_results):
                severity_class = "cyber-issue-high" if issue["severity"] == "high" else "cyber-issue-medium" if issue["severity"] == "medium" else "cyber-issue-low"
                severity_color = "#ff0080" if issue["severity"] == "high" else "#ffa500" if issue["severity"] == "medium" else "#0cebeb"
                severity_text = "HIGH SEVERITY" if issue["severity"] == "high" else "MEDIUM SEVERITY" if issue["severity"] == "medium" else "LOW SEVERITY"
                
                st.markdown(f'''
                    <div class="cyber-issue {severity_class}">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div style="font-family: 'Orbitron', sans-serif; font-size: 18px; color: {severity_color}; text-shadow: 0 0 5px {severity_color};">
                                {severity_text}
                            </div>
                            <div style="font-family: 'Orbitron', sans-serif; font-size: 16px; color: #ffffff;">
                                TERM: {issue["term"].upper()}
                            </div>
                        </div>
                        <p style="margin-top: 10px; font-family: 'Space Mono', monospace; font-size: 14px; color: #ffffff;">
                            {issue["issue"]}
                        </p>
                    </div>
                ''', unsafe_allow_html=True)
        else:
            st.markdown('<div class="cyber-container"><p style="color: #00ff9f; text-shadow: 0 0 5px rgba(0, 255, 159, 0.5); font-weight: bold;">No compliance issues found. Document fully compliant!</p></div>', unsafe_allow_html=True)
            
        # Feedback section
        st.markdown('<div class="cyber-subheader">AUDITOR FEEDBACK</div>', unsafe_allow_html=True)
        
        auditor_notes = st.text_area("Enter your notes on this analysis", height=100, label_visibility="collapsed")
        
        col_save, col_export = st.columns(2)
        with col_save:
            if st.button("SAVE FEEDBACK", key="save_feedback"):
                st.success("Feedback saved to audit trail.")
        
        with col_export:
            if st.button("EXPORT RESULTS", key="export_results"):
                st.success("Results exported to secure repository.")
                
        # Visualization of compliance breakdown
        st.markdown('<div class="cyber-subheader">COMPLIANCE BREAKDOWN</div>', unsafe_allow_html=True)
        
        # Create some sample visualization data based on the analysis
        if compliance_type == "Policy Clause Verification":
            chart_data = pd.DataFrame({
                'Category': ['Required Terms', 'Mandatory Language', 'Ambiguous Language'],
                'Score': [
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-10, 11))),
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-15, 16))),
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-20, 21)))
                ]
            })
        elif compliance_type == "Regulatory Disclosure Check":
            chart_data = pd.DataFrame({
                'Category': ['Disclosure Terms', 'Regulatory References', 'Board Oversight', 'Annual Review'],
                'Score': [
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-10, 11))),
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-15, 16))),
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-20, 21))),
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-12, 13)))
                ]
            })
        else:  # Risk Factor Identification
            chart_data = pd.DataFrame({
                'Category': ['Risk Categories', 'Probability Analysis', 'Impact Analysis', 'Mitigation Strategies'],
                'Score': [
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-10, 11))),
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-15, 16))),
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-20, 21))),
                    min(100, max(0, st.session_state.compliance_score + np.random.randint(-12, 13)))
                ]
            })
            
        # Create horizontal bar chart with cyberpunk colors
        chart = alt.Chart(chart_data).mark_bar().encode(
            x=alt.X('Score:Q', title='Compliance Score (%)', scale=alt.Scale(domain=[0, 100])),
            y=alt.Y('Category:N', title=None),
            color=alt.Color('Score:Q', scale=alt.Scale(
                domain=[0, 50, 100],
                range=['#ff0080', '#bd00ff', '#00ff9f']
            ))
        ).properties(
            height=200
        )
        
        st.altair_chart(chart, use_container_width=True)
    elif st.session_state.scanning:
        # Show scanning animation when in scanning state
        st.markdown('<div class="scanning-overlay"><div class="cyber-container" style="text-align: center; padding: 50px 20px;"><div style="font-family: \'Orbitron\', sans-serif; font-size: 24px; color: #0cebeb; text-shadow: 0 0 10px rgba(12, 235, 235, 0.7);">SCANNING DOCUMENT</div><div style="font-family: \'Space Mono\', monospace; margin-top: 20px; color: #ffffff;">Please wait while the AI analyzes your document...</div></div></div>', unsafe_allow_html=True)
    else:
        # Display instructions when no document has been analyzed yet
        st.markdown('''
            <div class="cyber-container">
                <h3 style="font-family: 'Orbitron', sans-serif; color: #00ff9f; margin-top: 0; text-shadow: 0 0 5px rgba(0, 255, 159, 0.5);">HOW TO USE</h3>
                <ol style="color: #ffffff; font-family: 'Space Mono', monospace;">
                    <li>Select a compliance check type</li>
                    <li>Load a sample template or upload your own document</li>
                    <li>Click "INITIATE COMPLIANCE SCAN" to run the check</li>
                    <li>Review the results and highlighted issues</li>
                    <li>Add your feedback and export if needed</li>
                </ol>
            </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('''
            <div class="cyber-container">
                <h3 style="font-family: 'Orbitron', sans-serif; color: #0cebeb; margin-top: 0; text-shadow: 0 0 5px rgba(12, 235, 235, 0.5);">ABOUT THIS PROTOTYPE</h3>
                <p style="color: #ffffff; font-family: 'Space Mono', monospace;">AuditAssist AI demonstrates how Natural Language Processing (NLP) could assist AXA's Internal Audit function with compliance document review.</p>
                <p style="color: #ffffff; font-family: 'Space Mono', monospace;">This is a feasibility prototype to visualize the potential workflow and outputs.</p>
                <p style="color: #ffffff; font-family: 'Space Mono', monospace;">In a production version, this would connect to a secure AI system for enhanced analysis capabilities.</p>
            </div>
        ''', unsafe_allow_html=True)
        
        # Sample visualization
        st.markdown('<div class="cyber-subheader">PREVIEW</div>', unsafe_allow_html=True)
        
        # Create sample chart data
        preview_data = pd.DataFrame({
            'Category': ['Policy Completeness', 'Language Clarity', 'Regulatory Alignment', 'Overall Compliance'],
            'Score': [76, 62, 88, 75]
        })
        
        # Create preview chart with cyberpunk colors
        preview_chart = alt.Chart(preview_data).mark_bar().encode(
            x=alt.X('Score:Q', title='Score (%)', scale=alt.Scale(domain=[0, 100])),
            y=alt.Y('Category:N', title=None),
            color=alt.Color('Score:Q', scale=alt.Scale(
                domain=[0, 50, 100],
                range=['#ff0080', '#bd00ff', '#00ff9f']
            ))
        ).properties(
            title='Sample Compliance Analysis',
            height=200
        )
        
        st.altair_chart(preview_chart, use_container_width=True)