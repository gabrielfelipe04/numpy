import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Questão 1
# A função normal(size=n) do modulo random do numpy cria n números aleatórios seguindo uma distribuição normal. 
# Sabendo o uso dessa função faça:
# Crie um array 1000 números aleatórios usando essa função.
values = np.random.normal(1, 1, 1000)
print(f'{values}\n')
# Plote os números usando o ponto como marcador.
plt.plot(values, 'o')

# Faça o histograma do array. (Gráfico de barra)
plt.bar(values, values)
plt.show()

# Calcule a média
media = np.mean(values)
print(f'Média: {media}\n')
# E o desvio padrão do array.
desvio_padrao = np.std(values)
print(f'Desvio padrão: {desvio_padrao}\n')

# Percorra o array e identifique quais pontos são maiores(>) que a média mais duas vezes(2x) o desvio padrão. 
# Armazene esses pontos em uma lista.
lista = []
# Duas vezes(2x) o desvio padrão (limite):
limite = media + (2 * desvio_padrao)
for i in range(len(values)):
    if values[i] > limite:
        lista.append(values[i])
    else:
        continue
print(f'Limite: {limite}\n')

print(f'Lista: {lista}\n')



# Calcule a média dos pontos armazenados na lista
mediaLista = np.mean(lista)
print(f'Média Lista: {mediaLista}\n')
# Calcule o desvio padrão dos pontos armazenados na lista
desvio_padraoLista = np.std(lista)
print(f'Desvio padrão Lista: {desvio_padraoLista}\n')



# Questão 2
# Um tipo de experimento comum é submeter uma pessoa a algum estímulo enquanto se regsitra algum sinal eletrofisiológico. 
# Nesse tipo de experimento, geralmente estamos interessados em analisar uma certa quantidade de pontos antes e depois 
# do estímulo ser apresentado. Cada corte antes e depois do estímulo é chamado de trial.

# Gere agora 12000 pontos usando a função normal. Esses 12000 pontos vão representar nosso sinal.
pontos = np.random.normal(1, 1, 12000)
# Crie um array com 10 linhas, onde cada linha vai conter 500 pontos antes e depois de um certo evento, 
# ou seja esse array deve ter dimensão 10x1000.
array = np.reshape(pontos, (10, 1200))
print(array)
print('-' * 30)
# Os eventos aconteceram nos índices: 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000 e 10000.
print('Os eventos aconteceram nos índices: ')
for i in range(len(array)):
    print(array[i][1199])
print('-'* 30)
# Cada linha desse array é um trial.

# Calcule a média para cada uma das 10 linhas da matriz nova:
linhas = [
    'linha 1: ', 'linha 2: ', 'linha 3: ', 'linha 4: ', 'linha 5: ', 
    'linha 6: ', 'linha 7: ', 'linha 8: ', 'linha 9: ', 'linha 10: '
    ]
for i in range(len(array)):
    print(f'Média {linhas[i]}: {np.mean(array[i])}')


print('-'* 30)


# Calcule o desvio padrão para cada uma das 10 linhas da matriz nova:
for i in range(len(array)):
    print(f'Desvio Padrão {linhas[i]}: {np.std(array[i])}')

# Calcule o trial médio que vai ter tamanho 1x1000
# Criando trial medio ???
trial_medio = np.empty(1200).reshape(1, 1200)
# depois sua média: 
media_TrialMedio = np.mean(trial_medio)
desvio_TrialMedio = np.std(trial_medio)
print('-' * 30)
print(f'Media Trial Médio: {media_TrialMedio}')
print(f'Media Trial Médio: {desvio_TrialMedio}')



# Questão 3
# O comando do numpy linspace(start, stop, num) cria uma quantidade de pontos igual a num no intervalo entre start e stop.
# Use a função normal para gerar 500 pontos e salve em uma variável chamada data
start = int(input('Start: '))
stop = int(input('Stop: '))
data = np.linspace(start, stop, 500)
print(data)
# e depois responda as questões abaixo.

# Use linspace() para gerar 501 pontos entre 0 e 100 e armazene em uma variável chamada f.
f = np.linspace(0, 100, 501)


# Crie uma função que recebe 3 parâmetros: start, end e array. A função deve retornar os dois índices de onde o valor mais próximo de start e end foram encontrados no array.

def MaisProximo(array, start, end):
    array = np.asarray(array)
    indice1 = (np.abs(array - start)).argmin()
    indice2 = (np.abs(array - end)).argmin()
    print(indice1)
    print(indice2)
    return indice1, indice2


print('-'*10)

print(f)
# Usando a função criada no passo anterior, encontre os índices do array f onde o start é igual a 1 e o end é igual a 4.
MaisProximo(f, 1, 4)
# Repita esse passo para start e end iguais a (4, 12) e (12, 30).
MaisProximo(f, 4, 12)
MaisProximo(f, 12, 30)

# Usando os indíces de cada intervalo calcule a média e o desvio padrão para cada intervalo de indices da variável data.
intervalo1 = [f[5:21]]
print(intervalo1)
mediaIntervalo1 = np.mean(intervalo1)
print(mediaIntervalo1)
desvioIntervalo1 = np.std(intervalo1)
print(desvioIntervalo1)

intervalo2 = [f[20:60]]
print(intervalo2)
mediaIntervalo2 = np.mean(intervalo2)
print(mediaIntervalo2)
desvioIntervalo2 = np.std(intervalo2)
print(desvioIntervalo2)

intervalo3 = [f[60:150]]
print(intervalo3)
mediaIntervalo3 = np.mean(intervalo3)
print(mediaIntervalo3)
desvioIntervalo3 = np.std(intervalo3)
print(desvioIntervalo3)

# Crie um gráfico de barras para plotar a média dos 3 intervalos. Use o desvio padrão para mostrar a barra de erro de cada barra.
N = 3  # Numero de elementos
medias = (mediaIntervalo1, mediaIntervalo2, mediaIntervalo3)
d = (desvioIntervalo1, desvioIntervalo2, desvioIntervalo3)
ind = np.arange(N)
width = 0.5
p1 = plt.bar(ind, medias, width, yerr=d)

plt.ylabel('Pontuação')
plt.title('Intensidade de Crise')
plt.xticks(ind, ('mediaIntervalo 1', 'mediaIntervalo 2', 'mediaIntervalo 3'))
plt.yticks(np.arange(0, 32, 2))
gic = plt.show()
