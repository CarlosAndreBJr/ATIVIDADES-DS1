
eletrodomestico = input("Digite o nome do aparelho (ex.: Geladeira): ")
watts = float(input(f"Digite a potência do {eletrodomestico} em watts (W): "))
horas_dia = float(input(f"Digite o tempo médio de uso diário do {eletrodomestico} em horas: "))

preco_watts = 0.62
consumo_mensal = (watts * horas_dia * 30) / 1000
custo_mensal = (consumo_mensal*preco_watts) 

print(f"\nO consumo mensal do aparelho ({eletrodomestico}) é de: {consumo_mensal:.1f} kWh e seu custo mensal com energia para esse aparelho é {custo_mensal} reais por mes") 