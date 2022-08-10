vazia = []
print('lista vazia', vazia, type(vazia))

frutas = ['maçã', 'uva', 'melancia']
print('frutas', frutas)

hobbies = ['trico', 'bordado', 'puzze']
hobbies.append('patins')
print('hobbies', hobbies)

numeros = [5, 1, 4, 8, 2, 6]
numeros.sort()
print('ordenação', numeros)
numeros.reverse()
print('ordenação reversa', numeros)
print('tamanho lita', len(numeros))

concatenar = frutas + hobbies
print('concatenar', concatenar)


print("\nFatiar\n")
lista = [0, 1, 2, 3, 4, 5]
print('pega todos os elementos até o indice 4', lista[:4])
print('pega todos os elementos a partir do indice 3', lista[3:])
print('pega os elementos a partir do indice 1 e antes do indice 3', lista[1:3])

print("\nRemover elementos\n")
del lista[0]
print('usar del', lista)

lista.pop(4)
print('usar pop', lista)