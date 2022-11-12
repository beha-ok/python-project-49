from random import randint, choice


game_offer = 'What number is missing in the progression?'


def raund():
    tuple_step = range(3, 5)
    random_step = choice(tuple_step)
    random_number_start = randint(2, 5)
    random_number_stop = randint(45, 49)
    questions = list(range(random_number_start, random_number_stop, random_step))
    result_questions = choice(questions) #рандомное число для индекса
    index_random_number = questions.index(result_questions)
    questions[index_random_number] = '..'
    questions = ' '.join(map(str, questions))
    return questions, str(result_questions)
