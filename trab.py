'''
TRABALHO FINAL - SUDOKU
ANTONIO ANDERSON COSTA PEREIRA - 422029
EDUARDO ALCANTARA DE ALENCAR PINTO - 428945
GUSTAVO SANTOS MARQUES DE FREITAS - 414665
'''

#Abrindo arquivo com dicas
arquivo = open('texto.txt')
dicas = arquivo.read()
dicas = dicas.split('\n')

#Matriz para sudoku
linha0 = 9*[' ']
linha1 = 9*[' ']
linha2 = 9*[' ']
linha3 = 9*[' ']
linha4 = 9*[' ']
linha5 = 9*[' ']
linha6 = 9*[' ']
linha7 = 9*[' ']
linha8 = 9*[' ']
sudoku = [linha0,linha1,linha2,linha3,linha4,linha5,linha6,linha7,linha8]

#Dicionário para letras das colunas
dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,}

#Trocar letra da coluna pelo número e insere pistas na matriz sudoku
contador = 0
while contador < len(dicas)-1:
	dicas[contador] = dicas[contador].replace(str(dicas[contador][0]), str(dic[dicas[contador][0]]))
	j = int(dicas[contador][0])
	i = int(dicas[contador][2])-1
	sudoku[i][j] = int(dicas[contador][4])
	contador = contador + 1

