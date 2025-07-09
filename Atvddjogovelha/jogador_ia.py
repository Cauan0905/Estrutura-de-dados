# -*- coding: utf-8 -*-
from random import choice
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)
        self.oponente = Tabuleiro.JOGADOR_X if tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

    def getJogada(self) -> (int, int):
    
        jogada = self.verifica_dupla(self.tipo)
        if jogada:
            return jogada

        jogada = self.verifica_dupla(self.oponente)
        if jogada:
            return jogada

        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        cantos_opostos = {
            (0, 0): (2, 2),
            (0, 2): (2, 0),
            (2, 0): (0, 2),
            (2, 2): (0, 0)
        }
        for canto, oposto in cantos_opostos.items():
            if self.matriz[canto[0]][canto[1]] == self.oponente and self.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                return oposto

        jogada = self.criar_duplas()
        if jogada:
            return jogada

        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        livres = [pos for pos in cantos if self.matriz[pos[0]][pos[1]] == Tabuleiro.DESCONHECIDO]
        if livres:
            return choice(livres)

        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)

        return None

    def verifica_dupla(self, jogador):
        
        for i in range(3):
            
            linha = self.matriz[i]
            if linha.count(jogador) == 2 and linha.count(Tabuleiro.DESCONHECIDO) == 1:
                return (i, linha.index(Tabuleiro.DESCONHECIDO))

            coluna = [self.matriz[0][i], self.matriz[1][i], self.matriz[2][i]]
            if coluna.count(jogador) == 2 and coluna.count(Tabuleiro.DESCONHECIDO) == 1:
                return (coluna.index(Tabuleiro.DESCONHECIDO), i)

        diag1 = [self.matriz[i][i] for i in range(3)]
        if diag1.count(jogador) == 2 and diag1.count(Tabuleiro.DESCONHECIDO) == 1:
            idx = diag1.index(Tabuleiro.DESCONHECIDO)
            return (idx, idx)

        diag2 = [self.matriz[i][2 - i] for i in range(3)]
        if diag2.count(jogador) == 2 and diag2.count(Tabuleiro.DESCONHECIDO) == 1:
            idx = diag2.index(Tabuleiro.DESCONHECIDO)
            return (idx, 2 - idx)

        return None

    def criar_duplas(self):
        possibilidades = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.matriz[l][c] = self.tipo
                    dupla = self.verifica_dupla(self.tipo)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                    if dupla:
                        possibilidades.append((l, c))
        if possibilidades:
            return choice(possibilidades)
        return None