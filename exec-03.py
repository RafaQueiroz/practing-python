def get_user_number():
    return int(input('Please, inform a number \n'))

def get_lesser_list(number):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = []
    for item in a:
        if item < number:
            result.append(item) 

    return result

def main():

    input_filter = get_user_number()
    lesser_list = get_lesser_list(input_filter)

    if(len(lesser_list) > 0 ):
        print('lesser than {} list: {} \n'.format(input_filter, lesser_list))
    else:
        print('Ops! It seems that there is no number lesser than {}'.format(input_filter))

if __name__ == '__main__':
    main()
