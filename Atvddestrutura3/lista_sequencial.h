#ifndef LISTA_SEQUENCIAL_H
#define LISTA_SEQUENCIAL_H

const int MAX = 100;

struct Lista {
    int dados[MAX];
    int tamanho;
};

// 1. Criação da lista vazia
void criarLista(Lista& l);

// 2. Verificar se a lista está vazia
bool estaVazia(const Lista& l);

// 3. Verificar se a lista está cheia
bool estaCheia(const Lista& l);

// 4. Obter o tamanho da lista
int obterTamanho(const Lista& l);

// 5. Obter o valor de uma posição
bool obterElemento(const Lista& l, int posicao, int& valor);

// 5. Modificar o valor de uma posição
bool modificarElemento(Lista& l, int posicao, int novoValor);

// 6. Inserir elemento em uma posição
bool inserirElemento(Lista& l, int posicao, int valor);

// 7. Remover elemento de uma posição
bool removerElemento(Lista& l, int posicao);

#endif
