#Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
#normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a
#seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
#código condição de pagamento
#1 A vista em dinheiro ou cheque, recebe 10% de desconto
#2 A vista no cartão de crédito, recebe 5% de desconto
#3 Em duas vezes, preço normal de etiqueta sem juros
#4 Em quatro vezes, preço normal de etiqueta mais juros de 7%
produto = float(input("valor do produto:  "))
pagamento = float(input("método de pagamento: "))

if pagamento == 1:
    resultado = produto * 10/100
elif pagamento == 2:
    resultado = produto * 5/100
elif pagamento == 3:
    resultado = produto
elif pagamento == 4:
    resultado = produto * 7/100
    
valor = (produto - resultado)

if pagamento >3:
    valor = (produto + resultado)
else:
    valor = (produto - resultado)
    
if resultado != None:
 print(f"valor do produto com descon é de {valor}")