#LEITOR DO ARQUIVO DE TEXTO
arquivo = open('arquivo.txt', 'r')
#print(arquivo.read())
lista = []
dicas = arquivo.read()
dicas = dicas.split()
print(dicas)