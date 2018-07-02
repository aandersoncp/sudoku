def interativo():
	#Abrindo e configurando arquivo com dicas
	arquivo = open('PistasConfig.txt')
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

	#cores a serem usadas no terminal
	vermelho = "\033[0;31m"
	azul = "\033[0;34m"
	ciano = "\033[1;36m"
	verde = "\033[0;32m"
	nulo = "\033[m"

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

	def scr (numero, linha, coluna): #função para selecionar cor de cada bloco do layout
		i = 0
		teste = False
		while i < len(dicas) - 1 and not teste:
			if int(dicas[i][0]) == coluna and int(dicas[i][2])-1 == linha and str(dicas[i][4]) == str(numero):
				teste = True
			i = i + 1
		if teste:
			return str(numero)
		else:
			return ciano+str(numero)+azul


	def layout(): #Procedimento para mostrar status da matriz sudoku
		print('\n')
		print("     A   B   C    D   E   F    G   H   I")
		print(azul+"  ++---+---+---++---+---+---++---+---+---++"+nulo)
		print("1 "+azul+"|| "+scr(sudoku[0][0], 0, 0)+" | "+scr(sudoku[0][1], 0, 1)+" | "+scr(sudoku[0][2], 0, 2)+" || "+scr(sudoku[0][3], 0, 3)+" | "+scr(sudoku[0][4], 0, 4)+" | "+scr(sudoku[0][5], 0, 5)+" || "+scr(sudoku[0][6], 0, 6)+" | "+scr(sudoku[0][7], 0, 7)+" | "+scr(sudoku[0][8], 0, 8)+" ||"+nulo)
		print(azul+"  ++---+---+---++---+---+---++---+---+---++"+nulo)
		print("2 "+azul+"|| "+scr(sudoku[1][0], 1, 0)+" | "+scr(sudoku[1][1], 1, 1)+" | "+scr(sudoku[1][2], 1, 2)+" || "+scr(sudoku[1][3], 1, 3)+" | "+scr(sudoku[1][4], 1, 4)+" | "+scr(sudoku[1][5], 1, 5)+" || "+scr(sudoku[1][6], 1, 6)+" | "+scr(sudoku[1][7], 1, 7)+" | "+scr(sudoku[1][8], 1, 8)+" ||"+nulo)
		print(azul+"  ++---+---+---++---+---+---++---+---+---++"+nulo)
		print("3 "+azul+"|| "+scr(sudoku[2][0], 2, 0)+" | "+scr(sudoku[2][1], 2, 1)+" | "+scr(sudoku[2][2], 2, 2)+" || "+scr(sudoku[2][3], 2, 3)+" | "+scr(sudoku[2][4], 2, 4)+" | "+scr(sudoku[2][5], 2, 5)+" || "+scr(sudoku[2][6], 2, 6)+" | "+scr(sudoku[2][7], 2, 7)+" | "+scr(sudoku[2][8], 2, 8)+" ||"+nulo)
		print(azul+"  ++===+===+===++===+===+===++===+===+===++"+nulo)
		print("4 "+azul+"|| "+scr(sudoku[3][0], 3, 0)+" | "+scr(sudoku[3][1], 3, 1)+" | "+scr(sudoku[3][2], 3, 2)+" || "+scr(sudoku[3][3], 3, 3)+" | "+scr(sudoku[3][4], 3, 4)+" | "+scr(sudoku[3][5], 3, 5)+" || "+scr(sudoku[3][6], 3, 6)+" | "+scr(sudoku[3][7], 3, 7)+" | "+scr(sudoku[3][8], 3, 8)+" ||"+nulo)
		print(azul+"  ++---+---+---++---+---+---++---+---+---++"+nulo)
		print("5 "+azul+"|| "+scr(sudoku[4][0], 4, 0)+" | "+scr(sudoku[4][1], 4, 1)+" | "+scr(sudoku[4][2], 4, 2)+" || "+scr(sudoku[4][3], 4, 3)+" | "+scr(sudoku[4][4], 4, 4)+" | "+scr(sudoku[4][5], 4, 5)+" || "+scr(sudoku[4][6], 4, 6)+" | "+scr(sudoku[4][7], 4, 7)+" | "+scr(sudoku[4][8], 4, 8)+" ||"+nulo)
		print(azul+"  ++---+---+---++---+---+---++---+---+---++"+nulo)
		print("6 "+azul+"|| "+scr(sudoku[5][0], 5, 0)+" | "+scr(sudoku[5][1], 5, 1)+" | "+scr(sudoku[5][2], 5, 2)+" || "+scr(sudoku[5][3], 5, 3)+" | "+scr(sudoku[5][4], 5, 4)+" | "+scr(sudoku[5][5], 5, 5)+" || "+scr(sudoku[5][6], 5, 6)+" | "+scr(sudoku[5][7], 5, 7)+" | "+scr(sudoku[5][8], 5, 8)+" ||"+nulo)
		print(azul+"  ++===+===+===++===+===+===++===+===+===++"+nulo)
		print("7 "+azul+"|| "+scr(sudoku[6][0], 6, 0)+" | "+scr(sudoku[6][1], 6, 1)+" | "+scr(sudoku[6][2], 6, 2)+" || "+scr(sudoku[6][3], 6, 3)+" | "+scr(sudoku[6][4], 6, 4)+" | "+scr(sudoku[6][5], 6, 5)+" || "+scr(sudoku[6][6], 6, 6)+" | "+scr(sudoku[6][7], 6, 7)+" | "+scr(sudoku[6][8], 6, 8)+" ||"+nulo)
		print(azul+"  ++---+---+---++---+---+---++---+---+---++"+nulo)
		print("8 "+azul+"|| "+scr(sudoku[7][0], 7, 0)+" | "+scr(sudoku[7][1], 7, 1)+" | "+scr(sudoku[7][2], 7, 2)+" || "+scr(sudoku[7][3], 7, 3)+" | "+scr(sudoku[7][4], 7, 4)+" | "+scr(sudoku[7][5], 7, 5)+" || "+scr(sudoku[7][6], 7, 6)+" | "+scr(sudoku[7][7], 7, 7)+" | "+scr(sudoku[7][8], 7, 8)+" ||"+nulo)
		print(azul+"  ++---+---+---++---+---+---++---+---+---++"+nulo)
		print("9 "+azul+"|| "+scr(sudoku[8][0], 8, 0)+" | "+scr(sudoku[8][1], 8, 1)+" | "+scr(sudoku[8][2], 8, 2)+" || "+scr(sudoku[8][3], 8, 3)+" | "+scr(sudoku[8][4], 8, 4)+" | "+scr(sudoku[8][5], 8, 5)+" || "+scr(sudoku[8][6], 8, 6)+" | "+scr(sudoku[8][7], 8, 7)+" | "+scr(sudoku[8][8], 8, 8)+" ||"+nulo)
		print(azul+"  ++---+---+---++---+---+---++---+---+---++"+nulo)
		print('\n')

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
					print("HA VALORES IGUAIS EM UM MESMO QUADRANTE!")
					qv = False
					k = 11
					i = 10
			i = i + 1
		return qv


	def info():
		print("FORMATO DE JOGADA: '<COL>,<LIN>: <NUMERO>'")
		print("COMANDO PARA DELETAR UMA JOGADA: 'D<COL>,<LIN>'")
		print("ENTRE 'X' PARA ENCERRAR O JOGO.")

				
	caracts = ["A","B","C","D","E","F","G","H","I","a","b","c","d","e","f","g","h","i"] #lista com caracteres aceitáveis



	layout() #mostra status do sudoku com as dicas do arquivo pela primeira vez
	print("---------SUDOKU - MODO INTERATIVO----------")
	print("      (ENTRE 'INFO' PARA INSTRUCOES)\n")


	loop = 1 #variável para quebra de loop 
	verdicas = 0 #variável para garantia de que dicas serão verificadas uma única vez dentro do loop
	while loop != 0:
		valido = 1 #variável para verificar validade das dicas
		valido2 = 1 #variável para verificar validade das entradas
		i = 0 #contadores
		j = 0
		gg = 0 #numero de jogadas preenchidas
		delecao = 0 
		comand = 0 #variáveis utilizadas para verificar ação de deleção e de info/sair, e evitar que outras ações sejam tomadas
		if verdicas == 0:
			#verificação da validade das dicas
			if len(dicas)-1>80 or not testequad():
				valido = 0
			elif valido==1:
				for i in range(len(dicas)-1):
					if int(dicas[i][4]) == 0: #verifica se o valor 0 está sendo usado na pista
						valido = 0
					else:
						for j in range(i+1,len(dicas)-1):
							if dicas[i][4] == dicas[j][4]:
								if (dicas[i][0] == dicas[j][0] and dicas[i][2] != dicas[j][2]) or (dicas[i][0] != dicas[j][0] and dicas[i][2] == dicas[j][2]): #verifica (com "ou exclusivo", para ignorar pistas repetidas) validade das pistas nas linhas e colunas
									valido = 0
									print("AS PISTAS NAO SEGUEM AS REGRAS DO JOGO!")
			else:
				verdicas = 1
			
			if valido==0:
				print("JOGO INVALIDO! CONFIGURE AS PISTAS CORRETAMENTE! \n(SUG: USE O COMANDO 'nano PistasConfig.txt')")
				loop = 0
		

		if valido == 1:
			i = 0 #contadores
			j = 0
			gg = 0 #numero de jogadas preenchidas
			while i<9 and sudoku[i][j] != ' ': #verifica se ainda já jogadas não preenchidas
				while j<9 and sudoku[i][j] != ' ':
					gg = gg + 1
					j = j + 1
				i = i + 1
				j = 0	
			if gg > 80:
				print(verde+"PARABENS, VOCE COMPLETOU O SUDOKU!"+nulo)
				loop = 0

		if loop!=0:
			jogada = input("DIGITE SUA JOGADA:")
			jogada = jogada.split() #verifica a formatação da jogada:
			jogada = "".join(jogada)
			v = jogada.find(',')
			p = jogada.find(':')
			vc = False #valicação do caractere da jogada
			contador = 0
			if not jogada:
				vc = True
				valido2 = 0
			while not vc and contador < 18: #testa se coluna tem caractere permitido
				if jogada[0] == caracts[contador]:
					vc = True
				contador = contador + 1
			if jogada == 'X': #testa se é entrada de comando para encerrar o jogo
				print(verde+"JOGO ENCERRADO!"+nulo)
				loop = 0
				comand = 1
			elif jogada == 'INFO': #teste se é entrada de comando de informação
				info ()
				comand = 1
			
			elif len(jogada)==4 and (jogada[0]=="D" or jogada[0]=="d"): #testa se é uma jogada de deleção
				vc = False #valicação da letra da jogada (coluna)
				vl = False #valicação do numero da jogada (linha)
				contador = 0
				while not vc and contador < 18: #testa se coluna tem caractere permitido
					if jogada[1] == caracts[contador]:
						vc = True
					contador = contador + 1
				contador = 1
				while contador < 10 and not vl: #testa de linha tem caractere de numero permitido
					if str(jogada[3]) == str(contador):
						vl = True
					contador = contador + 1
				if not vc or not vl or jogada[2] != ',': #testa se é uma jogada de deleção no formato correto
					print(vermelho+"FORMATO DE JOGADA NAO COMPREENDIDO!"+nulo)
					valido2 = 0
				else:
					vd = False #variável para verificação de dica
					contador = 0
					while not vd and contador < len(dicas) - 1: #testa se jogada tenta deletar uma dica
						if str(dic[jogada[1]]) == str(dicas[contador][0]) and str(jogada[3]) == str(dicas[contador][2]):
							vd = True
						contador = contador + 1
					if vd:
						print(vermelho+"PISTAS NAO PODEM SER DELETADAS!"+nulo)
						valido2 = 0
					else: #deletando a jogada
						l = int(jogada[3]) - 1
						c = int(dic[jogada[1]])
						if str(sudoku[l][c]) == ' ':
							print('\n'*130)
							layout()
							print(vermelho+"NAO HA VALOR A SER DELETADO!"+nulo)
							delecao = 1 #variável para impedir outras ações do programa sejam acionadas
						else:
							sudoku[l][c] = ' '
							print('\n'*130)
							layout()
							print(verde+"JOGADA DELETADA!"+nulo)
							delecao = 1 #variável para impedir outras ações do programa sejam acionadas

			elif (len(jogada) != 5 or v !=1 or p !=3 or int(jogada[2]) == 0 or int(jogada[4]) == 0 or not vc): #testa outra possibilidade de invalidação de entrada
				print("FORMATO DA JOGADA NAO COMPREENDIDO!")
				valido2 = 0

			else:
				coluna = int(dic[jogada[0]])
				linha = int(jogada[2])-1
				numero = int(jogada[4]) #formata valores da jogada para matriz sudoku
				for j in range(0,9): #verifica se há numero igual a jogada na linha
					if numero == sudoku[linha][j]:
						print(vermelho+"VALOR JA EXISTENTE NA LINHA!"+nulo)
						valido2 = 0
				for i in range(0,9):#verifica se há numero igual a jogada na coluna
					if numero == sudoku[i][coluna]: 
						print(vermelho+"VALOR JA EXISTENTE NA COLUNA!"+nulo)
						valido2 = 0
				for k in range (0, len(dicas)-1):#verifica se a jogada tenta sobrescrever uma dica
					if coluna==int(dicas[k][0]) and linha==int(dicas[k][2])-1:
						print(vermelho+"PISTAS NAO PODEM SER ALTERADAS!"+nulo)
						valido2 = 0
				
				if not testequad():
					valido2 = 0
		
			if valido2 == 0:
				print(vermelho+"JOGADA INVALIDA!"+nulo)
			elif valido2 == 1 and delecao == 0 and comand == 0: #salva valor anterior da matriz e sobreescreve a jogada para teste de quadrante
				numeroant = sudoku[linha][coluna]
				sudoku[linha][coluna] = numero
				print('\n'*130)
				layout()
			if not testequad() and delecao == 0 and comand == 0: #testa se há valore iguais no mesmo quadrante
				sudoku[linha][coluna] = numeroant
				print('\n'*130)
				layout()
				print(+vermelho+"HA VALORES IGUAIS EM UM MESMO QUADRANTE!"+nulo)
				print(vermelho+"JOGADA INVALIDA!"+nulo)



def batch():
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


print ("BEM-VINDO AO SUDOKU PYTHON 3")
comandoi = input("entre 'i' para MODO INTERATIVO entre 'b' para MODO BATCH:")

if comandoi == 'i':
	interativo()

elif comandoi == 'b':
	batch()

else:
	print("ENTRADA INVALIDA!")

