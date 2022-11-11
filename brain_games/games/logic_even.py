from random import randint


game_offer = f'Answer "yes" if the number is even, otherwise answer "no"'

def raund():
    random_number = randint(0, 30)
    if random_number % 2 == 0:
        result_questions = 'yes'
    elif random_number % 2 == 1:
        result_questions = 'no'
    return random_number, result_questions

