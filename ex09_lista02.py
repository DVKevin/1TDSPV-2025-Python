#No exercício da calculadora, visto em sala de aula, temos um problema com a operação
#de divisão. Sua tarefa será exibir uma mensagem informando que é impossível fazer uma
#divisão por 0. Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer
#tal operação.

num_a = float(input("Digite um número:  "))
op = input("Digite o operador (+-*/): ")
num_b = float(input("Digite outro número:  "))
if op == '+':
    resultado = num_a + num_b
elif op =='-':
    resultado = num_a - num_b
elif op =='*':
    resultado = num_a * num_b
elif op =='/':
    resultado = num_a / num_b
else:
    print(f"Operador{op} inválido!")
    resultado = None #vazio ou nada    
if num_a or num_b == 0:
    print("número invalido")


print(f"Resulado de {num_a}{op}{num_b} = {resultado}")

