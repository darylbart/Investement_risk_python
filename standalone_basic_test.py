def determine_risk_appetite():
    print("Welcome to the Investment Risk Appetite Determination Tool!\n")
    
    # Prompt the user for the number of questions to answer
    num_questions = int(input("How many questions would you like to answer? (Enter a number between 5 and 20): "))
    num_questions = max(5, min(20, num_questions))  # Ensure the number of questions is within the valid range

    print("Please answer the following questions on a scale of 1 to 5, where:")
    print("1 - Strongly Disagree")
    print("2 - Disagree")
    print("3 - Neutral")
    print("4 - Agree")
    print("5 - Strongly Agree\n")
    
    total_score = 0
    
    questions = [
        {"text": "I am comfortable with the possibility of losing some or all of my initial investment.", "weight": 1},
        {"text": "I prefer stable and consistent returns over the potential for higher returns with more volatility.", "weight": 2},
        {"text": "I am willing to invest in high-risk assets for the possibility of high returns.", "weight": 3},
        {"text": "I have a long-term investment horizon and can tolerate short-term market fluctuations.", "weight": 2},
        {"text": "I like to closely monitor my investments and make adjustments based on market conditions.", "weight": 1},
        {"text": "I have a good understanding of different investment options and their associated risks.", "weight": 2},
        {"text": "I am willing to invest a significant portion of my portfolio in stocks or equities.", "weight": 3},
        {"text": "I am comfortable with investing in emerging markets or new technologies.", "weight": 2},
        {"text": "I prefer low-risk investments even if they offer lower potential returns.", "weight": 1},
        {"text": "I am willing to accept short-term losses for the potential of long-term gains.", "weight": 3},
        {"text": "I have experienced significant losses in investments before and remained invested.", "weight": 2},
        {"text": "I tend to follow the advice of financial experts or advisors when making investment decisions.", "weight": 1},
        {"text": "I am close to retirement and prioritize preserving my capital over maximizing returns.", "weight": 1},
        {"text": "I enjoy actively trading and speculating in financial markets.", "weight": 3},
        {"text": "I have a low tolerance for market volatility and prefer stable investment options.", "weight": 1},
        {"text": "I aim for steady, predictable returns in my investment portfolio.", "weight": 2},
        {"text": "I am open to investing in alternative assets like real estate or commodities.", "weight": 2},
        {"text": "I often conduct thorough research before making any investment decisions.", "weight": 2},
        {"text": "I consider my investments a long-term commitment and rarely make impulsive changes.", "weight": 3},
        {"text": "I enjoy learning about financial markets and investment strategies.", "weight": 3}
    ]
    
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
    determine_risk_appetite()
