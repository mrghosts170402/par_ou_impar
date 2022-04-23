while True:
    valor_jogador_1 = input ('valor jogador 1: ')
    jogador_1 = input ("par ou impar 1: ")


    if jogador_1 == "par" or jogador_1 == "impar":
        if jogador_1 == "par":
            jogador_2 = "impar"

        elif jogador_1 == "impar":
            jogador_2 = "par"

        valor_jogador_2 = input ('valor jogador 2: ')
    else:
        print ("opcao invalida")

    if ((int(valor_jogador_1) + int (valor_jogador_2)) % 2) == 0:
        if jogador_1 == "par":
            print ("jogador 1 ganhou")
        else:
            print ("jogador 2 ganhou")
        
    else:
        if jogador_1 == "impar":
            print ("jogador 1 ganhou")
        else:
            print ("jogador 2 ganhou")
