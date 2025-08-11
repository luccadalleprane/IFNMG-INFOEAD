#1118
while True:
    notasValidas = 0
    somaNotas = 0
    while notasValidas < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            notasValidas += 1
            somaNotas += nota
        else:
            print("nota invalida")
            
    media = somaNotas / 2
    print(f"media = {media:.2f}")

    # Pergunta se quer continuar
    while True:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())
        if opcao == 1:
            break
        elif opcao == 2:
            exit()  # encerra o programa