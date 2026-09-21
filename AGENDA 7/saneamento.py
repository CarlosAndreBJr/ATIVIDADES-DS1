def classificar_consumo():
    print("--- CAMPANHA DE CONSCIENTIZAÇÃO AMBIENTAL ---")
    
    # Entrada de dados com padronização para letras minúsculas
    tipo_imovel = input("Digite o tipo de imóvel (casa, apartamento ou comercial): ").strip().lower()
    
    try:
        # Entrada do consumo permitindo que o usuário digite vírgula ou ponto
        consumo_input = input("Digite o consumo mensal de água em m³: ").strip().replace(',', '.')
        consumo = float(consumo_input)
    except ValueError:
        print("Erro: Por favor, insira um número decimal válido para o consumo.")
        return

    # Regras de Negócio para Classificação e Alertas
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
        
    elif tipo_imovel == "apartamento" and consumo < 10.0:
        print("Consumo econômico – excelente controle de água!")
        
    elif tipo_imovel == "apartamento" or (tipo_imovel == "casa" and consumo <= 25.0):
        print("Consumo moderado – dentro do padrão residencial.")
        
    elif tipo_imovel in ["casa", "apartamento"]:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
        
    else:
        print("Erro: Tipo de imóvel inválido. Escolha entre 'casa', 'apartamento' ou 'comercial'.")

if __name__ == "__main__":
    classificar_consumo()
