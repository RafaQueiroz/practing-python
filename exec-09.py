import random

def gen_rand_number():
    return random.randint(1, 10)

def main():
    rand_number = gen_rand_number()
    number_guessed = int(input('Im thinking on a number... Try to guess it \n '))

    while number_guessed != rand_number:
        if number_guessed > rand_number:
            number_guessed = int(input('Ops! Your number is higher. Try another \n'))
        elif number_guessed < rand_number:
            number_guessed = int(input('Ops! Your number is lesser. Try another \n'))

    print('Congratulations! You guessed right')

if __name__ == '__main__':
    main()