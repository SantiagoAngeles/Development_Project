import random
number = random.randrange(1, 50)


def main():
    lives = 5
    guess = int((input('Guess the number: ')))
    
    while guess != number:
        if guess < number:
            print('Try greater :(')
            lives = lives - 1
            guess = int(input('Guess the number again '))
        else:
            print('Try lower :(')
            lives = lives - 1
            guess = int(input('Guess the number again '))
        
        if lives == 0:
            print('You have lost')
            break
    
    if lives > 0 or guess == number:
        print('You have won :)')


if __name__ == '__main__':
    main()
