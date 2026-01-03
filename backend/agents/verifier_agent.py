def verify_solution(parsed, result):
    verdict = "PASS"
    confidence = 0.9
    needs_human = False

    if result["method"] == "exception":
        verdict = "FAIL"
        confidence = 0.1
        needs_human = True

    if "could not" in result["solution"].lower():
        verdict = "FAIL"
        confidence = 0.2
        needs_human = True

    return {
        "verdict": verdict,
        "confidence": confidence,
        "needs_human": needs_human
    }
