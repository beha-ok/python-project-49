import prompt
from random import randint


def user_game():
    name_user = prompt.string("May I have your name? ")
    print(f'Hello, {name_user}!')
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no"')
    while count < 3:
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            if answer == 'yes':
                count += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                return print(f"Let's try again, {name_user}!")
        elif random_number % 2 != 0:
            if answer == 'no':
                count += 1
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                return print(f"Let's try again, {name_user}!")
    return print(f'Congratulations, {name_user}!')


def main():
    user_game()


if __name__ == '__main__':
    main()
