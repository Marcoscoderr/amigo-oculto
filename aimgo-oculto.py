import random
from random import shuffle
from time import sleep

#Função principal
def main():

    #Dicionario com o nome e o e-mail dos participantes
    cadastro_participantes = {}

    #Lista com o nome dos participantes que posteriomente será embaralhado
    nome_participantes = []

    #Dicionario com definição final: Chave:Pessoa que dá o presente // Valor: Pessoa que recebe o presente
    sorteados = {}

    #Variável para guardar a escolha de usuário referente a inserção de um novo participante: s-Sim / n-Não
    novo_participante = ""
    
    while True:
        print("-"*10 + " Amigo Oculto " + "-"*10)

        #Menu de acesso
        print("""
            Menu de Acesso:

            1 - Adicionar participante
            2 - Remover participante
            3 - Ver lista de participantes
            4 - Realizar Sorteio!

            5 - Sair  
            """)
        escolha = input("Escolha uma opção: ")

        # Opção 5 - Sai do aplicativo
        if escolha == "5":
            break

        # Opção 1 - Adicona participante
        if escolha == "1":

            #Função para tratar e adicionar participante a lista
            adicionar_participante(cadastro_participantes, nome_participantes)
            #Pressionar tecla para retornar ao menu
            pressione_tecla()
            
        # Opção 2 - Remove participante
        if escolha == "2":
            # Se não houver participantes adicionados
            if len(nome_participantes) == 0:
                print("Você ainda não adicionou participantes!\n")
                pressione_tecla()                
                continue
            else:
                #Chama a função de tratar o nome e verifica se o nome está na lista
                eliminar = remover_participante(cadastro_participantes, nome_participantes)
                pressione_tecla()

                    #TESTE
                print(cadastro_participantes)
                print(nome_participantes)
                
                # else:
                #     print("Esse nome não está na lista!\n")
                #     pressione_tecla()

        # Opção 3 - Ver lista de participantes
        if escolha == "3":
            mostrar_participantes(cadastro_participantes)
            pressione_tecla()

        # Opção 4 - Realizar sorteio
        if escolha == "4":
            realizar_sorteio(cadastro_participantes, nome_participantes, sorteados)
            pressione_tecla()
                

#Misturando a lista
def mistura_lista(lista):
    """Função para embaralhar (misturar) os itens de uma lista

    Args:
        lista : Lista que deve ser embaralhada (misturada)
    """    
    random.shuffle(lista)
    return

#Funcão para adicionar participante
def adicionar_participante(dicionario, lista):
    """Função para tratar o nome e o e-mail que será adicionado a lista

    Returns:
    nome: str Nome do participante
    email : str Email do participante
    """    
    nome = input("\nDigite o nome do participante: ")
    
    #Tratamento do nome
    nome = nome.upper().strip().replace("  ", " ")

    #Tratamento do e-mail - INCOMPLETO
    email = input(f"Digite o e-mail de {nome}: ")
    # if "@" and "." not in email:
    #     print("Digite o e-mail corretamente!")

    #Inserindo participante no dicionário
    #dados[0] -> nome // dados[1] -> email
    dicionario[nome] = email
    #Inserindo nome do participante na lista que será sorteada
    lista.append(nome)

    return print("Participante adicionado!\n")

#Função para remover participante
def remover_participante(diconario, lista):
    """Função para tratar o nome do participante que será removido

    Args:
        dicionario (string): Chave: nome participante / Valor: e-mail participante
        lista (string): Lista com o nome dos participantes

    Returns:
        String: Mensagem de confirmação de exclusão do participante
    """    
    print("\nQual participante você deseja remover? ou 's' para sair.")
    for nome in lista:
        print(nome, end="\n")
    eliminar = input("Digite o nome: ")
                
    #Tratamento nome
    eliminar = eliminar.upper()

    #S para sair e não eliminar ninguem
    if eliminar == "S" :
        return print("\nSolicitação de exclusão cancelada!")
    
    #Caso tenha inserido um nome, verificar se está na lista
    elif eliminar in lista:

        #Apaga o participante no dicionário e na lista
        diconario.pop(eliminar)
        lista.remove(eliminar)
    else:
        return print(f"\nO participante {eliminar} não está na lista!\n")
        
    return print(f"{eliminar} foi retirado da lista!\n")
            
#Funcão para apresentar a lista de participates
def mostrar_participantes(dicionario):
    """Função para apresentar os participantes registrados

    Args:
        dicionario (string): Chave: Nome usuário / Chave: Email do usuário
    """
    
    print("\nLista de Participantes: \n")
    for pessoa in dicionario:
        print(f"Nome: {pessoa} - E-mail: {dicionario[pessoa]}")
    print("\n")
    return

#Função para definição dos participantes
def realizar_sorteio(dicionario, lista, dicionario_sorteados):
    try:
        #Tratamento de erro para que seja inseridos no mínimo 3 participantes
        if len(dicionario) < 3:
            raise ValueError("\nMínimo de 3 participantes!\n")
        else:
            #Realizar sorterio
            mistura_lista(lista)
            print("\n")
            for tempo in range(0,7):
                print("Sorteando" + tempo * ".", end="\r")
                sleep(1)
            print("\n")
            
            print(lista) 
            for nome in dicionario:

                #Conferindo se o participante não tirou ele mesmo
                #Vai ter que ser feito durante o sorteio para não ter o risco de travar no último
                #ou se o ultimo estiver igual recomeçar tudo outra vez

                #Conferindo se os participantes já não sairam juntos anteriormente
                
                #Retira o nome da lista envia para o dicionario de sorteados
                sorteado = lista.pop(0)

                dicionario_sorteados[nome] = sorteado
                print(lista)
            print(dicionario_sorteados)
            
      
    except ValueError as error:
            print(error)
                
#Funcão para enviar email aos participantes
def envio_email():

    return

#Funcão para pressionar qualquer tecla para continuar
def pressione_tecla():
    input("Pressione enter para continuar...")
    return


#Main inicial
if __name__ == "__main__":
    main()