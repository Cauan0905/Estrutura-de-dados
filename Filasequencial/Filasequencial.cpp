#include "FilaSequencial.h"
#include <iostream>

FilaSequencial::FilaSequencial() {
  tamanhoMaximo = 5;
  tamanhoAtual = 0;
  dados = new int[tamanhoMaximo];
  inicio = 0;
  fim = -1;
}

FilaSequencial::~FilaSequencial() {
  delete[] dados;
}

bool FilaSequencial::vazia() {
  return tamanhoAtual == 0; 
}

bool FilaSequencial::cheia() {
  return tamanhoAtual == tamanhoMaximo;
}

int FilaSequencial::getTamanho() {
  return this->tamanhoAtual;
}

int FilaSequencial::getPrimeiro() {
  if (this->vazia())
    return -1;
  return dados[inicio];
}

bool FilaSequencial::InserirElemento(int conteudo) {
  if (this->cheia())
    return false;
  if (fim < this->tamanhoMaximo - 1) {
    fim++;
  } else {
    fim = 0;
  }
  dados[fim] = conteudo;
  tamanhoAtual++;
  return true;
}

int FilaSequencial::RemoverElemento() {
  if (this->vazia())
    return -1;
  int retorno = this->getPrimeiro();
  if (inicio < this->tamanhoMaximo - 1) {
    inicio++;
  } else {
    inicio = 0;
  }
  tamanhoAtual--;
  return retorno;
}
