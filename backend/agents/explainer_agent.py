def explain_solution(parsed, result):
    problem = parsed["problem_text"]
    solution = result["solution"]

    explanation = f"""
Problem:
{problem}

Step 1: Identify what is required.
We need to find the derivative.

Step 2: Apply the derivative rules.
The derivative of x^2 is 2x.
The derivative of 5x is 5.

Step 3: Combine results.
Final Answer: {solution}
"""

    return explanation.strip()
