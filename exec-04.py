def main():
    number = int(input('Please, insert a number \n'))

    divisors = []

    for i in range(1, number+1):
        if number % i == 0 :
            divisors.append(i)

    print('All divisors of {} are : {}'.format(number, divisors))

if __name__ == '__main__':
    main()