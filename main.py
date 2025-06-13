import pandas as pd
import uuid
import boto3
from dotenv import load_dotenv
import os
from tabulate import tabulate

load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
tabela_paciente = dynamodb.Table("Pacientes")

mapa_sintomas = {
    "pé": ["dor", "formigamento", "coceira", "frio"],
    "perna": ["dor", "formigamento", "coceira", "frio"],
    "joelho": ["dor", "travamento", "coceira", "frio"],
    "coxa": ["formigamento", "coceira", "dor", "frio"],
    "região pélvica": ["coceira", "dor", "formigamento", "ardência", "vontade de ir no banheiro", "frio"],
    "barriga": ["dor/cólica", "azia", "estufamento", "vontade de ir no banheiro", "frio"],
    "peito": ["dor", "dor nos peitos", "falta de ar", "pressão", "coração acelerado", "coceira", "azia", "estufamento",
              "frio"],
    "braços": ["dor", "coceira", "formigamento", "ardência", "frio"],
    "garganta": ["azia", "coceira", "dor", "ardência", "tosse", "frio"],
    "boca": ["dor de dente", "dor de garganta", "dor ATM", "tosse"],
    "nariz": ["resfriado", "espirro", "coceira"],
    "olhos": ["tontura", "dor", "coceira", "visão embaçada", "cegueira ou escurecimento"],
    "ouvido": ["dor", "coceira", "surdez"],
    "cabeça": ["dor", "coceira", "tontura"]
}

medicos_credenciais = {}


def forca_opcao(msg, lista, msg_erro):
    opcao = input(msg)
    if not opcao in lista:
        print(msg_erro)
        return forca_opcao(msg, lista, msg_erro)
    return opcao


def checa_idade(msg):
    idade = input(msg)
    if not idade.isnumeric():
        print('Digite um número')
        checa_idade(msg)
    return int(idade)


def cadastrar_pacientes():
    print("\n Cadastro de Paciente")

    nome = input("Nome da criança: ")
    idade = checa_idade('Idade da criança: ')
    sexo = input("Sexo (M/F): ")
    nome_responsavel = input("Nome do responsável: ")
    rg = input("RG da criança: ")
    rg_responsavel = input("RG do responsável: ")
    id_paciente = str(uuid.uuid4())

    paciente = {
        'id': id_paciente,
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'nome do responsável': nome_responsavel,
        'rg': rg,
        'rg do responsável': rg_responsavel,
        'sintomas': [],
        'exame': []
    }

    try:
        tabela_paciente.put_item(Item=paciente)
        print("Paciente cadastrado com sucesso!")
        print(f"O ID do paciente é {id_paciente}")
    except Exception as e:
        print(f'Erro ao cadastrar paciente {e}')


def registrar_sintomas():
    print("\n Registro de Sintoma")
    id_paciente = input("ID do paciente: ")
    for key in mapa_sintomas.keys():
        print(key)
    # solicitar qual parte do corpo está ocorrendo o sintoma
    local = forca_opcao("Parte do corpo com sintoma: \n->", mapa_sintomas.keys(), 'Opção Inválida')
    # solicitar sintoma
    sintoma = forca_opcao("Qual o sintoma?\n->", mapa_sintomas[local], 'Sintoma Inválido')

    try:
        resposta = tabela_paciente.get_item(Key={'id': id_paciente})
        if 'Item' in resposta:
            paciente = resposta['Item']
            paciente['sintomas'].append({"local": local, "sintoma": sintoma})
            tabela_paciente.put_item(Item=paciente)
            print("Sintoma registrado com sucesso!")
        else:
            print("Paciente não encontrado.")
    except Exception as e:
        print(f"Erro ao registrar sintoma: {e}")


def remover_sintoma():
    print("\nRemover Sintoma")
    id_paciente = input("ID do paciente: ")

    try:
        resposta = tabela_paciente.get_item(Key={"id": id_paciente})
        if "Item" not in resposta:
            print("Paciente não encontrado.")
            return

        paciente = resposta["Item"]
        sintomas = paciente.get("sintomas", [])

        if not sintomas:
            print("Nenhum sintoma registrado para este paciente.")
            return

        print("\nSintomas registrados:")
        for i, s in enumerate(sintomas):
            print(f"{i + 1} - {s['local']}: {s['sintoma']}")

        indice = int(input("Digite o número do sintoma que deseja remover: ")) - 1

        if 0 <= indice < len(sintomas):
            sintoma_removido = sintomas.pop(indice)
            tabela_paciente.put_item(Item=paciente)
            print(f"Sintoma removido: {sintoma_removido['local']} - {sintoma_removido['sintoma']}")
        else:
            print("Opção inválida.")

    except:
        print(f"Erro ao remover sintoma!")


