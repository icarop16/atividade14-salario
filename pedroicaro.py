# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Escreva o valor do seu salario: "))
if salario > 1250.00:
    aumento10 = (salario*10)/100
    salarioAlm = salario + aumento10
    print(f"Seu salário, que era de R${salario}, recebeu um aumento de R${aumento10} e passara a ser R${salarioAlm}")
elif salario == 1250.00: 
    aumento15 = (salario*15)/100
    salarioAlm_2 = salario + aumento15
    print(f"Seu salário, que era de R${salario}, recebeu um aumento de R${aumento15} e passara a ser R${salarioAlm_2}")
else:
    aumento15_2 = (salario*15)/100
    salarioAlm_3 = salario + aumento15_2
    print(f"Seu salário, que era de R${salario}, recebeu um aumento de R${aumento15_2} e passara a ser R${salarioAlm_3}")
    
 

