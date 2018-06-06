#LEITOR DO ARQUIVO DE TEXTO
arquivo = open('arquivo.txt')
dicas = arquivo.read()
dicas = dicas.split()
print(dicas)
