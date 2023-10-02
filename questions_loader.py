# questions_loader.py

import json

def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions
