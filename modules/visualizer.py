import altair as alt
import pandas as pd
import numpy as np

def create_compliance_chart(data, compliance_type):
    """Create a compliance breakdown chart based on compliance type and data"""
    
    if compliance_type == "Policy Clause Verification":
        chart_data = pd.DataFrame({
            'Category': ['Required Terms', 'Mandatory Language', 'Ambiguous Language'],
            'Score': [
                min(100, max(0, data["compliance_score"] + np.random.randint(-10, 11))),
                min(100, max(0, data["compliance_score"] + np.random.randint(-15, 16))),
                min(100, max(0, data["compliance_score"] + np.random.randint(-20, 21)))
            ]
        })
    elif compliance_type == "Regulatory Disclosure Check":
        chart_data = pd.DataFrame({
            'Category': ['Disclosure Terms', 'Regulatory References', 'Board Oversight', 'Annual Review'],
            'Score': [
                min(100, max(0, data["compliance_score"] + np.random.randint(-10, 11))),
                min(100, max(0, data["compliance_score"] + np.random.randint(-15, 16))),
                min(100, max(0, data["compliance_score"] + np.random.randint(-20, 21))),
                min(100, max(0, data["compliance_score"] + np.random.randint(-12, 13)))
            ]
        })
    else:  # Risk Factor Identification
        chart_data = pd.DataFrame({
            'Category': ['Risk Categories', 'Probability Analysis', 'Impact Analysis', 'Mitigation Strategies'],
            'Score': [
                min(100, max(0, data["compliance_score"] + np.random.randint(-10, 11))),
                min(100, max(0, data["compliance_score"] + np.random.randint(-15, 16))),
                min(100, max(0, data["compliance_score"] + np.random.randint(-20, 21))),
                min(100, max(0, data["compliance_score"] + np.random.randint(-12, 13)))
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
    
    return chart

def generate_preview_chart():
    """Generate a sample preview chart for demonstration"""
    
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
    
    return preview_chart

def create_risk_heatmap(risk_factors, values, categories=['Probability', 'Impact']):
    """Create a risk heatmap visualization"""
    
    # Convert text values to numeric
    value_map = {
        'low': 1,
        'medium': 2,
        'high': 3
    }
    
    numeric_values = []
    for value in values:
        if value.lower() in value_map:
            numeric_values.append(value_map[value.lower()])
        else:
            numeric_values.append(1)  # Default to low if value not recognized
    
    # Create data for heatmap
    data = []
    for i, risk in enumerate(risk_factors):
        for j, category in enumerate(categories):
            # Use modulo to cycle through values if not enough provided
            value_index = (i * len(categories) + j) % len(numeric_values)
            data.append({
                'Risk Factor': risk,
                'Category': category,
                'Value': numeric_values[value_index]
            })
    
    # Create DataFrame
    heatmap_data = pd.DataFrame(data)
    
    # Create heatmap
    heatmap = alt.Chart(heatmap_data).mark_rect().encode(
        x=alt.X('Category:N', title=None),
        y=alt.Y('Risk Factor:N', title=None),
        color=alt.Color('Value:Q', scale=alt.Scale(
            domain=[1, 2, 3],
            range=['#00ff9f', '#bd00ff', '#ff0080']
        )),
        tooltip=['Risk Factor', 'Category', 'Value']
    ).properties(
        title='Risk Assessment Matrix',
        width=300,
        height=200
    )
    
    return heatmap