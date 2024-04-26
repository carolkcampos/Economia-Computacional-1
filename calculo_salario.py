# Alocação de memória 

valor_hora_aula = 40
taxa_imposto = 0.30

# Entrada de dados

horas_trabalhadas_semana = float(input("\nOlá! Quantas horas você trabalha por semana?"))

# Calcula horas trabalhadas por mês

horas_trabalhadas_mes = horas_trabalhadas_semana * 4

# Calcula do salário bruto

salario_bruto = horas_trabalhadas_mes * valor_hora_aula

# Calcula o valor descontado pelo imposto

valor_descontado = salario_bruto * taxa_imposto

# Calcula o valor do salário líquido

salario_liquido = salario_bruto - valor_descontado

# Saída de dados

print(f"Seu salário bruto é igual a {salario_bruto}")
print(f"O valor descontado por impostos do seu salário é igual a {valor_descontado}")
print(f"O valor do seu salário líquido é igual a {salario_liquido}")
