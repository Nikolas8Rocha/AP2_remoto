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
#condição de repetição para cada tipo de navio, exemplo: são 2 navios tanques, pois isso dentro da 
#lista existem duas listas de navios tanques, assim no serão imprimidos duas vezes onde cada navio
#tanque deve ser posicionado
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
    #pede onde o jogador quer posicionar seus navios
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
    #verifica se essa posição é valida
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
    #adiciona o novo navio a frota do jogador
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

#monta tabuleiro do jogador e do oponente já com as frotas
lista_oponente = funcoes.posiciona_frota (frota_oponente)
lista_jogador = funcoes.posiciona_frota (frota)
tabuleiros = funcoes.monta_tabuleiros (lista_jogador,lista_oponente)
print (tabuleiros)

jogando = True
posicoes_informadas = []
posicoes_informadas_op = []
while jogando == True:
    #inicio da lógica de jogabilidade de ações do jogador
    posicao_atual = []
    linha_j = int(input("Jogador, qual linha deseja atacar? "))
    #verifica se a linha onde o jogador atacou é valida
    while linha_j>9 or linha_j<0:
        print ("Linha inválida!")
        linha_j = int(input("Jogador, qual linha deseja atacar? "))
    coluna_j = int(input("Jogador, qual coluna deseja atacar? "))
    #verifica se a coluna onde o jogador atacou é valida
    while coluna_j>9 or coluna_j<0:
        print ("Coluna inválida!")
        coluna_j = int(input("Jogador, qual coluna deseja atacar? "))
    #cria o par ordenado de ataque do jogador
    posicao_atual = [linha_j,coluna_j]
    #verifica se não é uma jogada inéditada
    if posicao_atual in posicoes_informadas:
        print ("A posição linha {0} e coluna {1} já foi informada anteriormente!".format(linha_j,coluna_j))
    #caso seja uma jogada inétida segue a lógica do jogo...
    else:
        #atualiza o tabuleiro com a jogada
        posicoes_informadas.append(posicao_atual)
        lista_atualizado = funcoes.faz_jogada (lista_oponente,linha_j,coluna_j)
        
        afundados = funcoes.afundados(frota_oponente,lista_atualizado)
        c = 0
        #condição para a continuação do jogo.
        for barco, posicoes in frota_oponente.items():
            for posicao in posicoes:
                c+=1
        #Se c é quantidade de barcos que o oponente tem, quando c for igual a quantidade de afundados
        #significa que o jogador ganhou o jogo! 
        if afundados == c:
            print ("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False
        #caso o jogador não tenha derrubado todos os navios do oponente, o oponente tem a chance de 
        # fazer a sua jogada. Portanto, o código possibilita a ação do jogador e depois a resposta do oponente, 
        #necessariamente nesse ordem até que um dos dois ganhe o jogo!
        if afundados != c:
            #inica jogada aleatoria do oponente
            linha_op = random.randint (0,9)
            coluna_op = random.randint (0,9)
            ataque_op = [linha_op,coluna_op]
            #verifica se a jogada é valida
            while ataque_op in posicoes_informadas_op:
                linha_op = random.randint (0,9)
                coluna_op = random.randint (0,9)
                ataque_op = [linha_op,coluna_op]
            posicoes_informadas_op.append (ataque_op)
            print ("Seu oponente está atacando na linha {0} e coluna {1}".format (linha_op, coluna_op))
            lista_atualizada_op = funcoes.faz_jogada (lista_jogador,linha_op,coluna_op)
            afundados_op = funcoes.afundados(frota, lista_atualizada_op)
            #aqui é o mesmo princípio de número restantes de navios a serem a fundados, quando c_op
            #for igual a número de barcos afundados, o oponente ganha o jogo
            c_op = 0
            for barco, posicoes in frota.items():
                for posicao in posicoes:
                    c_op+=1
            if afundados_op == c_op:
                print ("Xi! O oponente derrubou toda a sua frota =(")
                jogando = False
            #o tabuleiro atualizado é sempre mostrado depois das ações
            if afundados_op != c_op:
                print (funcoes.monta_tabuleiros (lista_jogador,lista_atualizado))