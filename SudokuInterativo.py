'''
SUDOKU INTERATIVO PARA TERMINAL PYTHON 3
CRIADO POR:
ANTONIO ANDERSON 
EDUARDO ALCANTARA
GUSTAVO MARQUES
'''

try:
	arquivo = open('PistasConfig.txt') #Abrindo e configurando arquivo com pistas
	pistas = arquivo.read()
	pistas = pistas.split('\n') #cria uma lista com todas as pistas contidas no arquivo
	sudoku = [9*[' '],9*[' '],9*[' '],9*[' '],9*[' '],9*[' '],9*[' '],9*[' '],9*[' ']] #Matriz vazia 9x9 para manipular valores do sudoku

	#cores a serem usadas no terminal:
	vermelho = "\033[0;31m"
	azul = "\033[0;34m"
	ciano = "\033[1;36m"
	verde = "\033[0;32m"
	nulo = "\033[m"

	#Dicionário para letras das colunas
	dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8}

	#Trocando letra da coluna pelo número e inserindo pistas na matriz sudoku
	for contador in range(len(pistas)-1):
		pistas[contador] = pistas[contador].upper() #formata digitação das pistas para maiúsculo
		pistas[contador] = pistas[contador].replace(str(pistas[contador][0]), str(dic[pistas[contador][0]]))
		j = int(pistas[contador][0])
		i = int(pistas[contador][2])-1
		sudoku[i][j] = str(pistas[contador][4])

	def scr (numero, linha, coluna): #função para selecionar cor de cada bloco do layout
		i = 0
		teste = False
		while i < len(pistas) - 1 and not teste:
			if int(pistas[i][0]) == coluna and int(pistas[i][2])-1 == linha and str(pistas[i][4]) == str(numero):
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
		qv = True #variável para validação
		while i < 9 and qv:
			k = 1 #variável (1 a 9) para compração de respostas
			while k < 10 and qv:
				x = int(quadrante[i].count(str(k)))
				k = k + 1
				if x > 1:
					qv = False
					k = 11
					i = 10
			i = i + 1
		return qv


	caracts = ["A","B","C","D","E","F","G","H","I","a","b","c","d","e","f","g","h","i"] #lista com caracteres aceitáveis


	layout() #mostra status do sudoku com as pistas do arquivo pela primeira vez

	print("---------SUDOKU - MODO INTERATIVO----------")
	print("      (ENTRE 'INFO' PARA INSTRUCOES)\n")

	verpistas = False #variável para garantia de que pistas serão verificadas uma única vez dentro do loop
	while True:
		validoj = True #variável para verificar validade das jogadas
		i = 0 #contadores
		j = 0
		gg = 0 #numero de jogadas preenchidas
		delecao = False
		comand = False #variáveis utilizadas para verificar ação de deleção e de info/sair, e evitar que outras ações sejam tomadas
		if not verpistas:
			#verificação da validade das pistas
			print(azul+"verificando validade das pistas..."+nulo)
			try:
				if len(pistas)-1>80:
					print(vermelho+"A QUANTIDADE DE PISTAS EXCEDE O LIMITE!"+nulo)
					print("configure as pistas corretamente com 'nano PistasConfig.txt'")
					break
				if not testequad():
					print(vermelho+"HA PISTAS REPETIDAS EM UM MESMO QUADRANTE!"+nulo)
					print("configure as pistas corretamente com 'nano PistasConfig.txt'")
					break

				for i in range(len(pistas)-1):
					if int(pistas[i][4]) == 0: #verifica se o valor 0 está sendo usado na pista
						print(vermelo+"O VALOR '0' NAO EH ACEITAVEL!"+nulo)
						print("configure as pistas corretamente com 'nano PistasConfig.txt'")
						break

					for j in range(i+1,len(pistas)-1):
						if pistas[i][4] == pistas[j][4]:
							if (pistas[i][0] == pistas[j][0] and pistas[i][2] != pistas[j][2]) or (pistas[i][0] != pistas[j][0] and pistas[i][2] == pistas[j][2]): #verifica (com "ou exclusivo", para ignorar pistas repetidas) validade das pistas nas linhas e colunas
								print("AS PISTAS NAO SEGUEM AS REGRAS DO JOGO!")
								print("configure as pistas corretamente com 'nano PistasConfig.txt'")
								break
			except:
				print("configure as pistas corretamente com 'nano PistasConfig.txt'")
				break

			verpistas = True #impede que pistas sejam verificadas novamente
			print(verde+"PISTAS VALIDAS!"+nulo)

		for i in range(9): #verificando se ainda há jogadas vazias na matriz
			if ' ' in sudoku[i]:
				gg = gg + 1

		if gg == 0: #caso de jogo completo
			print(verde+"PARABENS, VOCE COMPLETOU O SUDOKU!"+nulo)
			break

		#recebendo e formatando jogada:
		jogada = input("DIGITE SUA JOGADA:")
		jogada = jogada.split()
		jogada = "".join(jogada)
		jogada = jogada.upper()
		v = jogada.find(',') #localiza vírgula e dois pontos do formato de jogada
		p = jogada.find(':')
		vc = False #valicação do caracteres da jogada
		contador = 0
				
		if jogada == 'SAIR': #testa se é entrada de comando para encerrar o jogo
			print(verde+"JOGO ENCERRADO!"+nulo)
			break

		if jogada == 'INFO': #teste se é entrada de comando de informação
			print(azul+"FORMATO DE JOGADA: '<COL>,<LIN>: <NUMERO>'")
			print("COMANDO PARA DELETAR UMA JOGADA: 'D<COL>,<LIN>'")
			print("ENTRE 'SAIR' PARA ENCERRAR O JOGO."+nulo)
			comand = True

		if not jogada: #caso em que a entrada da jogada é falsa (vazia)
			vc = True
			validoj = False

		if jogada[0] in dic: #testa se coluna tem caractere permitido
			vc = True
			
		if len(jogada)==4 and jogada[0]=="D": #testa se é uma jogada de deleção
			vco = False #valicação da letra da jogada (coluna)
			vl = False #valicação do numero da jogada (linha)
			if jogada[1] in dic: #testa se coluna tem caractere permitido
				vco = True
			
			try: #evita erro caso valor da linha não seja numerico
				if int(jogada[3]) > 0 and int(jogada[3]) < 10: #verifica se linha tem caractere permite
					vl = True
			except:
				vl = False

			if not vco or not vl or jogada[2] != ',': #caso em que jogada de deleção é inválida
				print(vermelho+"FORMATO DE JOGADA NAO COMPREENDIDO! TENTE NOVAMENTE."+nulo)
				validoj = False

			else:
				vd = False #variável para verificação de pista
				contador = 0
				while not vd and contador < len(pistas) - 1: #testa se jogada tenta deletar uma dica
					if str(dic[jogada[1]]) == str(pistas[contador][0]) and str(jogada[3]) == str(pistas[contador][2]):
						vd = True
					contador = contador + 1

				if vd: #caso em que deleção coincide com pista
					print(vermelho+"PISTAS NAO PODEM SER DELETADAS!"+nulo)
					validoj = False

				else: #deletando a jogada
					l = int(jogada[3]) - 1
					c = int(dic[jogada[1]])

					if str(sudoku[l][c]) == ' ': #caso em que se tenta deletar espaço em branco
						print('\n'*130)
						layout()
						print(vermelho+"NAO HA VALOR A SER DELETADO!"+nulo)
						delecao = 1 #variável para impedir outras ações do programa sejam acionadas

					else:
						sudoku[l][c] = ' '
						print('\n'*130)
						layout()
						print(verde+"JOGADA DELETADA!"+nulo)
						delecao = True #variável para impedir outras ações do programa sejam acionadas
				
		if not delecao and not comand and (len(jogada) != 5 or v !=1 or p !=3 or str(jogada[2]) == '0' or str(jogada[4]) == '0' or not vc): #testa outra possibilidade de invalidação de entrada
			print(vermelho+"FORMATO DA JOGADA NAO COMPREENDIDO!"+nulo)
			validoj = False

		else: #caso de jogada normal
			try: #tenta manipular valores da jogada assumindo que podem ser convertidos em inteiro
				coluna = int(dic[jogada[0]])
				linha = int(jogada[2])-1
				numero = int(jogada[4]) #formata valores da jogada para matriz sudoku

				if str(numero) in sudoku[linha]: #verifica se há numero igual a jogada na linha
					print(vermelho+"VALOR JA EXISTENTE NA LINHA!"+nulo)
					validoj = False
				
				i = 0 #contador
				while validoj and i < 9:#verifica se há numero igual a jogada na coluna
					if str(numero) == sudoku[i][coluna]: 
						print(vermelho+"VALOR JA EXISTENTE NA COLUNA!"+nulo)
						validoj = False
					i = i + 1

				for k in range (0, len(pistas)-1):#verifica se a jogada tenta sobrescrever uma dica
					if coluna==int(pistas[k][0]) and linha==int(pistas[k][2])-1:
						print(vermelho+"PISTAS NAO PODEM SER ALTERADAS!"+nulo)
						validoj = False
				
			except: #caso em que valores não podem ser convertidos em inteiro
				validoj = False
		
			if not validoj and not delecao and not comand: #caso em que a jogada não segue formatação
				print(vermelho+"JOGADA INVALIDA!"+nulo)

			#salvando valor anterior da matriz e sobreescreve a jogada para teste de quadrante
			elif not delecao and not comand: 
				numeroant = sudoku[linha][coluna]
				sudoku[linha][coluna] = str(numero)
				print('\n'*130)
				layout()

			if not testequad() and not delecao and not comand: #caso de valor repetido no quadrante
				sudoku[linha][coluna] = numeroant
				print('\n'*130)
				layout()
				print(vermelho+"HA VALORES IGUAIS EM UM MESMO QUADRANTE!"+nulo)
				print(vermelho+"JOGADA INVALIDA!"+nulo)

except:
	print("ERRO INESPERADO!")

