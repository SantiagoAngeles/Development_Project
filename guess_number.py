import random # paquete de código de funciones para trabajar con la
              # aleatoriedad del lenguaje


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio: # todo lo que está debajo de
                                              # while es una vuelta en el ciclo
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!') # si no pasa lo que en el condicional while dice
                       # se imprime el mensaje


if __name__ == '__main__':
    run()