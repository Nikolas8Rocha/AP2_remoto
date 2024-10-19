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
    for navios in frota.keys():
        if navios not in frota:
            frota[navios] = define_posicoes(linha, coluna, orientacao, tamanho)
        else:
            a = frota [nome]
            b = [define_posicoes(linha, coluna, orientacao, tamanho)]
            frota[nome] = [a,b]
            #frota[navios] += define_posicoes(linha, coluna, orientacao, tamanho)
        
    
    return frota



frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)

