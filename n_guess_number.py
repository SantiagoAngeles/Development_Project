import random
number = random.randrange(1, 50)

def main():
    guess = int((input('Guess the number: ')))
    # number = int(number)
    while guess != number:
        if guess < number:
            print('Try greater :(')
            guess = int(input('Guess the number again'))
        else:
            print('Try lower :(')
            guess = int(input('Guess the number again'))
    
    print('You have won :)')

if __name__ == '__main__':
    main()
