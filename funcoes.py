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
        frota[nome] = define_posicoes(linha, coluna, orientacao, tamanho)
    else: 
        if nome not in frota:
            frota[nome] = define_posicoes(linha, coluna, orientacao, tamanho)
        else:
            for navio, lista_posicoes in frota.items():
                if nome == navio:
                    a = lista_posicoes
                    b = [define_posicoes(linha, coluna, orientacao, tamanho)]
                    c = a+b
                    frota [nome] = c
                    
    return frota


