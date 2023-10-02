# app.py

from flask import Flask, render_template, request, redirect, url_for
from risk_determination import determine_risk_appetite
from questions_loader import load_questions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        num_questions = int(request.form['num_questions'])
        return redirect(url_for('questions', num_questions=num_questions))

    return render_template('index.html')

@app.route('/questions/<int:num_questions>', methods=['GET', 'POST'])
def questions(num_questions):
    questions_data = load_questions('questions.json')

    if request.method == 'POST':
        user_responses = [request.form[f'question{i + 1}'] for i in range(num_questions)]
        risk_appetite = determine_risk_appetite(user_responses, questions_data)
        return render_template('result.html', risk_appetite=risk_appetite)

    return render_template('questions.html', num_questions=num_questions, questions=questions_data)

if __name__ == '__main__':
    app.run(debug=True)
