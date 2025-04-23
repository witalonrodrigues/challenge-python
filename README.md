# Mapa da Dor - Hospital Infantil Sabará

Sistema interativo para gerenciamento de pacientes pediátricos, com foco no registro de sintomas e exames de forma lúdica e eficiente. Desenvolvido como parte de um projeto acadêmico com aplicação real no ambiente hospitalar, utilizando **Python**, **DynamoDB** e **Pandas**.

---

## Sobre o Projeto

O **Mapa da Dor** tem como objetivo facilitar a comunicação entre crianças e profissionais da saúde, permitindo o registro preciso de sintomas, exames e movimentações hospitalares. 

---

## Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) – SDK da AWS para Python
- [Pandas](https://pandas.pydata.org/) – análise e geração de relatórios
- [python-dotenv](https://pypi.org/project/python-dotenv/) – gerenciamento de variáveis de ambiente

---

## ⚙️ Funcionalidades

### Área do Médico
- Buscar paciente por ID, nome ou RG
- Registrar e remover sintomas
- Registrar exames
- Gerar relatório dos pacientes em CSV
- Remover pacientes
- Listar todos os pacientes

### Área do Paciente
- Cadastro de novo paciente
- Registro de sintomas

---

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

## Variáveis de ambiente
Crie um arquivo .env na raiz do projeto com suas credenciais da AWS:

env

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

## Como Executar

Este sistema roda via terminal.

Após instalar as dependências e configurar suas variáveis de ambiente:

```bash
python main.py
```

## Relatórios

Geração de relatório automática em .csv com os seguintes dados:

- Nome
- Idade
- Gênero
- Sintomas

## Autor
Desenvolvido por: Witalon Antonio Rodrigues - RM559023
