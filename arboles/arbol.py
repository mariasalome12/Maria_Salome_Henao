import tkinter as tk

class Nodo:
    def __init__(self, valor):
        """

        :param valor: ingresa un valor al árbol

        """
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Visualizacion:
    def __init__(self, raiz):
        """

        :param raiz: ingresa la raiz del arbol para luego
        visualizarla en una ventana emergente

        """
        self.raiz = raiz
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()

    def dibujar(self, nodo, x, y, dx):
        """

        :param nodo: nodo del arbol
        :param x: coordenada en posicion horizontal
        :param y: coordenada en posicion vertical
        :param dx: distancia horizontal
        :return:

        """
        if nodo:
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(nodo.valor))
            if nodo.izquierda:
                self.canvas.create_line(x, y, x - dx, y + 50)
                self.dibujar(nodo.izquierda, x - dx, y + 50, dx // 2)
            if nodo.derecha:
                self.canvas.create_line(x, y, x + dx, y + 50)
                self.dibujar(nodo.derecha, x + dx, y + 50, dx // 2)

    def visualizararbol(self):
        self.dibujar(self.raiz, 200, 50, 100)

    def retorno(self):
        self.window.mainloop()

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self.recursivo(self.raiz, valor)

    def recursivo(self, nodo, valor):
        """

        :param nodo: crea un nodo
        :param valor: un valor que se va a encontrar en un nodo
        :return:

        """
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.recursivo(nodo.izquierda, valor)

        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.recursivo(nodo.derecha, valor)

    def postorder(self, nodo):
        if nodo:
            self.postorder(nodo.izquierda)
            self.postorder(nodo.derecha)
            print(nodo.valor, end=" ")

    def preorder(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorder(nodo.izquierda)
            self.preorder(nodo.derecha)

    def inorder(self, nodo):
        if nodo:
            self.inorder(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorder(nodo.derecha)

    def altura(self, nodo):
        if nodo is None:
            return 0
        altura_izq = self.altura(nodo.izquierda)
        altura_derec = self.altura(nodo.derecha)
        return max(altura_izq, altura_derec) + 1

    def es_completo(self, nodo):
        if nodo is None:
            return True
        if nodo.izquierda is None and nodo.derecha is None:
            return True
        if nodo.izquierda is not None and nodo.derecha is not None:
            return self.es_completo(nodo.izquierda) and self.es_completo(nodo.derecha)
        return False

    def contador(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contador(nodo.izquierda) + self.contador(nodo.derecha)

    def eliminar(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            print("El valor a eliminar debe ser un número entero positivo.")
            return
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._minimo_valor(nodo.derecha)
            nodo.derecha = self._eliminar(nodo.derecha, nodo.valor)

        return nodo

    def _minimo_valor(self, nodo):
        valor_actual = nodo
        while valor_actual.izquierda is not None:
            valor_actual = valor_actual.izquierda
        return valor_actual.valor


if __name__ == "__main__":
    arbol = ArbolBinario()

    while True:
        opcion = input("Marca -1 para recibir nodos infinitos, x para detener o un número entero positivo para insertar en el árbol : ")

        if opcion == "x":
            break

        elif opcion == "-1":
            continue
        try:
            valor = int(opcion)
            if valor >= 0:
                arbol.insertar(valor)
            else:
                print("El valor a ingresar debe ser un número entero positivo")
        except ValueError:
            print("El valor a ingresar debe ser un número entero positivo")

    visual = Visualizacion(arbol.raiz)

    while True:
        print("\nBienvenido:")
        print("1---> Recorrido PostOrder")
        print("2---> Recorrido PreOrder")
        print("3---> Recorrido InOrder")
        print("4---> Numero de Hojas")
        print("5---> Altura")
        print("6---> Es completo")
        print("7---> Numero de Nodos")
        print("8---> Eliminar Nodo")
        eleccion = input("Selecciona una opción o usa S para salir: ")

        if eleccion == "S":
            break
        elif eleccion == "1":
            print("Recorrido PostOrder:")
            arbol.postorder(arbol.raiz)

        elif eleccion == "2":
            print("Recorrido PreOrder:")
            arbol.preorder(arbol.raiz)

        elif eleccion == "3":
            print("Recorrido InOrder:")
            arbol.inorder(arbol.raiz)

        elif eleccion == "4":
            print("Número de Hojas:", arbol.contador(arbol.raiz))

        elif eleccion == "5":
            print("Altura del árbol:", arbol.altura(arbol.raiz))

        elif eleccion == "6":
            if arbol.es_completo(arbol.raiz):
                print("El árbol es completo.")
            else:
                print("El árbol no es completo.")

        elif eleccion == "7":
            print("Número de Nodos:", arbol.contador(arbol.raiz))

        elif eleccion == "8":
            valor_eliminar = input("Ingrese el valor del nodo que desea eliminar: ")
            if not isinstance(valor_eliminar, int) or valor_eliminar <= 0:
                print("El valor a eliminar debe ser un número entero positivo.")
            else:
                arbol.eliminar(valor_eliminar)


    visual.visualizararbol()
    visual.retorno()


# El arbol tiene dos nuevas cosas, una es que se pueden eliminar nodos del arbol y otra es una gráfica al finalizar la ejecución del arbol