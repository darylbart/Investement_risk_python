import json

def determine_risk_appetite(user_responses, questions):
    total_weighted_score = 0
    total_weight = 0

    for i, response in enumerate(user_responses):
        total_weighted_score += int(response) * questions[i % len(questions)]["weight"]
        total_weight += questions[i % len(questions)]["weight"]

    if total_weight == 0:
        return "Unable to determine risk appetite"  # Handle edge case

    average_score = total_weighted_score / total_weight

    if average_score < 2.25:
        risk_appetite = "Conservative"
    elif 2.25 <= average_score < 3.75:
        risk_appetite = "Moderate"
    else:
        risk_appetite = "Aggressive"

    return risk_appetite
