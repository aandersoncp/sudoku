'''
SUDOKU PARA TERMINAL PYTHON 3 (MOOD INTEGRADO)
CRIADO POR:
GUSTAVO MARQUES
'''

while True:
	print ("BEM-VINDO AO SUDOKU PYTHON 3")
	print("- Entre 'i' para MODO INTERATIVO\n- Entre 'b' para MODO BATCH\n- Entre 's' para sair")
	comandoi = input("Entrada: ")

	if comandoi == 's' or comandoi == 'S':
		break

	elif comandoi == 'i' or comandoi == 'I':
		try:
			from SudokuInterativo import *
			print("MODO ENCERRADO")

		except:
			print("Erro, arquivo 'SudokuInterativo.py' corrompido ou não encontrado!")

	elif comandoi == 'b' or comandoi == 'B':
		try:			
			print("---------SUDOKU - MODO BATCH----------")
			from SudokuBatch import *
			print("MODO ENCERRADO")

		except:
			print("Erro, arquivo 'SudokuBatch.py' corrompido ou não encontrado!")


	else:
		print("ENTRADA INVALIDA!")

