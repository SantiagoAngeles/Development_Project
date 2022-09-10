import random


def run():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    answer = first_number + second_number
    while answer == True:
        return True
        
    if answer == True:
        print('You are right!')
    else:
        print('Try again')


if __name__ == '__main__':
    run()