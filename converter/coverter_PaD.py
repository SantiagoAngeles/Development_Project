# to convert pesos to dollars
def main():
    pesos = float(input('How muhc pesos do you have:  '))
    dollar_value = 20
    dollar = pesos / dollar_value
    dollar = str(dollar)
    print('You got ' + dollar + ' dollars ')


if __name__ == '__main__':
    main()
