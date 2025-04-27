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
- Registro de Sintomas: Médicos podem registrar sintomas e exames dos pacientes, enquanto pacientes podem informar sintomas específicos.

- Exclusão e Busca de Pacientes: O sistema permite excluir ou buscar pacientes registrados.

- Relatório de Pacientes: O sistema gera um arquivo CSV contendo informações de todos os pacientes cadastrados, incluindo sintomas e exames.

### Área do Paciente
- Cadastro de Pacientes: Permite o cadastro de novos pacientes, incluindo informações pessoais e identificadoras.
- Registro de Sintomas: Médicos podem registrar sintomas e exames dos pacientes, enquanto pacientes podem informar sintomas específicos.

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

## Funcionamento do Sistema
### Banco de Dados DynamoDB
O projeto utiliza o AWS DynamoDB para armazenar informações dos pacientes, sintomas e exames. As tabelas essenciais são:

- Pacientes: Armazena as informações pessoais de cada paciente, como nome, idade, sexo, RG, etc.

- Sintomas: Armazena os sintomas registrados para cada paciente, relacionados a diferentes partes do corpo.

## Diagrama
![python drawio](https://github.com/user-attachments/assets/3163a569-7f2e-45bb-8b33-f1718e1f0752)



### Fluxo de Execução
- Cadastro de Pacientes: O responsável do paciente realiza o cadastro, fornecendo as informações necessárias.

- Registro de Sintomas: O médico ou paciente registra os sintomas do paciente em diferentes partes do corpo. O sistema oferece uma lista de sintomas pré-definidos para facilitar a escolha.

- Exame e Resultados: Os médicos podem registrar exames realizados, bem como os resultados obtidos.

- Busca e Remoção de Pacientes: O sistema permite ao médico buscar pacientes por nome ou RG, além de remover registros de pacientes.

- Relatórios: O sistema gera relatórios em formato CSV com as informações dos pacientes, sintomas e exames.

## Como Executar

Após instalar as dependências e configurar suas variáveis de ambiente:

```bash
python main.py
```
A interação com o sistema é feita via terminal. O menu de opções é exibido a cada etapa e o usuário deve selecionar uma opção através de números correspondentes.

### Exemplo de Menu
```
Sistema Hospital Sabará
Você é:
1 - Médico
2 - Paciente
0 - Sair
```

### Instruções:
O usuário deverá digitar 1, 2, 3, etc para selecionar a ação desejada.

Cada número corresponde a uma funcionalidade específica. O sistema processará a seleção e, dependendo da escolha, executará a ação correspondente.

Caso o número não corresponda a uma opção válida, o sistema solicitará uma nova entrada até que uma opção válida seja escolhida.

### Relatórios

Geração de relatório automática em .csv com os seguintes dados:

- Nome
- Idade
- Gênero
- Sintomas

## Autores
- Lucas Alves Piereti - RM559533
- Rafaela Heer Robinson - RM560249
- Julia Hadja Kfouri Nunes - RM559410
- Witalon Antonio Rodrigues - RM559023
