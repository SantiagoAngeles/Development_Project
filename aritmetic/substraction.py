import random

def run(first_number, answer):
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    print(first_number)
    print(' + ')
    print(second_number)
    
    # I dunno how use this function

    ## answer = first_number + second_number
    
    # how I define 'answer'?

    user = int(input('Write the answer:  '))
    
    if user == answer:
        print('You are right')
    else:
        print('You are wrong')


menu = """

1 - adition
2 - subtraction
3 - multiply
4 - divide

"""

option = int(input(menu))
if option == 1:
    run(first_number + second_number)
if option == 2:
    run(first_number - second_number)
if option == 3:
    run(first_number * second_number)
if option == 4:
    run(first_number / second_number)
else:
    print('Choose a posible option please')


if __name__ == '__main__':
    run()
