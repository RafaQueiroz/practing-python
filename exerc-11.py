
def get_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i:
            divisores.append(i)
    return divisores

def main():
    numero = int(input('Number: \n')) 
    divisores = get_divisores(numero)

    if len(divisores) > 1:
        print('{} não é primo'.format(numero))
    else:
        print('{} é primo'.format(numero))

if __name__ == '__main__':
    main()
