#include <iostream>
#ifndef FILASEQUENCIAL_H
#define FILASEQUENCIAL_H

class FilaSequencial {
public:
  FilaSequencial();
  virtual ~FilaSequencial();
  bool vazia(), cheia();
  int getTamanho(), getPrimeiro();
  bool InserirElemento(int conteudo);
  int RemoverElemento();

private:
  int tamanhoAtual, tamanhoMaximo, inicio, fim;
  int *dados;
};
#endif