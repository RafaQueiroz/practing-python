def main():

    text = str(input('insert some text and check if it is a palindrome \n'))
    text = text.replace(' ', '')

    if text == text[::-1]:
        print('It is a palindrome \n')
    else:
        print('It is not a palindrome \n')

if __name__ == '__main__':
    main()
