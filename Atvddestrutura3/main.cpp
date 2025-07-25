#include <iostream>
#include "lista_sequencial.h"

using namespace std;

void criarLista(Lista& l) {
    l.tamanho = 0;
}

bool estaVazia(const Lista& l) {
    return l.tamanho == 0;
}

bool estaCheia(const Lista& l) {
    return l.tamanho == MAX;
}

int obterTamanho(const Lista& l) {
    return l.tamanho;
}

bool obterElemento(const Lista& l, int posicao, int& valor) {
    if (posicao < 1 || posicao > l.tamanho) return false;
    valor = l.dados[posicao - 1];
    return true;
}

bool modificarElemento(Lista& l, int posicao, int novoValor) {
    if (posicao < 1 || posicao > l.tamanho) return false;
    l.dados[posicao - 1] = novoValor;
    return true;
}

bool inserirElemento(Lista& l, int posicao, int valor) {
    if (estaCheia(l) || posicao < 1 || posicao > l.tamanho + 1) return false;
    for (int i = l.tamanho; i >= posicao; --i) {
        l.dados[i] = l.dados[i - 1];
    }
    l.dados[posicao - 1] = valor;
    l.tamanho++;
    return true;
}

bool removerElemento(Lista& l, int posicao) {
    if (posicao < 1 || posicao > l.tamanho) return false;
    for (int i = posicao; i < l.tamanho; ++i) {
        l.dados[i - 1] = l.dados[i];
    }
    l.tamanho--;
    return true;
}

// Exemplo de teste
int main() {
    Lista lista;
    criarLista(lista);

    inserirElemento(lista, 1, 10);
    inserirElemento(lista, 2, 20);
    inserirElemento(lista, 2, 15); // agora lista: 10, 15, 20

    cout << "Tamanho da lista: " << obterTamanho(lista) << endl;

    for (int i = 1; i <= obterTamanho(lista); ++i) {
        int valor;
        obterElemento(lista, i, valor);
        cout << "Elemento " << i << ": " << valor << endl;
    }

    modificarElemento(lista, 2, 99);
    removerElemento(lista, 1);

    cout << "Após modificações:" << endl;
    for (int i = 1; i <= obterTamanho(lista); ++i) {
        int valor;
        obterElemento(lista, i, valor);
        cout << "Elemento " << i << ": " << valor << endl;
    }

    return 0;
}
