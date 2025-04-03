#Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.
num_a = int(input("Número A:  "))
num_b = int(input("Número B:  "))

div = num_a % num_b

if div == 0:
    print(f"{num_a} é divisível por {num_b}")
else:
    print(f"{num_a} não é divisível por {num_b}")