import funcoes
tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
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


frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

lista_oponente = funcoes.posiciona_frota (frota_oponente)
lista_jogador = funcoes.posiciona_frota (frota)



jogando = True
posicoes_informadas = []
while jogando == True:
    posicao_atual = []
    linha_j = int(input("Jogador, qual linha deseja atacar?"))
    while linha_j>9 or linha_j<0:
        print ("Linha inválida!")
        linha_j = int(input("Jogador, qual linha deseja atacar?"))
    coluna_j = int(input("Jogador, qual coluna deseja atacar?"))
    while coluna_j>9 or coluna_j<0:
        print ("Coluna inválida!")
        coluna_j = int(input("Jogador, qual coluna deseja atacar?"))
    posicao_atual = [linha_j,coluna_j]
    if posicao_atual in posicoes_informadas:
        print ("A posição linha {0} e coluna {1} já foi informada anteriormente!".format(linha_j,coluna_j))
    else:
        posicoes_informadas.append(posicao_atual)
        lista_atualizado = funcoes.faz_jogada (lista_oponente,linha_j,coluna_j)
        tabuleiros = funcoes.monta_tabuleiros (lista_jogador,lista_atualizado)
        print (tabuleiros)
        afundados = funcoes.afundados(frota_oponente,lista_atualizado)
        c = 0
        for barco, posicoes in frota_oponente.items():
            for posicao in posicoes:
                c+=1
        if afundados == c:
            print ("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False