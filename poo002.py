import random
import time

print("JOGO DA MEMÓRIA SIMPLES")

# 1️⃣ Criando os pares
cartas = ['A', 'A', 'B', 'B']

# 2️⃣ Embaralhando
random.shuffle(cartas)

# 3️⃣ Transformando em tabuleiro 2x2
tabuleiro = [cartas[0:2], cartas[2:4]]

# 4️⃣ Controlando o que já foi revelado
revelado = [[False, False], [False, False]]

jogadas = 0


# Função para mostrar o tabuleiro
def mostrar():
    for i in range(2):
        for j in range(2):
            if revelado[i][j]:
                print(f"[{tabuleiro[i][j]}]", end=" ")
            else:
                print("[ ]", end=" ")
        print()


# Loop principal do jogo
while True:

    mostrar()

    print("\nEscolha a primeira carta")
    l1 = int(input("Linha (0 ou 1): "))
    c1 = int(input("Coluna (0 ou 1): "))

    print("Escolha a segunda carta")
    l2 = int(input("Linha (0 ou 1): "))
    c2 = int(input("Coluna (0 ou 1): "))

    # Revela as cartas
    revelado[l1][c1] = True
    revelado[l2][c2] = True

    mostrar()
    jogadas += 1

    # Verifica se é par
    if tabuleiro[l1][c1] == tabuleiro[l2][c2]:
        print("Você acertou o par!\n")
    else:
        print("Errou! As cartas serão escondidas.")
        time.sleep(2)
        revelado[l1][c1] = False
        revelado[l2][c2] = False

    # Verifica se terminou
    if revelado == [[True, True], [True, True]]:
        print(f"\nParabéns! Você venceu em {jogadas} jogadas.")
        break


#teste