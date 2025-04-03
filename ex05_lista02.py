#A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha
#trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor
#da hora-extra é o valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalhe
#apenas nos dias úteis, escreva um algoritmo que recebe:
#a) o total de dias úteis de um mês
#b) o total de horas trabalhadas pelo trabalhador
#c) quanto o trabalhador recebe por hora
#Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário final do
#trabalhador.
dias = float(input("dias uteis:  "))
horas_trab = float(input("horas trab:  "))
salario_h= float(input("salario hora:  "))

salario_d = salario_h * 8

salario = salario_d * dias
print(f"Sálario: {salario}")

extra = float(input("total de horas extra mensal:  "))

h_extra = (extra/dias)/8

vh_extra = h_extra * (salario_h+(salario_h*(50/100)))

salario_extra = (vh_extra * 8 *dias) + salario

print(f"salario com hora extra: {salario_extra}")













