lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
lista_produtos[lista_produtos.index('batons')] = 'rímel'
lista_produtos[lista_produtos.index('loções')] = 'cremes hidratantes'
lista_produtos.remove('delineadores')
lista_produtos.extend(['hidratação', 'condicionadores'])
print(lista_produtos)