import re
import numpy as np

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

def get_document_template(template_name):
    """Return sample document text based on template name"""
    try:
        # Try to read from the sample_data directory
        with open(f"assets/sample_data/{template_name.lower().replace(' ', '_')}.txt", "r") as file:
            return file.read()
    except:
        # Fallback to hardcoded templates
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