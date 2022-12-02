import random

# implement functions use better the code

def run():
    option = int(input('Choose an option to start (1, 2, 3, 4): '))

    if option == 1:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        
        print(first_number)
        print('(+)')
        print(second_number)
        
        answer = first_number + second_number
        answer = int(answer)
        
        user = int(input('Write the answer:  '))
        
        if answer == user:
            print('You are right')
        else:
            print('You are wrong')

    elif option == 2:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
    
        print(first_number)
        print('(-)')
        print(second_number)

        answer = first_number - second_number
        answer = int(answer)
        
        user = int(input('Write the answer:  '))
        
        if answer == user:
            print('You are right')
        else:
            print('You are wrong')

    elif option == 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        
        print(first_number)
        print('(*)')
        print(second_number)
        
        answer = first_number * second_number
        answer = int(answer)
        
        user = int(input('Write the answer:  '))
         
        if answer == user:
            print('You are right')
        else:
            print('You are wrong')

    elif option == 4:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 10)
                
        print(first_number)
        print('(/)')
        print(second_number)
        
        answer_int = first_number / second_number
        # answer_dec = first_number % second_number
        answer_ult = answer_int # + answer_dec
        answer_ult = float(answer_ult)
        answer_ult = round(answer_ult, 2)
        
        user = float(input('Write the answer:  '))
        user = round(user, 2)

        if answer_ult == user:
            print('You are right')
        else:
            print('You are wrong') 
    
    else:
        print('Choose a posible input please')

if __name__ == '__main__':
    run()
