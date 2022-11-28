import random

def run():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    #first_number = str(first_number)
    #second_number = str(second_number)
    print(first_number)
    print(' + ')
    print(second_number)

    answer = first_number + second_number
    answer = int(answer)

    user = int(input('Write the answer:  '))
    # I think I should fix below
    if answer == user:
        print('You are right')
    else:
        print('You are wrong')


if __name__ == '__main__':
    run()

