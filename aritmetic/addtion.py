import random

def run():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    print(first_number)
    print(' + ')
    print(second_number)

    answer = first_number + second_number
    user = input('Write the answer:  ')
    while user == answer:
        return True
        
    if user == True:
        print('You are right!')
    elif user == False:
        print('Try again')


if __name__ == '__main__':
    run()