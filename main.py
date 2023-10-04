#Importando o Numpy
import numpy as np

#Busca de arquivo externo para realizar as operações com Array
nome_arquivo = "arquivo_array.txt"
with open(nome_arquivo, 'r') as arquivo:
    array = arquivo.read()
    array_int = [int(numero) for numero in array.split()]

#Visualização da lista em array
meu_array = np.array(array_int)
print(f'\nMeu Array é: {meu_array}\n')

#Reshape do array para bidimensional
array_bidimensional = np.array(meu_array).reshape((2,3))
print(f'\nModulando o Array:\n {array_bidimensional}\n')

#Calculo das médias do array
media_linha = np.mean(array_bidimensional, axis=1)
print(f'\nA média das linhas do Array é: {media_linha}\n')

#Calculo da soma das colunas
soma_coluna = np.sum(array_bidimensional, axis=0)
print(f'A soma das colunas é: {soma_coluna}\n')

#Calculo da soma total do array
soma_total = np.sum(array_bidimensional)
print(f'\nA soma total do Array é: {soma_total}\n')

#Matriz transposta
transposta = np.transpose(array_bidimensional)
print(f'\nA matriz transposta é:\n {transposta}\n')

#Operação com a matriz transposta
resultado = transposta * 2
print(f'\nO resultado da operação da matriz transposta é:\n {resultado}\n')

#Media com a matriz transposta
media_linha = np.mean(transposta, axis=1)
print(f'\nA média das linhas da matriz transposta é: {media_linha}\n')

#Soma da coluna da matriz transposta
soma_coluna = np.sum(transposta, axis=0)
print(f'\nA soma das colunas da matriz transposta é: \n {soma_coluna}\n')

#Busca de arquivo externo para realizar as operações com Matriz e Array
outra_matriz = "matriz.txt"
with open(outra_matriz, 'r') as arquivo:
    matriz = arquivo.read()
    matriz_int = [int(numero) for numero in matriz.split()]

#Visualização em array
minha_matriz = np.array(matriz_int)
print(f'\nMeu Array é: {minha_matriz}\n')

#Reshape do array para bidimensional
minha_matriz = np.array(matriz_int).reshape((3,2))
print(f'\nModulando o Array:\n {minha_matriz}\n')

#Calculo do produto escalar
produto_escalar = np.dot(array_bidimensional, minha_matriz)
print(f'\nO produto escalar é:\n {produto_escalar}\n')

#Filtro no array
filtro = array_bidimensional > 55
matriz_filtrada = array_bidimensional[filtro]
print(f'\nA matriz com filtro é:\n {matriz_filtrada}\n')

#Reorganização da matriz
matriz_int = np.array(meu_array).reshape((2,3))
print(f'\nA reorganização da matriz é:\n {matriz_int}\n')

#Soma de ambos
resultado = array_bidimensional + matriz_int
print(f'\nO resultado da soma entre arrays é:\n {resultado}\n')