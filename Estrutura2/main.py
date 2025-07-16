import time
import sys

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            conteudo = f.read().replace('\n', ' ')
            return list(map(int, conteudo.split()))
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        sys.exit(1)
    except ValueError:
        print("Erro ao converter os dados para inteiros. Verifique o formato do arquivo.")
        sys.exit(1)

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        chave = a[i]
        j = i - 1
        while j >= 0 and chave < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = chave
    return a

def main():
    if len(sys.argv) != 2:
        print("Uso: python ordenacao.py <arquivo_entrada.txt>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    dados = ler_arquivo(nome_arquivo)

    print(f"\nDados lidos: {dados}\n")

    # Selection Sort
    inicio_sel = time.time()
    resultado_sel = selection_sort(dados)
    fim_sel = time.time()
    tempo_sel = fim_sel - inicio_sel

    # Insertion Sort
    inicio_ins = time.time()
    resultado_ins = insertion_sort(dados)
    fim_ins = time.time()
    tempo_ins = fim_ins - inicio_ins

    # Resultados
    print("=== Resultados ===")
    print(f"Ordenado (Selection Sort): {resultado_sel}")
    print(f"Tempo Selection Sort: {tempo_sel:.6f} segundos")

    print(f"\nOrdenado (Insertion Sort): {resultado_ins}")
    print(f"Tempo Insertion Sort: {tempo_ins:.6f} segundos")

    print("\n=== Comparação ===")
    if tempo_sel < tempo_ins:
        print("Selection Sort foi mais rápido.")
    elif tempo_sel > tempo_ins:
        print("Insertion Sort foi mais rápido.")
    else:
        print("Ambos os algoritmos tiveram tempos iguais.")

if __name__ == "__main__":
    main()
