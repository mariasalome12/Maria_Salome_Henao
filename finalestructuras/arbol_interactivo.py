class Arbol_Binario:
    def __init__(self, valor, izquierda=None, derecha=None):
        """

        :param valor: valor para el nodo
        :param izquierda: direccion
        :param derecha: direccion
        """
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


def Callback(nodo):
    """

    :param nodo: recibe el nodo que se ha ingresado
    :return: el callback
    """
    print(f"callback({nodo.valor})")


def Arbol_interactivo(raiz, callback):
    """

    :param raiz: nodo padre
    :param callback: en el nodo que están en ese momento
    :return: los nodos organizados
    """
    stack = []
    current = raiz

    while stack or current:
        if current:
            stack.append(current)
            current = current.izquierda
        else:
            current = stack.pop()
            callback(current)
            current = current.derecha


def insertar_nodo(raiz, valor):
    """

    :param raiz: nodo padre
    :param valor: valor del nodo ingresado
    :return: nuevo nodo
    """
    if not isinstance(valor, int) and valor.lower() != 's':
        print("Valor incorrecto. Por favor, ingrese un número entero o 's'.")
        return raiz

    nuevo_nodo = Arbol_Binario(valor)
    if raiz is None:
        return nuevo_nodo

    current = raiz
    while True:
        if valor < current.valor:
            if current.izquierda is None:
                current.izquierda = nuevo_nodo
                break
            else:
                current = current.izquierda
        else:
            if current.derecha is None:
                current.derecha = nuevo_nodo
                break
            else:
                current = current.derecha

    return raiz


if __name__ == "__main__":
    arbol_ = None

    while True:
        valor = input("Ingresa el valor del nodo o s para detenerse: ")

        if valor.lower() == 's':
            break

        try:
            valor = int(valor)
        except ValueError:
            print("el valor ingresado es incorrecto, por favor intente nuevamente  ")
            continue

        arbol_ = insertar_nodo(arbol_, valor)
        Arbol_interactivo(arbol_, Callback)
