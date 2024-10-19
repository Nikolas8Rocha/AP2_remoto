def define_posicoes (linha, coluna, orientacao, tamanho):
    posicoes_ocupadas = []
    
    if orientacao == "horizontal":
        i = 0
        while i<tamanho:
            coluna_2  = coluna + i
            posicoes_ocupadas.append ([linha, coluna_2])
            i+=1
    if orientacao == "vertical":
        i = 0
        while i<tamanho:
            linha_2  = linha + i
            posicoes_ocupadas.append ([linha_2, coluna])
            i+=1
    return posicoes_ocupadas



def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    if len (frota)<1:
        frota[nome] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    else: 
        if nome not in frota:
            frota[nome] = [define_posicoes(linha, coluna, orientacao, tamanho)]
        else:
            for navio, lista_posicoes in frota.items():
                if nome == navio:
                    a = lista_posicoes
                    b = [define_posicoes(linha, coluna, orientacao, tamanho)]
                    c = a+b
                    frota [nome] = c
                    
    return frota




def faz_jogada(tabuleiro,linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    
    return tabuleiro



def posiciona_frota (lista_frota): 
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

    posicoes_totais = []
    for nome, lista_posicoes in lista_frota.items():
        for lista_de_cada_navio in lista_posicoes:
            for posicao in lista_de_cada_navio:
                posicoes_totais.append (posicao)
    for linha_coluna in posicoes_totais:
        linha = linha_coluna [0]
        coluna = linha_coluna [1]
        tabuleiro [linha] [coluna] = 1
    return tabuleiro

def afundados(dic_emba, partida):

    cont = 0
    for tipo, posi_embar in dic_emba.items():
        for posi_navio in posi_embar:
            a = True
            for coordenada in posi_navio:
                linha = coordenada [0]
                coluna = coordenada [1]
                if partida [linha][coluna] != "X":
                    a = False
            if a == True:
                cont += 1
    return cont            


