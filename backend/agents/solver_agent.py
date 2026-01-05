import sympy as sp
import re

def normalize_expression(expr):
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    return expr

def solve_problem(parsed, context):
    text = parsed["problem_text"].lower()

    try:
        # Derivatives
        if "derivative" in text:
            expr_str = normalize_expression(text.split("of")[-1])
            x = sp.symbols('x')
            expr = sp.sympify(expr_str)
            sol = sp.diff(expr, x)
            return {"solution": str(sol), "method": "derivative"}

        # Quadratic equations
        if "solve" in text and "x" in text:
            eq = normalize_expression(text.replace("solve", "").replace("=", "-(") + ")")
            x = sp.symbols('x')
            sol = sp.solve(sp.sympify(eq), x)
            return {"solution": str(sol), "method": "quadratic"}

        # Limits
        if "limit" in text:
            expr = normalize_expression(text.split("of")[-1].split("as")[0])
            x = sp.symbols('x')
            sol = sp.limit(sp.sympify(expr), x, 0)
            return {"solution": str(sol), "method": "limit"}

        return {"solution": "Solver could not recognize problem type.", "method": "unknown"}

    except Exception as e:
        return {"solution": f"Error: {e}", "method": "exception"}
