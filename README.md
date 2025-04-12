# 💰 Sistema Bancário Simples

Um projeto de terminal feito em Python, simulando funcionalidades básicas de um sistema bancário.

## 📄 Informações Gerais

- **Autor:** Jessé Miguel Ramos  
- **Data de Criação:** 05/04/2025  
- **Última Atualização:** 12/04/2025  
- **Versão:** 1.1  

## 🧠 Funcionalidades

Este sistema oferece as seguintes operações:

- [1] Depositar
- [2] Sacar
- [3] Exibir Extrato
- [4] Criar Novo Usuário
- [5] Listar Contas Criadas
- [6] Criar Nova Conta Bancária
- [0] Sair do sistema

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Módulo `textwrap` (nativo do Python)

## 🧾 Regras de Negócio

- O usuário só pode realizar até **3 saques diários**.
- Cada saque deve ser de no **máximo R$ 500,00**.
- Só é possível realizar operações com valores **positivos**.
- O extrato mostra todas as movimentações (depósitos e saques) e o saldo atual.
- Usuários são identificados unicamente pelo CPF.
- Uma conta bancária só pode ser criada se o CPF do usuário já estiver cadastrado.

## ✅ Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Jesse-DEVs/sistema-bancario.git
   cd sistema-bancario
   ```

2. Execute o programa:
   ```bash
   python sistema_bancario.py
   ```

3. Use o menu exibido para interagir com o sistema.

## 🧑‍💻 Estrutura do Código

- **Funções principais:** depositar, sacar, exibir extrato, criar usuário, criar conta, listar contas.
- **Função `main()`** gerencia o fluxo principal do sistema e interage com o usuário via terminal.

## 📌 Observações

- Este sistema não utiliza banco de dados — os dados são armazenados apenas em memória durante a execução.
- Ideal para fins didáticos e prática de conceitos básicos de **funções**, **listas**, **dicionários**, **parâmetros especiais (`/` e `*`)** e **lógica de negócios**.
