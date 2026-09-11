# 📊 Calculadora de Consumo de Energia Elétrica

Este projeto é uma aplicação simples desenvolvida para ajudar no cálculo e monitoramento do consumo de energia elétrica de eletrodomésticos, permitindo uma melhor gestão dos gastos residenciais.

## 🚀 Objetivo do Sistema
O objetivo principal é calcular o consumo em quilowatts-hora (kWh) de um aparelho a partir de sua potência e tempo de uso, estimando também o custo financeiro final com base na tarifa local.

## 🛠️ Tecnologias e Recursos
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-⚡-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

## 🧮 Fórmula Utilizada para o Cálculo

O cálculo do consumo elétrico e do custo financeiro baseia-se nas seguintes fórmulas matemáticas:

1. **Consumo Mensal (kWh):**
   $$\text{Consumo (kWh)} = \frac{\text{Potência (W)} \times \text{Horas de Uso por Dia} \times \text{Dias de Uso}}{1000}$$

2. **Custo Total (R$):**
   $$\text{Custo Total} = \text{Consumo (kWh)} \times \text{Tarifa da Distribuidora (R\$/kWh)}$$

## 💻 Instruções para Executar o Programa

Siga os passos abaixo para clonar e rodar o projeto localmente em sua máquina:

### Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado no seu sistema.

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. **Navegar até o diretório do projeto:**
   ```bash
   cd nome-do-repositorio
   ```

3. **Executar o script principal:**
   ```bash
   python main.py
   ```

4. **Interagir com o terminal:**
   Insira os dados solicitados (potência em Watts, horas de uso diário e o valor da tarifa) para visualizar o resultado imediatamente no terminal.
