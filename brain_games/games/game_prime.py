from random import randint


game_offer = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def raund():
    random_number = randint(0, 30)
    random_number
    if random_number < 2:
        return random_number, 'no'
    start_num = 2
    while start_num <= random_number / 2:
        if random_number % start_num == 0:
            return random_number, 'no'
        start_num += 1
    return random_number, 'yes'
