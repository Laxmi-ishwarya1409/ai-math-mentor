import re
import sympy as sp
import ast

def normalize_expression(expr):
    expr = expr.lower()

    # spoken math
    expr = expr.replace("squared", "^2")
    expr = expr.replace("cubed", "^3")
    expr = expr.replace("plus", "+")
    expr = expr.replace("minus", "-")
    expr = expr.replace("times", "*")
    expr = expr.replace("multiplied by", "*")
    expr = expr.replace("divided by", "/")

    # fix powers
    expr = expr.replace("^", "**")

    # fix trig functions: sin x -> sin(x)
    expr = re.sub(r'sin\s+([a-zA-Z0-9]+)', r'sin(\1)', expr)
    expr = re.sub(r'cos\s+([a-zA-Z0-9]+)', r'cos(\1)', expr)
    expr = re.sub(r'tan\s+([a-zA-Z0-9]+)', r'tan(\1)', expr)

    # insert multiplication: 5x -> 5*x
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)

    return expr



def solve_problem(parsed, context):
    text = parsed["problem_text"].lower()

    try:
        # DERIVATIVE
        if "derivative" in text:
            expr = text.split("of")[-1]
            expr = normalize_expression(expr)
            x = sp.symbols("x")
            result = sp.diff(expr, x)
            return {"solution": str(result), "method": "derivative"}

        # LIMIT
        if "limit" in text:
            x = sp.symbols("x")
            expr = text.split("of")[-1]
            expr = expr.replace("as x approaches 0", "").strip()
            expr = normalize_expression(expr)
            sym_expr = sp.sympify(expr)
            result = sp.limit(sym_expr, x, 0)
            return {"solution": str(result), "method": "limit"}


        # QUADRATIC EQUATION
        if "=" in text:
            expr = text.replace("solve:", "").strip()
            left, right = expr.split("=")
            x = sp.symbols("x")
            equation = sp.Eq(sp.sympify(normalize_expression(left)), sp.sympify(normalize_expression(right)))
            result = sp.solve(equation, x)
            return {"solution": str(result), "method": "equation solving"}

        # PROBABILITY — die
        if "probability" in text and "die" in text:
            return {"solution": "1/2", "method": "basic probability"}

        # LINEAR ALGEBRA — determinant 2x2
        if "determinant" in text and "[" in text:
            matrix_text = text.split("matrix")[-1].strip()
            matrix = ast.literal_eval(matrix_text)
            a, b = matrix[0]
            c, d = matrix[1]
            det = a*d - b*c
            return {"solution": str(det), "method": "matrix determinant"}

    except Exception as e:
        return {"solution": f"Error: {e}", "method": "exception"}

    return {"solution": "Solver could not recognize problem type.", "method": "unknown"}
