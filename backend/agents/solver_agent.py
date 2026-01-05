import sympy as sp
import re

def normalize_expression(expr):
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    return expr

def solve_problem(parsed, context):
    text = parsed["problem_text"].lower()

    try:
        # DERIVATIVES
        if "derivative" in text:
            raw = text.split("of")[-1].strip()
            raw = raw.replace("sin x", "sin(x)").replace("cos x", "cos(x)")
            raw = normalize_expression(raw)
            x = sp.symbols('x')
            expr = sp.sympify(raw)
            sol = sp.diff(expr, x)
            return {"solution": str(sol), "method": "derivative"}

        # QUADRATIC EQUATIONS
        if "solve" in text and "x" in text and "=" in text:
            raw = text.replace("solve", "").replace(":", "").strip()
            left, right = raw.split("=")
            left = normalize_expression(left.strip())
            right = normalize_expression(right.strip())
            x = sp.symbols('x')
            equation = sp.sympify(left) - sp.sympify(right)
            sol = sp.solve(equation, x)
            return {"solution": str(sol), "method": "quadratic"}


        # LIMITS
        if "limit" in text:
            raw = text.split("of")[-1].split("as")[0].strip()
            raw = raw.replace("sin x", "sin(x)").replace("cos x", "cos(x)")
            raw = normalize_expression(raw)
            x = sp.symbols('x')
            sol = sp.limit(sp.sympify(raw), x, 0)
            return {"solution": str(sol), "method": "limit"}

        return {"solution": "Solver could not recognize problem type.", "method": "unknown"}

    except Exception as e:
        return {"solution": f"Error: {e}", "method": "exception"}
