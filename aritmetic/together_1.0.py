import random

def run():
    option = int(input('Choose an option to start (1, 2, 3, 4): '))
    if option == 1:
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

    if option == 2:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        #first_number = str(first_number)
        #second_number = str(second_number)
        print(first_number)
        print(' - ')
        print(second_number)

        answer = first_number - second_number
        answer = int(answer)

        user = int(input('Write the answer:  '))
        # I think I should fix below
        if answer == user:
            print('You are right')
        else:
            print('You are wrong')

    if option == 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        #first_number = str(first_number)
        #second_number = str(second_number)
        print(first_number)
        print(' * ')
        print(second_number)

        answer = first_number * second_number
        answer = int(answer)

        user = int(input('Write the answer:  '))
        # I think I should fix below
        if answer == user:
            print('You are right')
        else:
            print('You are wrong')

    if option == 4:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        #first_number = str(first_number)
        #second_number = str(second_number)
        print(first_number)
        print(' / ')
        print(second_number)

        answer1 = first_number / second_number
        answer2 = first_number % second_number
        answer_u = answer1 + answer2
        answer_u = int(answer_u)

        user = int(input('Write the answer:  '))
        # I think I should fix below
        if answer_u == user:
            print('You are right')
        else:
            print('You are wrong')

    else:
        print('Choose a posible input please')

if __name__ == '__main__':
    run()
