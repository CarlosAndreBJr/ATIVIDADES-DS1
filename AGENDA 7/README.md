# 🚰 Sistema de Conscientização de Consumo de Água

> Script em Python desenvolvido para classificar o perfil de consumo de água de imóveis e emitir alertas educativos automáticos.

## 🎯 Sobre o Projeto

Este projeto faz parte de uma campanha de conscientização ambiental promovida pela companhia de saneamento local. O objetivo é engajar os moradores através de feedbacks instantâneos baseados nas regras de consumo de cada categoria de imóvel.

## 🚀 Funcionalidades

* **Classificação por Categoria**: Identifica se o imóvel é comercial, residencial (casa) ou apartamento.
* **Alertas Educativos**: Emite mensagens personalizadas focadas em economia de recursos hídricos.
* **Validação de Dados**: Tratamento inteligente para entradas numéricas decimais.

## 📋 Regras de Negócio Aplicadas

| Tipo de Imóvel | Faixa de Consumo | Mensagem de Alerta |
| :--- | :--- | :--- |
| **Comercial** | Qualquer consumo | *Tarifa comercial aplicada – consulte o plano corporativo.* |
| **Apartamento** | Menor que 10 m³ | *Consumo econômico – excelente controle de água!* |
| **Casa / Apto** | Até 25 m³ | *Consumo moderado – dentro do padrão residencial.* |
| **Casa / Apto** | Acima de 25 m³ | *Consumo excessivo – adote medidas de economia e verifique vazamentos.* |

## 🛠️ Tecnologias Utilizadas

* 🐍 **Python 3.x** - Linguagem base do script.
* 📦 **Git & GitHub** - Controle de versão e hospedagem do código.

## 💻 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe o arquivo `saneamento.py`.
3. Abra o terminal na pasta do arquivo e execute:
   ```bash
   python saneamento.py
   ```
