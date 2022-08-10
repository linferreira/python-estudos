vazio = {}
print(vazio, type(vazio))

estudante = {"nome": "Lindsay", "idade": 25}
print('estudante', estudante)

estudante['matricula'] = '250655'
print('estudante com nova chave', estudante)

print('pegar e organizar por chave e valor', sorted(estudante.items()))

print('pegar e organizar por chaves', sorted(estudante.keys()))

print('pegar o total de itens do dicionarios', len(estudante))

print('por item: nome ==', estudante["nome"])
