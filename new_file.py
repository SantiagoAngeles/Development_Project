def run():
    initial = str(input('Type your idea'))

    initial = initial.replace(' ', '')
    initial = initial.lower()
    palindrome = initial[::-1]

    if initial == palindrome:
        print(initial + 'It is a palidrome')
    else:
        print(initial + 'It is not a palindrome')


if __name__ == '__main__':
    run()
