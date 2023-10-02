# risk_determination.py

import json

def determine_risk_appetite(user_responses, questions):
    total_score = 0

    for i, response in enumerate(user_responses):
        total_score += int(response) * questions[i % len(questions)]["weight"]

    average_score = total_score / len(user_responses)

    if average_score < 2.5:
        risk_appetite = "Conservative"
    elif 2.5 <= average_score <= 3.5:
        risk_appetite = "Moderate"
    else:
        risk_appetite = "Aggressive"

    return risk_appetite
