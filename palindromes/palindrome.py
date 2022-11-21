# first of all design a function to save the palindrome
def palindrome(word):
    word = word.lower()
    word = word.replace(' ', '')
    up_word = word[::-1]
    if up_word == word:
        return True
    else:
        return False

# second make other function to conditionals
def main():
    word = input('Write your idea: ')
    if  palindrome(word) == True:
        print('It is a palindrome')
    else:
        print('It is not a palindrome')

# use entry point
if __name__ == '__main__':
    main()
