from random import randrange

def ask_question():
    x= input('What is your question?')
<<<<<<< HEAD
    while '?' not in x:
        print('I am sorry, I can only answer questions')
        x= input('What is your question?')
    while x =! 'Quit':
        x= input('What is your quesiton?')
=======
    return 'Your question is: ' + x

def get_answer():
    answers = ["Is it certain", "As I see it, yes", "It is decidely so", "Most likely", "Reply hazy try again", "Don't count on it", "Ask again later", "My reply is no", "Without a doubt"]
    i = randrange(len(answers))
    return answers[i]
>>>>>>> 1aeec89030394c4dd7306a84058771a22d7179ae
