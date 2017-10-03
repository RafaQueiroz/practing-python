def main():
    number = int(input('Please, Give an number: \n'))

    returnSentence = 'Your number is '

    if number % 2 == 0:
        returnSentence += 'even'
    else:
        returnSentence += 'odd'

    print(returnSentence)

if __name__ == '__main__':
    main()