import re

def parse_problem(text):
    topic = "algebra"
    if "limit" in text.lower():
        topic = "calculus"
    elif "probability" in text.lower():
        topic = "probability"
    elif "matrix" in text.lower():
        topic = "linear_algebra"

    variables = list(set(re.findall(r"[a-zA-Z]", text)))
    
    structured = {
        "problem_text": text,
        "topic": topic,
        "variables": variables,
        "constraints": [],
        "needs_clarification": False
    }

    return structured
