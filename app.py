# app.py

from flask import Flask, render_template, request, redirect, url_for
from risk_determination import determine_risk_appetite
from questions_loader import load_questions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    """Handle the initial questionnaire page."""
    if request.method == 'POST':
        num_questions = int(request.form['num_questions'])
        return redirect(url_for('questions', num_questions=num_questions))

    return render_template('index.html')

@app.route('/questions/<int:num_questions>', methods=['GET', 'POST'])
def questions(num_questions):
    """Handle the questionnaire page with specified number of questions."""
    questions_data = load_questions('questions.json')

    if request.method == 'POST':
        # Extract user responses from the form
        user_responses = [request.form[f'question{i + 1}'] for i in range(num_questions)]
        
        # Determine risk appetite based on user responses
        risk_appetite = determine_risk_appetite(user_responses, questions_data)

        # Prepare data for template
        user_responses_with_questions = [{'question': question, 'response': response} for question, response in zip(questions_data[:num_questions], user_responses)]

        # Write a detailed summary to a text file
        with open('summary.txt', 'w') as file:
            file.write('Risk Appetite: {}\n'.format(risk_appetite))
            file.write('User Responses:\n')
            for i, (question, response) in enumerate(zip(questions_data[:num_questions], user_responses), start=1):
                file.write('Question {}: {}\n'.format(i, question['text']))  # Include question text
                file.write('  User Response: {}\n'.format(response))
            file.write('Summary Numbers: {}\n'.format(", ".join(str(i) for i in user_responses)))

        return render_template('result.html', risk_appetite=risk_appetite, user_responses_with_questions=user_responses_with_questions)

    return render_template('questions.html', num_questions=num_questions, questions=questions_data)

if __name__ == '__main__':
    app.run(debug=True)
