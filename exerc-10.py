import random

def random_range():
    return [random.randint(0, 10) for i in range(0, 20)]

def main(): 
    range_one = random_range()
    range_two = random_range()
    intersection = []

    print('Range one: {} \n'.format(range_one))
    print('Range two: {} \n'.format(range_two))

    for i in range_one:
        for j in range_two:
            if i == j and i not in intersection:
                intersection.append(i)

    print('intersection: {}'.format(intersection))

if __name__ == '__main__':
    main()
