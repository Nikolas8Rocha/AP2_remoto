import funcoes



i = 0

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}  

while i < 10:

    if i > 5:
        print("Insira as informações referentes ao navio submarino que possui tamanho 1")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

            
        valida = funcoes.posicao_valida(frota, linha , coluna,"vertical", 1)
        while valida == False:
            print("Esta posição não está válida!")
            print("Insira as informações referentes ao navio porta-aviões que possui tamanho 1")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            valida = funcoes.posicao_valida(frota, linha , coluna, "vertical", 1)
        frota = funcoes.preenche_frota(frota,"submarino",linha, coluna, orientacao, 1)
    
    else:
        if i == 0:
            print("Insira as informações referentes ao navio porta-aviões que possui tamanho 4")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            if orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
            
            valida = funcoes.posicao_valida(frota, linha , coluna, orientacao, 4)
            while valida == False:
                print("Esta posição não está válida!")
                print("Insira as informações referentes ao navio porta-aviões que possui tamanho 4")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                orientacao = int(input("[1] Vertical [2] Horizontal "))
                if orientacao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
                valida = funcoes.posicao_valida(frota, linha , coluna, orientacao, 4)
            frota = funcoes.preenche_frota(frota,"porta-aviões",linha, coluna, orientacao, 4)
        elif i > 0 and i <= 2:
            print("Insira as informações referentes ao navio navio-tanque que possui tamanho 3")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            if orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
            
            valida = funcoes.posicao_valida(frota, linha , coluna, orientacao, 3)
            while valida == False:
                print("Esta posição não está válida!")
                print("Insira as informações referentes ao navio porta-aviões que possui tamanho 3")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                orientacao = int(input("[1] Vertical [2] Horizontal "))
                if orientacao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
                valida = funcoes.posicao_valida(frota, linha , coluna, orientacao, 3)
            frota = funcoes.preenche_frota(frota,"navio-tanque",linha, coluna, orientacao, 3)
        elif i > 2 and i <= 5:            
            print("Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            if orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
            
            valida = funcoes.posicao_valida(frota, linha , coluna, orientacao, 2)
            while valida == False:
                print("Esta posição não está válida!")
                print("Insira as informações referentes ao navio porta-aviões que possui tamanho 2")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                orientacao = int(input("[1] Vertical [2] Horizontal "))
                if orientacao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
                valida = funcoes.posicao_valida(frota, linha , coluna, orientacao, 2)
            frota = funcoes.preenche_frota(frota,"contratorpedeiro",linha, coluna, orientacao, 2)

    i += 1


print(frota)

