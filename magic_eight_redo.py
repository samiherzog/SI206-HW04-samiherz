from random import randrange
def ask_question():
    x= input('What is your question?')
# <<<<<<< HEAD
    if '?' not in x:
        print('I am sorry, I can only answer questions')
        x= input('What is your question?')
    if x != 'Quit':

# =======
        print('Your question is: ' + x)

# <<<<<<< HEAD
    return get_answerC()


# This is me adding branch add_questionsC

def get_answerC():

    answers = ["Yes definitely" , "You may rely on it", "Yes", "Signs point to yes",
        "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
        "My sources say no", "Outlook not so good", "Very doubtful"]
    index = randrange(len(answers))
    # answer = answers[index]
    # return answer
# =======
# def get_answer():
    more_answers = ["Is it certain", "As I see it, yes", "It is decidely so", "Most likely", "Reply hazy try again", "Don't count on it", "Ask again later", "My reply is no", "Without a doubt"]
    i = randrange(len(answers))
    for c in more_answers:
        answers.append(c)
    answer = answers[i]
    return answers[i]
# >>>>>>> 1aeec89030394c4dd7306a84058771a22d7179ae
# >>>>>>> cd1eb038158dfe11e8b96aec20305dc1652642d0

ask_question()
print(get_answerC())
