import json
import random

def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    
    random.shuffle(questions)
    return questions
