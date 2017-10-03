import random

def random_range():
    rand_range = []
    
    for i in range(1, random.randint(1, 100)):
        rand_range.append(random.randint(0, 100))
    
    return rand_range

def main():
    range_one = random_range()
    range_two = random_range()

    equals = []
    
    for i in range_one:
        for j in range_two:
            if i == j and i not in equals:
                equals.append(i)

    
    print('Range one: {}'.format(range_one))
    print('Range two: {}'.format(range_two))
    print('Intersection of both ranges: {}'.format(equals))


if __name__ == '__main__':
    main()
