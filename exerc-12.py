import random

def get_first_and_last(item_list):
    return_list = []

    if item_list:
        return_list.append(item_list[0])
        return_list.append(item_list[-1])
    return return_list

def main():
    random_list = range(0, 100, 2)
    empty_list = []

    print('\n New List: {}'.format(get_first_and_last(random_list)))
    print('\n  Empty list: {}'.format(get_first_and_last(empty_list)))

if __name__ == "__main__":
    main()