# coverting Dollars to Pesos

def run():
    dollar = float(input('How much dollars do you have?:  '))
    peso_value = 20
    equivalent_dp = dollar * peso_value
    equivalent_dp = str(equivalent_dp)
    print(' You got ' + equivalent_dp + ' pesos ')


if __name__ == '__main__':
    run()
