import sympy as sp
import re

def normalize_expression(expr):
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    return expr

def solve_problem(parsed, context):
    problem = parsed["problem_text"]

    try:
        if "derivative" in problem.lower():
            raw_expr = problem.split("of")[-1].strip()
            clean_expr = normalize_expression(raw_expr)

            x = sp.symbols('x')
            expr = sp.sympify(clean_expr)
            solution = sp.diff(expr, x)

            return {
                "solution": str(solution),
                "method": "symbolic differentiation"
            }

        return {
            "solution": "Solver could not recognize problem type.",
            "method": "unknown"
        }

    except Exception as e:
        return {
            "solution": f"Error solving problem: {e}",
            "method": "exception"
        }
