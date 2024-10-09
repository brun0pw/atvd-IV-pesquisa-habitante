import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    sexo: str
    idade: int
    salario: int

@dataclass    
class Habitante_Regiao:
    media_salarial: float
    menor_idade: int
    maior_idade: int
    quantidade_de_mulheres: int

# Função para calcular a média salarial
def media(lista_salario):
    if len(lista_salario) == 0:
        return 0
    return sum(lista_salario) / len(lista_salario)

# Função para determinar maior e menor idade
def idade(lista_idade):
    if len(lista_idade) == 0:
        return None, None
    return min(lista_idade), max(lista_idade)

# Função para criar o arquivo
def criar_arquivo():
    return "Pesquisa_Habitante.txt"

# Função para ler os dados do arquivo e calcular as estatísticas
def ler_dados_do_arquivo():
    lista_idade = []
    lista_salario = []
    mulheres_ricas = 0
    nome_do_arquivo = criar_arquivo()

    # Abrir e ler o arquivo
    with open(nome_do_arquivo, "r") as arquivo:
        for linha in arquivo:
            nome, sexo, idade, salario = linha.strip().split(",")
            idade = int(idade)
            salario = int(salario)
            
            # Adiciona os dados às listas de idade e salário
            lista_idade.append(idade)
            lista_salario.append(salario)
            
            # Verifica se a pessoa é mulher e tem salário >= R$ 5000
            if sexo.strip().lower() == "f" and salario >= 5000:
                mulheres_ricas += 1
    
    return lista_idade, lista_salario, mulheres_ricas

# Função de menu
def menu():
    while True:
        print("""
============================================
            PESQUISA HABITACIONAL           
============================================
CÓDIGO  | DESCRIÇÃO
  1     | ADICIONAR PESSOA  
  2     | EXIBIR DADOS E SAIR
=============================================    
        """)
        escolha_opcao = int(input("Digite sua opção: "))
        if escolha_opcao == 1:
            adicionar_pessoa(lista_pessoa)
            calcular_dados_atuais(lista_pessoa)
            escolha_continuar = input("Deseja continuar? (s/n) ").lower()
            if escolha_continuar != "s":
                break
        elif escolha_opcao == 2:
            exibindo_resultados()
            break
        else:
            print("=== Opção inválida ===")

def adicionar_pessoa(lista_pessoa):
    pessoa = Pessoa(
        nome=input("Digite seu nome: "),
        sexo=input("Digite seu gênero: (m/f) ").lower(),
        idade=int(input("Digite sua idade: ")),
        salario=int(input("Digite quanto você ganha: "))
    )
    lista_pessoa.append(pessoa)
    # Atualizar as listas globais imediatamente
    lista_idade.append(pessoa.idade)
    lista_salario.append(pessoa.salario)

def calcular_dados_atuais(lista_pessoa):
    nome_do_arquivo = criar_arquivo()
    with open(nome_do_arquivo, "a") as habitante_regiao:
        for pessoa in lista_pessoa:
            habitante_regiao.write(f"{pessoa.nome}, {pessoa.sexo}, {pessoa.idade}, {pessoa.salario}\n")
    print(f"Dados de {len(lista_pessoa)} pessoas gravados no arquivo.")

# Função para exibir os resultados
def exibindo_resultados():
    # Ler dados do arquivo para calcular as estatísticas
    lista_idade, lista_salario, mulheres_ricas = ler_dados_do_arquivo()
    
    # Calcular média salarial, menor e maior idade
    menor_idade, maior_idade = idade(lista_idade)
    media_salarial = media(lista_salario)
    
    # Exibir os resultados
    print("\n=== RESULTADOS DA PESQUISA ===")
    print(f"Média salarial: R$ {media_salarial:.2f}")
    print(f"Menor idade: {menor_idade}")
    print(f"Maior idade: {maior_idade}")
    print(f"Quantidade de mulheres que ganham acima de R$ 5000: {mulheres_ricas}")

# Listas globais
lista_pessoa = [] 
lista_salario = []
lista_idade = []

# Inicia o menu
menu()
