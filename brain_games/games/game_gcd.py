from random import randint
from math import gcd


game_offer = 'Find the greatest common divisor of given numbers.'


def raund():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    questions = f'{random_number_1} {random_number_2}'
    result_questions = gcd(random_number_1, random_number_2)
    return questions, str(result_questions)
