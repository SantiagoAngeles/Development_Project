import random

def run():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    print(first_number)
    print(' + ')
    print(second_number)
    
    answer = first_number + second_number
    
    user = int(input('Write the answer:  '))
    # I think I should fix below
    if user == answer:
        print('You are right')
    else:
        print('You are wrong')


if __name__ == '__main__':
    run()
