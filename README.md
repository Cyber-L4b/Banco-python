# 🏦 Sistema Bancário em Python

Este projeto simula um sistema bancário simples, com funcionalidades de cadastro de usuários, criação de contas bancárias, depósitos, saques e geração de extratos. 

## 📌 Funcionalidades

- ✅ Criar usuários (CPF único)
- ✅ Criar contas bancárias (associadas a usuários)
- ✅ Realizar depósitos
- ✅ Realizar saques (com limite de valor e de quantidade diária)
- ✅ Visualizar extrato de transações
- ✅ Listar todas as contas cadastradas
- ✅ Interface via terminal (CLI)

## 📚 Conceitos Aplicados

- Programação procedural em Python
- Estrutura de dados (listas, dicionários)
- Argumentos posicionais e nomeados
- Funções com parâmetros opcionais e nomeados
- Boas práticas de código limpo e modular
- Simulação de múltiplos usuários e contas

## 💡 Regras de Negócio

- Cada usuário é identificado pelo CPF (não pode haver dois usuários com o mesmo CPF)
- Cada conta bancária está vinculada a um único usuário
- Saques têm limite de R$500 por operação
- Só são permitidos até 3 saques por dia
- Depósitos e saques devem ser maiores que zero

## 🖥️ Demonstração

```bash
=============== MENU ================
[1] Criar usuário
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar contas
[7] Sair
=> 
