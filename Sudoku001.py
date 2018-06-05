#LEITOR DO ARQUIVO DE TEXTO
arquivo = open('arquivo.txt', 'r')
lista = []
dicas = arquivo.read()
dicas = dicas.split()
print(dicas)
