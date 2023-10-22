print("                          CALCULADORA DE SALÁRIO            ")
print("                          ------------------                ")

print(' ')
print('                             COMO USAR?                     ')
print(' ')
print('                               """"""""                     ')
print(' ')
print('1 - Digite o seu salário bruto.                             ')
print('2 - O programa irá criar um recibo de pagamento.')
print('3 - O recibo de pagamento terá o valor: SALÁRIO BRUTO - INSS - IRRF => SALARIO LIQUIDO')
print('4 - Este programa não irá calcular outros descontos atrelados à folha de pagamento')
print(' ')
print('                               """"""""                     ')

salario_bruto = float(input("Digite o valor do seu SALÁRIO BRUTO: R$ "))
print(' ')

if salario_bruto <= 1320.00:
    desconto_inss = salario_bruto * 0.075
elif salario_bruto > 1320.01 and salario_bruto <= 2571.29:
    desconto_inss = (((salario_bruto - 1320) * 0.09) + 99)
elif salario_bruto > 2571.30 and salario_bruto <= 3856.94:
    desconto_inss = (((salario_bruto - 2571.29)* 0.12) + 99 + 112.62)    
elif salario_bruto > 3856.95 and salario_bruto <= 7507.49:
    desconto_inss = (((salario_bruto - 3856.94)* 0.14) + 99 + 112.62 + 154.28)
else:
    print("Valor inválido")

bc_irrf = salario_bruto - desconto_inss

if bc_irrf <= 2112.00:
    desconto_irrf = 0
elif bc_irrf > 2112.01 and bc_irrf <= 2826.65:
    desconto_irrf = (bc_irrf * 0.075) - 158.40
elif bc_irrf > 2826.66 and bc_irrf <= 3751.06:
    desconto_irrf = (bc_irrf * 0.15) - 370.40
elif bc_irrf > 3751.07 and bc_irrf <= 4664.68:
    desconto_irrf = (bc_irrf * 0.225) - 651.73
elif bc_irrf > 4664.69:
    desconto_irrf = (bc_irrf * 0.275) - 884.96
else:
    print("Valor inválido")

print("                          RECIBO PAGAMENTO                                      ")
print("                          ------------------                                    ")
print("                                                                                ")
print("PROVENTOS/DESCONTOS           VALOR                                             ")
print(f"SALARIO BRUTO:           R$ {salario_bruto:.2f}                                ")
print(f"DESCONTO INSS            R$ {desconto_inss:.2f}                                ")
print(f"DESCONTO IRRF            R$ {desconto_irrf:.2f}                                ")
print(f"SALARIO LIQUIDO          R$ {salario_bruto - desconto_inss - desconto_irrf:.2f}")
print("                                                                                ")
print("                          ------------------                                    ")
    


