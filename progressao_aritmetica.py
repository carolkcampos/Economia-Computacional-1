# Entrada de dados 
## Solicita os valores do usuário
n = int(input("\nDigite o valor de n (o termo desejado): "))
primeiro_termo = float(input("\nDigite o primeiro termo da progressão: "))
razao = float(input("\nDigite a razão da progressão: "))

# Processamento de dados
## Calcula o n-ésimo termo
n_esimo_termo = primeiro_termo + (n - 1) * razao

## Calcula a soma dos termos
soma_termos = (n * (primeiro_termo + n_esimo_termo)) / 2

# Saída de dados
print(f"O n-ésimo termo da progressão é:, {n_esimo_termo}")
print(f"A soma dos termos da progressão até o {n}, º termo é: {soma_termos}")