def buscar_paciente():
    print("\nBuscar Paciente")
    busca = input("Digite o nome ou RG do paciente: ").strip().lower()
    try:
        resposta = tabela_paciente.scan()
        for item in resposta.get('Items', []):
            if busca in item.get('nome', '').lower() or busca in item.get('rg', '').lower():
                print("\nPaciente encontrado:")
                for chave, valor in item.items():
                    print(f"{chave}: {valor}")
                return
        print("Nenhum paciente encontrado com esse dado.")
    except:
        print(f"Erro na busca!")


def remover_paciente():
    print("\nRemover Paciente")
    id_paciente = input("id do paciente: ")

    tabela_paciente.delete_item(Key={'id': id_paciente})
    print("Paciente removido com sucesso!")


def visualizar_pacientes():
    print("\nVisualizar Paciente")
    id_paciente = input("ID do paciente: ")
    try:
        resposta = tabela_paciente.get_item(Key={'id': id_paciente})
        if 'Item' in resposta:
            paciente = resposta['Item']
            print("\nDados do Paciente:")
            for chave, valor in paciente.items():
                print(f"{chave}: {valor}")
        else:
            print("Paciente não encontrado.")
    except:
        print(f"Erro ao buscar paciente:")


def registrar_exame():
    print("\nRegistro de Exame")
    id_paciente = input("ID do paciente: ")
    nome_do_exame = input("Nome do exame: ")
    resultado = input("Resultado do exame: ")

    try:
        resposta = tabela_paciente.get_item(Key={'id': id_paciente})
        if 'Item' in resposta:
            paciente = resposta['Item']
            paciente['exame'].append({"exame": nome_do_exame, "resultado": resultado})
            tabela_paciente.put_item(Item=paciente)
            print("Exame registrado com sucesso!")
        else:
            print("Paciente não encontrado.")
    except:
        print(f"Erro ao registrar exame")


def gerar_relatorio():
    print("\nGerar Relatório CSV")
    try:
        resposta = tabela_paciente.scan()
        pacientes = resposta.get('Items', [])
        if pacientes:
            dados = []
            for paciente in pacientes:
                dados.append({
                    "Nome": paciente.get("nome", ""),
                    "Idade": paciente.get("idade", ""),
                    "Sexo": paciente.get("sexo", ""),
                    "RG": paciente.get("rg", ""),
                    "Sintomas": paciente.get("sintomas", ""),
                    "ID": paciente.get("id", ""),
                    "Nome do Responsável": paciente.get("nome do responsável", ""),
                    "RG do Responsável": paciente.get("rg do responsável", "")
                })

            df = pd.DataFrame(dados, columns=[
                "ID", "Nome", "Idade", "Sexo", "RG", "Sintomas", "Nome do Responsável", "RG do Responsável"
            ])
            df.to_csv('relatorio_de_pacientes.csv', index=False, encoding='utf-8-sig', sep=';')
            print("Relatório gerado com sucesso como 'relatorio_de_pacientes.csv'")
        else:
            print("Nenhum paciente foi encontrado para o relatório ser gerado.")
    except:
        print(f"Erro ao gerar relatório")


def visualizar_todos_pacientes():
    print("\nVisualizar Todos os Pacientes")
    try:
        resposta = tabela_paciente.scan()
        pacientes = resposta.get("Items", [])

        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return

        for paciente in pacientes:
            print("\n----------------------------")
            for chave, valor in paciente.items():
                print(f"{chave}: {valor}")

    except Exception as e:
        print(f"Erro ao buscar pacientes: {e}")

def ler_csv_relatorio():
    try:
        df = pd.read_csv('relatorio_de_pacientes.csv', sep=';', encoding='utf-8-sig')
        print("\nRelatório de Pacientes:\n")
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    except FileNotFoundError:
        print("Arquivo 'relatorio_de_pacientes.csv' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o relatório: {e}")

