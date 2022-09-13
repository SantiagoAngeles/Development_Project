def text(input):
    message = message.replace(' ', '')
    message = message.lower()
    abecedary = ('a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    for message in abecedary:
        if message == abecedary:
            return True
        else:
            continue


def main():
    message = str(input('Write your message: '))
    if message == True:
        print('Your encrypted message is: ' + message)
    else:
        print('something went wrong :(')


if __name__ == '__main__':
    main()
