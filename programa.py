import funcoes

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}  

navios = [
    ['porta-aviões',4],
    ['navio-tanque',3],
    ['navio-tanque',3],
    ['contratorpedeiro',2],
    ['contratorpedeiro',2],
    ['contratorpedeiro',2],
    ['submarino',1],
    ['submarino',1],
    ['submarino',1],
    ['submarino',1],
]
for barco in navios:
    navio = barco[0]
    tamanho = barco[1]
    print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    if tamanho == 1:
        orientacao = 'vertical'
    else:
        orientacao = int(input("[1] Vertical [2] Horizontal "))
        if orientacao == 1:
            orientacao = "vertical"
        else:
            orientacao = "horizontal"

    valida = funcoes.posicao_valida(frota, linha , coluna, orientacao, tamanho)
    while valida == False:
        print("Esta posição não está válida!")
        print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if tamanho == 1:
            orientacao = 'vertical'
        else:
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            if orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
        valida = funcoes.posicao_valida(frota, linha , coluna, orientacao, tamanho)
    frota = funcoes.preenche_frota(frota,navio,linha, coluna, orientacao, tamanho)

print(frota)