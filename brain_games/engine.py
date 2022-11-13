from prompt import string


def engine_games(game):
    count = 0
    print("Welcome to the Brain Games!")
    user_name = string("May I have your name? ")
    print(f'Hello, {user_name}')
    print(f'{game.game_offer}')
    while count < 3:
        questions, result_questions = game.raund()
        print(f"Question: {questions}")
        answer = string('Your answer: ')
        if answer != result_questions:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{result_questions}'")
            print(f"Let's try again, {user_name}!")
            break
        count += 1
        print('Correct!')
    else:
        print(f"Congratulations, {user_name}!")
