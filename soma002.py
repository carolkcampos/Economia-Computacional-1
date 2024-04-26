# Este código produz a soma de dos números 

# Alocação de memória 
parcela = 0
soma = 0
num = 0

# Entrada e processamento de dados
while parcela < 2:
    num = int(input(f"\nInforme a parcela {parcela + 1}"))
    soma = soma + num
    parcela += 1 # isto aqui é a mesma coisa que parcela = parcela + 1 

# Saída de dados
print(f"A soma dos números é igual a {soma}.")