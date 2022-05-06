# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random


def print_hi(name):
    print('---------------Welcome!-----------------')
    print()
    print(f'Hi, {name}')


def generate_number():
    num = random.randint(1, 100)
    return num


def is_valid(text):
    try:
        return 0 <= int(text) <= 100
    except ValueError:
        return False


def user_input(guessed):
    # print(guessed)

    flag = False
    counter = 0
    while flag == False:
        num = input('Guess the number: ')
        if is_valid(num):
            if int(num) < guessed:
                counter += 1
                print('More...')
            elif int(num) > guessed:
                counter += 1
                print('Smaller...')
            else:
                flag = True
        else:
            print('You must enter a number from 0 to 100')
            continue

    print()
    print(f'You guessed! It was number {num}. Attempts {counter}.')
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('this program guesses the number')
    again = 'yes'
    while True:
        if again == 'yes':
            user_input(generate_number())
            again = input('Repeat? Enter "yes" to repeat or press "Enter" to end: ')
        else:
            print()
            print('-------------Thanks, bye!---------------')
            break
