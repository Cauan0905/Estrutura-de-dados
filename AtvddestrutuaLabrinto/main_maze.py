# -*- coding: utf-8 -*-
import time
from maze import Maze

def solve_maze_stack(maze: Maze):
    """Resolve o labirinto usando backtracking com pilha"""
    # Pilha para armazenar as posições a visitar
    stack = []

    # Pega posição inicial do jogador
    start = maze.get_init_pos_player()
    stack.append(start)

    # Lista para registrar posições visitadas
    visited = set()

    # Enquanto houver posições para explorar
    while stack:
        # Retira a posição do topo da pilha
        current = stack.pop()

        # Ignora se já foi visitada
        if current in visited:
            continue
        visited.add(current)

        # Move o jogador para essa posição
        maze.mov_player(current)
        time.sleep(0.02)  # atraso para visualizar movimento

        # Se encontrou o prêmio
        if maze.find_prize(current):
            print("Prêmio encontrado!")
            return True

        # Gerar vizinhos (cima, baixo, esquerda, direita)
        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for nx, ny in neighbors:
            # Verifica se a posição é livre e não visitada
            if maze.is_free((nx, ny)) and (nx, ny) not in visited:
                stack.append((nx, ny))

    print("Não há caminho até o prêmio.")
    return False


if __name__ == "__main__":
    maze_csv_path = "labirinto1.txt"
    maze = Maze()
    maze.load_from_csv(maze_csv_path)

    # Exibe o labirinto em uma thread separada
    maze.run()

    # Define posição inicial e prêmio
    maze.init_player()

    # Resolve o labirinto com pilha
    solve_maze_stack(maze)
