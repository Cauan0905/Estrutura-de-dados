class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def esta_vazia(self):
        return self.inicio is None

    def tamanho(self):
        contador = 0
        atual = self.inicio
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador

    def obter_valor(self, posicao):
        if posicao < 1 or posicao > self.tamanho():
            raise IndexError("Posição inválida")
        atual = self.inicio
        for _ in range(1, posicao):
            atual = atual.proximo
        return atual.valor

    def modificar_valor(self, posicao, novo_valor):
        if posicao < 1 or posicao > self.tamanho():
            raise IndexError("Posição inválida")
        atual = self.inicio
        for _ in range(1, posicao):
            atual = atual.proximo
        atual.valor = novo_valor

    def inserir(self, posicao, valor):
        if posicao < 1 or posicao > self.tamanho() + 1:
            raise IndexError("Posição inválida")

        novo_no = No(valor)

        if posicao == 1:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            anterior = self.inicio
            for _ in range(1, posicao - 1):
                anterior = anterior.proximo
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no

    def remover(self, posicao):
        if posicao < 1 or posicao > self.tamanho():
            raise IndexError("Posição inválida")

        if posicao == 1:
            removido = self.inicio
            self.inicio = self.inicio.proximo
        else:
            anterior = self.inicio
            for _ in range(1, posicao - 1):
                anterior = anterior.proximo
            removido = anterior.proximo
            anterior.proximo = removido.proximo
        return removido.valor

    def imprimir(self):
        atual = self.inicio
        elementos = []
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        print(" -> ".join(elementos) if elementos else "Lista vazia")


# Casos de teste
if __name__ == "__main__":
    lista = ListaEncadeada()

    print("Lista vazia?")
    print(lista.esta_vazia())  

    print("\nInserindo valores...")
    lista.inserir(1, 7)
    lista.inserir(2, 10)
    lista.inserir(3, 27)
    lista.inserir(2, 9) 
    lista.imprimir()  

    print("\nTamanho da lista:", lista.tamanho())  

    print("\nValor na posição 3:", lista.obter_valor(3))  

    print("\nModificando valor da posição 2 para 99")
    lista.modificar_valor(2, 100)
    lista.imprimir()  

    print("\nRemovendo elemento da posição 1")
    removido = lista.remover(1)
    print(f"Removido: {removido}")
    lista.imprimir()  

    print("\nRemovendo elemento da posição 2")
    lista.remover(2)
    lista.imprimir() 

    print("\nLista vazia?")
    print(lista.esta_vazia())
