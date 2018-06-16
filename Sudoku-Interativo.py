'''
TRABALHO FINAL - SUDOKU
ANTONIO ANDERSON COSTA PEREIRA - 422029
EDUARDO ALCANTARA DE ALENCAR PINTO - 428945
GUSTAVO SANTOS MARQUES DE FREITAS - 414665
'''

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
	print("     A   B   C    D   E   F    G   H   I")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("1 || \033[0;31m"+str(sudoku[0][0])+" | "+str(sudoku[0][1])+" | "+str(sudoku[0][2])+"\033[m ||\033[0;34m "+str(sudoku[0][3])+" | "+str(sudoku[0][4])+" | "+str(sudoku[0][5])+"\033[m ||\033[0;31m "+str(sudoku[0][6])+" | "+str(sudoku[0][7])+" | "+str(sudoku[0][8])+"\033[m ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("2 || \033[0;31m"+str(sudoku[1][0])+" | "+str(sudoku[1][1])+" | "+str(sudoku[1][2])+"\033[m ||\033[0;34m "+str(sudoku[1][3])+" | "+str(sudoku[1][4])+" | "+str(sudoku[1][5])+"\033[m ||\033[0;31m "+str(sudoku[1][6])+" | "+str(sudoku[1][7])+" | "+str(sudoku[1][8])+"\033[m ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("3 || \033[0;31m"+str(sudoku[2][0])+" | "+str(sudoku[2][1])+" | "+str(sudoku[2][2])+"\033[m ||\033[0;34m "+str(sudoku[2][3])+" | "+str(sudoku[2][4])+" | "+str(sudoku[2][5])+"\033[m ||\033[0;31m "+str(sudoku[2][6])+" | "+str(sudoku[2][7])+" | "+str(sudoku[2][8])+"\033[m ||")
	print("  ++===+===+===++===+===+===++===+===+===++")
	print("4 ||\033[0;34m "+str(sudoku[3][0])+" | "+str(sudoku[3][1])+" | "+str(sudoku[3][2])+"\033[m ||\033[0;31m "+str(sudoku[3][3])+" | "+str(sudoku[3][4])+" | "+str(sudoku[3][5])+"\033[m ||\033[0;34m "+str(sudoku[3][6])+" | "+str(sudoku[3][7])+" | "+str(sudoku[3][8])+"\033[m ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("5 ||\033[0;34m "+str(sudoku[4][0])+" | "+str(sudoku[4][1])+" | "+str(sudoku[4][2])+"\033[m ||\033[0;31m "+str(sudoku[4][3])+" | "+str(sudoku[4][4])+" | "+str(sudoku[4][5])+"\033[m ||\033[0;34m "+str(sudoku[4][6])+" | "+str(sudoku[4][7])+" | "+str(sudoku[4][8])+"\033[m ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("6 ||\033[0;34m "+str(sudoku[5][0])+" | "+str(sudoku[5][1])+" | "+str(sudoku[5][2])+"\033[m ||\033[0;31m "+str(sudoku[5][3])+" | "+str(sudoku[5][4])+" | "+str(sudoku[5][5])+"\033[m ||\033[0;34m "+str(sudoku[5][6])+" | "+str(sudoku[5][7])+" | "+str(sudoku[5][8])+"\033[m ||")
	print("  ++===+===+===++===+===+===++===+===+===++")
	print("7 ||\033[0;31m "+str(sudoku[6][0])+" | "+str(sudoku[6][1])+" | "+str(sudoku[6][2])+"\033[m ||\033[0;34m "+str(sudoku[6][3])+" | "+str(sudoku[6][4])+" | "+str(sudoku[6][5])+"\033[m ||\033[0;31m "+str(sudoku[6][6])+" | "+str(sudoku[6][7])+" | "+str(sudoku[6][8])+"\033[m ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("8 ||\033[0;31m "+str(sudoku[7][0])+" | "+str(sudoku[7][1])+" | "+str(sudoku[7][2])+"\033[m ||\033[0;34m "+str(sudoku[7][3])+" | "+str(sudoku[7][4])+" | "+str(sudoku[7][5])+"\033[m ||\033[0;31m "+str(sudoku[7][6])+" | "+str(sudoku[7][7])+" | "+str(sudoku[7][8])+"\033[m ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
	print("9 ||\033[0;31m "+str(sudoku[8][0])+" | "+str(sudoku[8][1])+" | "+str(sudoku[8][2])+"\033[m ||\033[0;34m "+str(sudoku[8][3])+" | "+str(sudoku[8][4])+" | "+str(sudoku[8][5])+"\033[m ||\033[0;31m "+str(sudoku[8][6])+" | "+str(sudoku[8][7])+" | "+str(sudoku[8][8])+"\033[m ||")
	print("  ++---+---+---++---+---+---++---+---+---++")
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
	while i<9 and sudoku[i][j] != ' ': #verifica se ainda já jogadas não preenchidas
		while j<9 and sudoku[i][j] != ' ':
			gg = gg + 1
			j = j + 1
		i = i + 1
		j = 0	
	if gg > 80:
		print("PARABENS, VOCE COMPLETOU O SUDOKU!")
		loop = 0

	if verdicas == 0:
		#verificação da validade das dicas
		if len(dicas)-1>80 or not testequad():
			valido = 0
		elif valido==1:
			for i in range(len(dicas)-1):
				for j in range(i+1,len(dicas)-1):
					if dicas[i][4] == dicas[j][4]:
						if (dicas[i][0] == dicas[j][0] and dicas[i][2] != dicas[j][2]) or (dicas[i][0] != dicas[j][0] and dicas[i][2] == dicas[j][2]):
							valido = 0
							print("AS PISTAS NAO SEGUEM AS REGRAS DO JOGO!")
		else:
			verdicas = 1
		
		if valido==0:
			print("JOGO INVALIDO! CONFIGURE AS PISTAS CORRETAMENTE! \n(SUG: USE O COMANDO 'nano PistasConfig.txt')")
			loop = 0


	if loop!=0:
		jogada = input("DIGITE SUA JOGADA:")
		jogada = jogada.split() #verifica a formatação da jogada:
		jogada = "".join(jogada)
		v = jogada.find(',')
		p = jogada.find(':')
		vc = False #valicação da letra da jogada
		contador = 0
		while not vc and contador < 18: #testa se coluna tem caractere permitido
			if jogada[0] == caracts[contador]:
				vc = True
			contador = contador + 1
		if jogada == 'X':
			print("JOGO ENCERRADO!")
			loop = 0
			comand = 1
		elif jogada == 'INFO':
			info ()
			comand = 1
		elif (len(jogada) != 5 or v !=1 or p !=3 or int(jogada[2]) == 0 or int(jogada[4]) == 0 or not vc) and len(jogada)!=4:
			print("FORMATO DA JOGADA NAO COMPREENDIDO!")
			valido2 = 0
		
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
				print("FORMATO DE JOGADA DE DELECAO NAO COMPREENDIDO!")
				valido2 = 0
			else:
				vd = False #variável para verificação de dica
				contador = 0
				while not vd and contador < len(dicas) - 1: #testa se jogada tenta deletar uma dica
					if str(dic[jogada[1]]) == str(dicas[contador][0]) and str(jogada[3]) == str(dicas[contador][2]):
						vd = True
					contador = contador + 1
				if vd:
					print("DICAS NAO PODEM SER DELETADAS!")
					valido2 = 0
				else: #deletando a jogada
					l = int(jogada[3]) - 1
					c = int(dic[jogada[1]])
					sudoku[l][c] = ' '
					print('\n'*130)
					layout()
					print("JOGADA DELETADA!")
					delecao = 1 #variável para impedir outras ações do programa
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
			
			if not testequad():
				valido2 = 0
	
		if valido2 == 0:
			print("JOGADA INVALIDA!")
		elif valido2 == 1 and delecao == 0 and comand == 0:
			numeroant = sudoku[linha][coluna]
			sudoku[linha][coluna] = numero
			print('\n'*130)
			layout()
		if not testequad() and delecao == 0 and comand == 0:
			sudoku[linha][coluna] = numeroant
			print('\n'*130)
			layout()
			print("HA VALORES IGUAIS EM UM MESMO QUADRANTE!")
			print("JOGADA INVALIDA!")

