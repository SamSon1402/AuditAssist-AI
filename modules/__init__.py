# This file makes the modules directory a Python package
# It can be empty or include imports to make key functions available at package level

from .analyzer import analyze_document, highlight_issues_in_text, get_document_template
from .visualizer import create_compliance_chart, generate_preview_chart
from .utils import simulate_progress, calculate_compliance_score

__all__ = [
    'analyze_document',
    'highlight_issues_in_text',
    'get_document_template',
    'create_compliance_chart',
    'generate_preview_chart',
    'simulate_progress',
    'calculate_compliance_score'
]