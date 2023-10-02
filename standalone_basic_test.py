import json

def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

def determine_risk_appetite(questions):
    print("Welcome to the Investment Risk Appetite Determination Tool!\n")
    
    num_questions = int(input("How many questions would you like to answer? (Enter a number between 5 and 20): "))
    num_questions = max(5, min(20, num_questions))
    
    print("Please answer the following questions on a scale of 1 to 5, where:")
    print("1 - Strongly Disagree")
    print("2 - Disagree")
    print("3 - Neutral")
    print("4 - Agree")
    print("5 - Strongly Agree\n")
    
    total_score = 0
    
    # Display the selected questions and get user responses
    for i in range(num_questions):
        question = questions[i % len(questions)]
        response = int(input(f"Question {i + 1}: {question['text']} (Enter a number between 1 and 5): "))
        total_score += response * question["weight"]
    
    # Calculate average score
    average_score = total_score / num_questions
    
    # Determine risk appetite based on the average score
    if average_score < 2.5:
        risk_appetite = "Conservative"
    elif 2.5 <= average_score <= 3.5:
        risk_appetite = "Moderate"
    else:
        risk_appetite = "Aggressive"
    
    print("\nThank you for completing the questionnaire.")
    print(f"Based on your responses, your investment risk appetite is: {risk_appetite}")

if __name__ == "__main__":
    questions = load_questions('questions.json')
    determine_risk_appetite(questions)
