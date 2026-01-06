from random import randint
import time


numero_aleatorio = randint(1, 10)

tentativas = 0

inicio = time.perf_counter()



while True:

    palpite = int(input("Digite um número entre 1 e 10: "))

    if palpite < 1 or palpite > 10:
        print("Número inválido! Tente novamente.")
        continue

    if palpite < numero_aleatorio:
        print("Tente um número maior.")
        tentativas += 1

    elif palpite > numero_aleatorio:
        print("Tente um número menor.")
        tentativas += 1

    else:
        print("Parabéns! Você acertou!")
        break


fim = time.perf_counter()


print(f"Você tentou {tentativas} vezes até acertar o número.")
print(f"Tempo total: {fim - inicio:.2f} segundos.")