def suma_numeros(numero1: int, numero2: int) -> int:
    """
    Realiza la suma de dos numeros
    :param numero1: int
    :param numero2: int
    :return: numero1 + numero2
    """
    return numero1 + numero2

def resta_numeros(numero1: int, numero2: int) -> int:
    """
    Realiza la resta de dos numeros
    :param numero1: int
    :param numero2: int
    :return: numero1 - numero2
    """
    return numero1 - numero2

def multiplicacion_numeros(numero1: int =4, numero2: int=4) -> int:
    """
    Realiza la Multiplicacion de dos numeros
    :param numero1: int
    :param numero2: int
    :return: numero1 * numero2
    """
    return numero1 * numero2

def divicion_numeros(dividendo: float =4, divisor: float=4) -> float:
    """
    Realiza la divicion de dos numeros, si el divisor es 0 retorna None
    :param dividendo: int
    :param divisor: int
    :return: dividendo / divisor
    """
    if divisor == 0:
        return None
    return (dividendo / divisor)

if __name__ == '__main__':
    print(suma_numeros(3, 4))
    print(resta_numeros(3, 4))
    print(multiplicacion_numeros(8,8))
    print(multiplicacion_numeros(numero1=20, numero2=20))
    print(divicion_numeros())