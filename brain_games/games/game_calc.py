from random import choice, randint


game_offer = 'What is the result of the expression?'


def raund():
    game_offer
    operators = ['*', '+', '-']
    random_operator = choice(operators)
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    questions = (f'{num_1} {random_operator} {num_2}')
    result_questions = eval(f'{num_1} {random_operator} {num_2}')
    return questions, str(result_questions)