#Função para exibir status do sudoku
def layout():
	print('\n')
	print ("     A   B   C   D   E   F   G   H   I")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("1 || "+str(sudoku[0][0])+" | "+str(sudoku[0][1])+" | "+str(sudoku[0][2])+" || "+str(sudoku[0][3])+" | "+str(sudoku[0][4])+" | "+str(sudoku[0][5])+" || "+str(sudoku[0][6])+" | "+str(sudoku[0][7])+" | "+str(sudoku[0][8])+" ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("2 || "+str(sudoku[1][0])+" | "+str(sudoku[1][1])+" | "+str(sudoku[1][2])+" || "+str(sudoku[1][3])+" | "+str(sudoku[1][4])+" | "+str(sudoku[1][5])+" || "+str(sudoku[1][6])+" | "+str(sudoku[1][7])+" | "+str(sudoku[1][8])+" ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("3 || "+str(sudoku[2][0])+" | "+str(sudoku[2][1])+" | "+str(sudoku[2][2])+" || "+str(sudoku[2][3])+" | "+str(sudoku[2][4])+" | "+str(sudoku[2][5])+" || "+str(sudoku[2][6])+" | "+str(sudoku[2][7])+" | "+str(sudoku[2][8])+" ||")
	print("  ++===+===+===++===+===+===++===+===+===++")
	print("4 || "+str(sudoku[3][0])+" | "+str(sudoku[3][1])+" | "+str(sudoku[3][2])+" || "+str(sudoku[3][3])+" | "+str(sudoku[3][4])+" | "+str(sudoku[3][5])+" || "+str(sudoku[3][6])+" | "+str(sudoku[3][7])+" | "+str(sudoku[3][8])+" ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("5 || "+str(sudoku[4][0])+" | "+str(sudoku[4][1])+" | "+str(sudoku[4][2])+" || "+str(sudoku[4][3])+" | "+str(sudoku[4][4])+" | "+str(sudoku[4][5])+" || "+str(sudoku[4][6])+" | "+str(sudoku[4][7])+" | "+str(sudoku[4][8])+" ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("6 || "+str(sudoku[5][0])+" | "+str(sudoku[5][1])+" | "+str(sudoku[5][2])+" || "+str(sudoku[5][3])+" | "+str(sudoku[5][4])+" | "+str(sudoku[5][5])+" || "+str(sudoku[5][6])+" | "+str(sudoku[5][7])+" | "+str(sudoku[5][8])+" ||")
	print("  ++===+===+===++===+===+===++===+===+===++")
	print("7 || "+str(sudoku[6][0])+" | "+str(sudoku[6][1])+" | "+str(sudoku[6][2])+" || "+str(sudoku[6][3])+" | "+str(sudoku[6][4])+" | "+str(sudoku[6][5])+" || "+str(sudoku[6][6])+" | "+str(sudoku[6][7])+" | "+str(sudoku[6][8])+" ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("8 || "+str(sudoku[7][0])+" | "+str(sudoku[7][1])+" | "+str(sudoku[7][2])+" || "+str(sudoku[7][3])+" | "+str(sudoku[7][4])+" | "+str(sudoku[7][5])+" || "+str(sudoku[7][6])+" | "+str(sudoku[7][7])+" | "+str(sudoku[7][8])+" ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("9 || "+str(sudoku[8][0])+" | "+str(sudoku[8][1])+" | "+str(sudoku[8][2])+" || "+str(sudoku[8][3])+" | "+str(sudoku[8][4])+" | "+str(sudoku[8][5])+" || "+str(sudoku[8][6])+" | "+str(sudoku[8][7])+" | "+str(sudoku[8][8])+" ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print('\n')

vq = 1 #variável de validade dos quadrantes
def quad():#Verificador dos quadrantes
	#Quadrantes
	q1 = []
	i = 0
	for i in range(0, 3):
	    q1.append(sudoku[i][:3])
	q2 = []
	i = 0
	for i in range(0, 3):
	    q2.append(sudoku[i][3:6])
	q3 = []
	i = 0
	for i in range(0, 3):
	    q3.append(sudoku[i][6:])
	q4 = []
	i = 0
	for i in range(3, 6):
	    q4.append(sudoku[i][:3])
	q5 = []
	i = 0
	for i in range(3, 6):
	    q5.append(sudoku[i][3:6])
	q6 = []
	i = 0
	for i in range(3, 6):
	    q6.append(sudoku[i][6:])
	q7 = []
	i = 0
	for i in range(6, 9):
	    q7.append(sudoku[i][:3])
	q8 = []
	i = 0
	for i in range(6, 9):
	    q8.append(sudoku[i][3:6])
	q9 = []
	i = 0
	for i in range(6, 9):
	    q9.append(sudoku[i][6:])
	quadrante = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
	vq = 1 #variável de validade
	i = 0 #linha
	j = 0 #coluna
	k = 0 #contador
	for i in range(0, 9):
		for j in range(0, 3):
			for k in range(1, 10):
				x = int(quadrante[i][j].count(k))
				if x > 1:
					print("HA VALORES IGUAIS EM UM MESMO QUADRANTE!")
					vq = 0

layout() #mostra status do sudoku com as dicas do arquivo pela primeira vez

#Verificador de entradas do usuário
"""while contador < len(dicas)-1:
	dicas[contador] = dicas[contador].split()
	dicas[contador] = "".join(dicas[contador])
	v = dicas[contador].find(',')
	p = dicas[contador].find(':')
	if len(dicas[contador]) != 5 or v !=1 or p !=3 or int(dicas[contador][2]) == 0 or int(dicas[contador][4]) ==0:
		dicas[contador] = 0
	print(dicas[contador])
	contador = contador + 1"""

loop = 1 #variável para quebra de loop 
verdicas = 0 #variável para garantia de que dicas serão verificadas uma única vez dentro do loop
while loop != 0:
	valido = 1 #variável para verificar validade das dicas
	valido2 = 1 #variável para verificar validade das entradas
	if verdicas == 0:
		#verificação da validade das dicas
		if len(dicas)-1>80:
			valido = 0
		elif valido==1:
			for i in range(len(dicas)-1):
				for j in range(i+1,len(dicas)-1):
					if dicas[i][4] == dicas[j][4]:
						if (dicas[i][0] == dicas[j][0] and dicas[i][2] != dicas[j][2]) or (dicas[i][0] != dicas[j][0] and dicas[i][2] == dicas[j][2]):
							valido = 0
		else:
			verdicas = 1
		
		quad() #chama a função que verifica se há número iguais nos quadrantes
		if vq == 0:
			valido = 0

		if valido==0:
			print("JOGO INVALIDO! CONFIGURE AS DICAS CORRETAMENTE")
			loop = 0
	if loop!=0:
		jogada = input("DIGITE SUA JOGADA:")
		jogada = jogada.split()
		jogada = "".join(jogada)
		v = jogada.find(',')
		p = jogada.find(':')
		#verifica a formatação da jogada
		if len(jogada) != 5 or v !=1 or p !=3 or int(jogada[2]) == 0 or int(jogada[4]) == 0:
			print("FORMATO NÃO COMPREENDIDO!")
			valido2 = 0
		else:
			coluna = int(dic[jogada[0]])
			linha = int(jogada[2])-1
			numero = int(jogada[4]) #formata valores da jogada para matriz sudoku
			for j in range(0,9): #verifica se há numero igual a jogada na linha
				if numero == sudoku[linha][j]:
					print("VALOR JA EXISTENTE NA LINHA!")
					valido2 = 0
			for i in range(0,9):#verifica se há numero igual a jogada na coluna
				if numero == sudoku[i][coluna]: 
					print("VALOR JA EXISTENTE NA COLUNA!")
					valido2 = 0
			for k in range (0, len(dicas)-1):#verifica se a jogada tenta sobrescrever uma dica
				if coluna==int(dicas[k][0]) and linha==int(dicas[k][2])-1:
					print("DICAS NAO PODEM SER ALTERADAS!")
					valido2 = 0
			quad() #chama a função que verifica se há número iguais nos quadrantes
			if vq == 0:
				valido = 0

		if valido2 == 0:
			print("JOGADA INVALIDA!")
			loop = 0 #APENAS PARA FINS DE TESTE!
		elif valido2 == 1:
			sudoku[linha][coluna] = numero
			print('\n'*130)
			layout()



				
#validador de numero na posição
'''def posicao_valido(sudoku,i,j,num):
  linha_valida=all([num != sudoku[i][x]for x in range(9)])
  if linha_valida:
    coluna_valida=all([num != sudoku[x][j]for x in range(9)])
    if coluna_valida:
      linhaX, colunaY = 3*(i//3),3*(j//3)
      for x in range (linhaX,linhaX+3):
        for y in range (colunaY,colunaY+3):
          if sudoku[x][y] == num:
            return False
      return True
  return False'''

