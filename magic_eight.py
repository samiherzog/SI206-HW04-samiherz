from random import randrange
def ask_question():
    x= input('What is your question?')
    return 'Your question is: ' + x






# This is me adding branch add_questionsC

def get_answerC():

    answers = ["Yes definitely" , "You may rely on it", "Yes", "Signs point to yes",
        "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
        "My sources say no", "Outlook not so good", "Very doubtful"]
    index = randrange(len(answers))
    answer = answers[index]
    return answer
