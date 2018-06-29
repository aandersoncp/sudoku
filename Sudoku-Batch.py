'''
SUDOKU INTERATIVO PARA TERMINAL PYTHON 3
CRIADO POR:
ANTONIO ANDERSON 
EDUARDO ALCANTARA
GUSTAVO MARQUES
'''

#Abrindo e configurando arquivo com dicas
arquivo = open('PistasConfig.txt')
dicas = arquivo.read()
dicas = dicas.split('\n')

#Abrindo e configurando arquivo com dicas
arquivo = open('Jogadas.txt')
jogadas = arquivo.read()
jogadas = jogadas.split('\n')

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

def testelin(numero, linha): #função para testar se há números iguais na linha
	validade = True
	contador = 0
	distintos = 0 #conta quantos numeros distintos há na linha
	while contador < 9 and validade:
		if numero == sudoku[linha][contador]:
			distintos = distintos + 1
			if distintos > 1:
				contador = 10
				validade = False			
		contador = contador + 1
	return validade


def testecol(numero, coluna): #função para testar se há números iguais na coluna
	validade = True
	contador = 0
	distintos = 0 #conta quantos numeros distintos há na linha
	while contador < 9 and validade:
		if numero == sudoku[coluna][contador]:
			distintos = distintos + 1
			if distintos > 1:
				contador = 10
				validade = False			
		contador = contador + 1
	return validade


def testequad(): #função para teste de numeros iguais em um mesmo quadrante
	#separação da matriz sudoku em quadrantes
	q1 = [sudoku[0][0], sudoku[0][1], sudoku[0][2], sudoku[1][0], sudoku[1][1], sudoku[1][2], sudoku[2][0], sudoku[2][1], sudoku[2][2]]
	q2 = [sudoku[0][3], sudoku[0][4], sudoku[0][5], sudoku[1][3], sudoku[1][4], sudoku[1][5], sudoku[2][3], sudoku[2][4], sudoku[2][5]]
	q3 = [sudoku[0][6], sudoku[0][7], sudoku[0][8], sudoku[1][6], sudoku[1][7], sudoku[1][8], sudoku[2][6], sudoku[2][7], sudoku[2][8]]
	q4 = [sudoku[3][0], sudoku[3][1], sudoku[3][2], sudoku[4][0], sudoku[4][1], sudoku[4][2], sudoku[5][0], sudoku[5][1], sudoku[5][2]]
	q5 = [sudoku[3][3], sudoku[3][4], sudoku[3][5], sudoku[4][3], sudoku[4][4], sudoku[4][5], sudoku[5][3], sudoku[5][4], sudoku[5][5]]
	q6 = [sudoku[3][6], sudoku[3][7], sudoku[3][8], sudoku[4][6], sudoku[4][7], sudoku[4][8], sudoku[5][6], sudoku[5][7], sudoku[5][8]]
	q7 = [sudoku[6][0], sudoku[6][1], sudoku[6][2], sudoku[7][0], sudoku[7][1], sudoku[7][2], sudoku[8][0], sudoku[8][1], sudoku[8][2]]
	q8 = [sudoku[6][3], sudoku[6][4], sudoku[6][5], sudoku[7][3], sudoku[7][4], sudoku[7][5], sudoku[8][3], sudoku[8][4], sudoku[8][5]]
	q9 = [sudoku[6][6], sudoku[6][7], sudoku[6][8], sudoku[7][6], sudoku[7][7], sudoku[7][8], sudoku[8][6], sudoku[8][7], sudoku[8][8]]
	quadrante = [q1, q2, q3, q4, q5, q6, q7, q8, q9] #matriz com os quadrantes da matriz sudoku
	x = 0 #contadores
	i = 0
	#variável (1 a 9) para compração de respostas
	qv = True
	while i < 9 and qv:
		k = 1
		while k < 10 and qv:
			x = int(quadrante[i].count(k))
			k = k + 1
			if x > 1:
				qv = False
				k = 11
				i = 10
		i = i + 1
	return qv

#Trocar letra da coluna pelo número e insere pistas na matriz sudoku
contador = 0
erro = False #variável para verificar se dicas foram testasdas e evitar outras ações do programa

if len(dicas) > 80: #testa se há mais de 80 dicas
	print("Configuracao de dicas invalida.") 
	erro = True

else:
	while contador < len(dicas)-1:
		dicas[contador] = dicas[contador].replace(str(dicas[contador][0]), str(dic[dicas[contador][0]]))
		j = int(dicas[contador][0]) #coluna da matriz sudoku
		i = int(dicas[contador][2])-1 #linha da matriz sudoku
		sudoku[i][j] = int(dicas[contador][4])
		if int(dicas[contador][4]) == 0: #verifica se há o valor zero entre as pistas 
			print("Configuracao de dicas invalida.") 
			contador = len(dicas)
			erro = True
		else:
			if not testelin(sudoku[i][j], i) or not testecol(sudoku[i][j], j): #insere as pistas na matriz e testa linha e coluna
				print("Configuracao de dicas invalida.") 
				contador = len(dicas)
				erro = True
		contador = contador + 1

if not erro:
	contador = 0
	for contador in range(0, len(jogadas)-1): #percorre todas as jogadas da lista de jogadas
		coluna = int(dic[jogadas[contador][0]])
		linha = int(jogadas[contador][2])-1
		numero = int(jogadas[contador][4]) #formata valores da jogada para matriz sudoku		
		contador2 = 0 #variável para percorrer a lista de pistas
		distintodica = True #variável para testar se jogada tenta sobreescrever uma pista
		while contador2 < len(dicas)-1 and distintodica:
			if coluna==int(dicas[contador2][0]) and linha==int(dicas[contador2][2])-1:
				print("A jogada ("+str(jogadas[contador][0])+","+str(jogadas[contador][2])+") = "+str(numero)+" eh invalida!")
				distintodica = False
			contador2 = contador2 + 1

		if distintodica:
			jogadaante = sudoku[linha][coluna] #salva valor anterior da matriz
			sudoku[linha][coluna] = int(jogadas[contador][4]) #insere jogada na matriz para uso das funções
			if int(jogadas[contador][4]) == 0 or not testelin(numero, linha) or not testecol(numero, coluna) or not testequad(): #teste se o valor da jogada é zero, se há mesmo valor na linha, coluna ou quadrante
				sudoku[linha][coluna] = jogadaante
				print("A jogada ("+str(jogadas[contador][0])+","+str(jogadas[contador][2])+") = "+str(numero)+" eh invalida!")
	contlinha = 0 #contadores
	contcoluna = 0
	gg = 0 #variável para testar se jogo está completo
	while contlinha<9 and sudoku[contlinha][contcoluna] != ' ': #verifica se ainda já jogadas não preenchidas
		while contcoluna<9 and sudoku[contlinha][contcoluna] != ' ':
			gg = gg + 1
			contcoluna = contcoluna + 1
		contlinha = contlinha + 1
		contcoluna = 0	
	if gg == 81:
		print("A grade foi preenchida com sucesso!")

	else:
		print("A grade nao foi preenchida!")