def cadastrar_medico():
    print("\nCadastro de Médico")
    crm = input("Informe o CRM: ")
    if crm in medicos_credenciais:
        print("CRM já cadastrado.")
        return False
    senha = input("Crie uma senha: ")
    medicos_credenciais[crm] = senha
    print("Cadastro realizado com sucesso!")
    return True

def login_medico():
    print("\nLogin de Médico")
    crm = input("CRM: ")
    senha = input("Senha: ")
    if crm in medicos_credenciais and medicos_credenciais[crm] == senha:
        print("Login bem-sucedido!\n")
        return True
    else:
        print("CRM ou senha incorretos.")
        return False

def autenticar_medico():
    while True:
        print("\n[Autenticação de Médico]")
        print("1 - Login")
        print("2 - Cadastro")
        print("0 - Voltar ao menu principal")
        acao = input("Escolha uma opção: ")

        if acao == '1':
            while True:
                print("\n[Login de Médico]")
                crm = input("CRM (ou 0 para voltar): ")
                if crm == '0':
                    return False
                senha = input("Senha: ")

                if crm in medicos_credenciais and medicos_credenciais[crm] == senha:
                    print("Login bem-sucedido!\n")
                    return True
                else:
                    print("\nCRM ou senha incorretos.")
                    print("1 - Tentar novamente")
                    print("2 - Voltar ao menu principal")
                    tentativa = input("Escolha uma opção: ")
                    if tentativa == '2':
                        return False
        elif acao == '2':
            print("\n[Cadastro de Médico]")
            crm = input("Informe o CRM (ou 0 para voltar): ")
            if crm == '0':
                return False
            if crm in medicos_credenciais:
                print("CRM já cadastrado.")
                continue
            senha = input("Crie uma senha: ")
            medicos_credenciais[crm] = senha
            print("Cadastro realizado com sucesso!")
        elif acao == '0':
            return False
        else:
            print("Opção inválida.")
menu_medico = {
    "1": registrar_exame,
    "2": visualizar_pacientes,
    "3": buscar_paciente,
    "4": remover_paciente,
    "5": registrar_sintomas,
    "6": remover_sintoma,
    "7": gerar_relatorio,
    "8": ler_csv_relatorio
}

menu_paciente = {
    "1": cadastrar_pacientes,
    "2": registrar_sintomas
}


def menu():
    while True:
        print("\n Sistema Hospital Sabará")
        print("Você é:")
        print("1 - Médico")
        print("2 - Paciente")
        print("0 - Sair")

        tipo_usuario = forca_opcao('\nEscolha uma opção\n-> ', ['1', '2', '0'], 'Opção inválida. Tente novamente.')

        if tipo_usuario == "1":
            autenticar_medico()
            while True:
                while True:
                    print("\n Sistema Hospital Sabará")
                    print("Você é:")
                    print("1 - Médico")
                    print("2 - Paciente")
                    print("0 - Sair")

                    tipo_usuario = forca_opcao('\nEscolha uma opção\n-> ', ['1', '2', '0'],
                                               'Opção inválida. Tente novamente.')

                    if tipo_usuario == "1":
                        if autenticar_medico():
                            while True:
                                print("\n Menu Médico")
                                print("1 - Registrar Exame")
                                print("2 - Visualizar Paciente")
                                print("3 - Buscar Paciente")
                                print("4 - Remover Paciente")
                                print("5 - Registrar Sintomas")
                                print("6 - Remover Sintomas")
                                print("7 - Gerar Relatório CSV")
                                print("8 - Ler Relatório CSV")
                                print("0 - Voltar")

                                opcao = forca_opcao("\nEscolha uma opção\n-> ",
                                                    ['1', '2', '3', '4', '5', '6', '7', '8', '0'],
                                                    "Opção inválida. Tente novamente.")

                                if opcao == "0":
                                    break
                                else:
                                    menu_medico[opcao]()
                        else:
                            continue

                    elif tipo_usuario == "2":
                        while True:
                            print("\nMenu Paciente")
                            print("1 - Fazer o cadastro")
                            print("2 - Registrar Sintoma")
                            print("0 - Voltar")

                            opcao = forca_opcao("Escolha uma opção\n-> ", ['1', '2', '0'],
                                                "Opção inválida. Tente novamente.")

                            if opcao == '0':
                                break
                            else:
                                menu_paciente[opcao]()

                    elif tipo_usuario == "0":
                        print("Saindo do sistema...")
                        break


if __name__ == "__main__":
    menu()
