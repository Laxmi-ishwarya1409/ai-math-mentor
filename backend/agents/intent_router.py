def route_intent(parsed_problem):
    topic = parsed_problem["topic"]

    if topic == "algebra":
        return "ALGEBRA_FLOW"
    elif topic == "calculus":
        return "CALCULUS_FLOW"
    elif topic == "probability":
        return "PROBABILITY_FLOW"
    elif topic == "linear_algebra":
        return "LINEAR_ALGEBRA_FLOW"
    else:
        return "GENERAL_FLOW"
