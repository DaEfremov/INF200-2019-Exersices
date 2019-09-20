__author__ = 'Daniil Efremov'
__email__ = 'daniil.vitalevich.efremov@nmbu.no'

from random import randint as rand_num


def negative_checker():
    guessed_int = 0
    while guessed_int < 1:
        guessed_int = int(input('Your guess: '))
    return guessed_int


def rand_int():
    return rand_num(2, 12)


def equal_checker(right_num, guessed_num):
    return right_num == guessed_num


if __name__ == '__main__':

    num_of_guesses = 3
    win_condition = False

    while win_condition is False and num_of_guesses > 0:

        win_condition = equal_checker(rand_int(), negative_checker())

        if win_condition is False:
            print('Wrong, try again!')
            num_of_guesses -= 1

    if num_of_guesses > 0:
        print('You won {} points.'.format(num_of_guesses))
    else:
        print('You lost. Correct answer: {}.'.format(rand_int()))
