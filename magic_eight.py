from random import randrange

def ask_question():
    x= input('What is your question?')
    return 'Your question is: ' + x

answers = ["Is it certain", "As I see it, yes", "It is decidely so", "Most likely", "Reply hazy try again", "Don't count on it", "Ask again later", "My reply is no", "Without a doubt", "Outlook good", "Better not tell you now", "My sources say no", "Yes definitely", "Yes", "Cannot predict now", "Outlook not so good", "You may rely on it", "Signs point to yes", "Concentrate and ask again", "Very doubtful"]
i = randrange(answers)
