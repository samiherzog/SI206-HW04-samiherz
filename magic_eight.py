from random import randrange

def ask_question():
    x= input('What is your question?')
    return 'Your question is: ' + x

def get_answer():
    answers = ["Is it certain", "As I see it, yes", "It is decidely so", "Most likely", "Reply hazy try again", "Don't count on it", "Ask again later", "My reply is no", "Without a doubt"]
    i = randrange(len(answers))
    return answers[i]
