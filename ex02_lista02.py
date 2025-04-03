#Escrever um algoritmo que leia dois valores inteiro 
#distintos e informe qual é o maior ou se
#houve um empate.

num_1 = int(input("Escreva o primeiro número inteiro:  "))
num_2 = int(input("Escreva o segundo número inteiro:  "))

if num_1<num_2:
    print(f"{num_1} é menor que {num_2}")
else:
    if num_1>num_2:
        print(f"{num_1} é maior que {num_2}")
    else:
        print(f"{num_1} e {num_2} são iguais")
    
        
    

        