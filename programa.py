import funcoes
import random
random.seed (2)
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
        orientacao = int(input("Orientação: [1] Vertical [2] Horizontal "))
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
            orientacao = int(input("Orientação: [1] Vertical [2] Horizontal "))
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
tabuleiros = funcoes.monta_tabuleiros (lista_jogador,lista_oponente)
print (tabuleiros)

jogando = True
posicoes_informadas = []
posicoes_informadas_op = []
while jogando == True:
    posicao_atual = []
    linha_j = int(input("Jogador, qual linha deseja atacar? "))
    while linha_j>9 or linha_j<0:
        print ("Linha inválida!")
        linha_j = int(input("Jogador, qual linha deseja atacar? "))
    coluna_j = int(input("Jogador, qual coluna deseja atacar? "))
    while coluna_j>9 or coluna_j<0:
        print ("Coluna inválida!")
        coluna_j = int(input("Jogador, qual coluna deseja atacar? "))
    posicao_atual = [linha_j,coluna_j]
    if posicao_atual in posicoes_informadas:
        print ("A posição linha {0} e coluna {1} já foi informada anteriormente!".format(linha_j,coluna_j))
    else:
        posicoes_informadas.append(posicao_atual)
        lista_atualizado = funcoes.faz_jogada (lista_oponente,linha_j,coluna_j)
        
        afundados = funcoes.afundados(frota_oponente,lista_atualizado)
        c = 0
        for barco, posicoes in frota_oponente.items():
            for posicao in posicoes:
                c+=1
        if afundados == c:
            print ("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False
        if afundados != c:
            linha_op = random.randint (0,9)
            coluna_op = random.randint (0,9)
            ataque_op = [linha_op,coluna_op]
            while ataque_op in posicoes_informadas_op:
                linha_op = random.randint (0,9)
                coluna_op = random.randint (0,9)
                ataque_op = [linha_op,coluna_op]
            posicoes_informadas_op.append (ataque_op)
            print ("Seu oponente está atacando na linha {0} e coluna {1}".format (linha_op, coluna_op))
            lista_atualizada_op = funcoes.faz_jogada (lista_jogador,linha_op,coluna_op)
            afundados_op = funcoes.afundados(frota, lista_atualizada_op)
            c_op = 0
            for barco, posicoes in frota.items():
                for posicao in posicoes:
                    c_op+=1
            if afundados_op == c_op:
                print ("Xi! O oponente derrubou toda a sua frota =(")
                jogando = False
            if afundados_op != c_op:
                print (funcoes.monta_tabuleiros (lista_jogador,lista_atualizado))