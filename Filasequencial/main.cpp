#include "FilaSequencial.h"
#include <iostream>

int main() {
  FilaSequencial *fila = new FilaSequencial();

  std::cout << "Fila vazia? " << (fila->vazia() ? "Sim" : "Não") << std::endl;

 
  for (int i = 10; i <= 16; i++) { 
    std::cout << "Inserindo " << i << ": ";
    if (fila->InserirElemento(i))
      std::cout << "Sucesso";
    else
      std::cout << "Falha (Fila cheia)";
    std::cout << std::endl;
  }

  std::cout << "Fila cheia? " << (fila->cheia() ? "Sim" : "Não") << std::endl;

  std::cout << "Primeiro elemento: " << fila->getPrimeiro() << std::endl;

  for (int i = 0; i < 7; i++) { 
    int removido = fila->RemoverElemento();
    std::cout << "Removido: " << removido << std::endl;
    std::cout << "Primeiro agora: " << fila->getPrimeiro() << std::endl;
  }

  std::cout << "Fila vazia? " << (fila->vazia() ? "Sim" : "Não") << std::endl;

  for (int i = 200; i < 204; i++) { 
    std::cout << "Inserindo " << i << ": ";
    if (fila->InserirElemento(i))
      std::cout << "Sucesso";
    else
      std::cout << "Falha (Fila cheia)";
    std::cout << std::endl;
  }

  std::cout << "Primeiro elemento apos circularidade: " << fila->getPrimeiro() << std::endl;
  while (!fila->vazia()) {
    int removido = fila->RemoverElemento();
    std::cout << "Removido: " << removido << std::endl;
    std::cout << "Primeiro agora: " << fila->getPrimeiro() << std::endl;
  }

  std::cout << "Fila vazia? " << (fila->vazia() ? "Sim" : "Não") << std::endl;
  delete fila;
}
