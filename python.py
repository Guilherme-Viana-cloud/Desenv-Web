produto = str(input('Qual o nome do produto? '))
quantidade = int(input('Quantos produtos você comprou? '))

if quantidade < 5:
    desconto = 'sem desconto'

elif 5 <= quantidade <= 10:
    desconto = 'desconto de 5%'

elif 11 <= quantidade <= 20:
    desconto = 'desconto de 10%'

else:
    desconto = 'desconto de 15%'

print(f'Você comprou {quantidade} unidades de {produto}. Com base na sua compra, você recebe {desconto}.')
