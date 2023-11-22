import random
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

    #Menu com opções??? (Inserir participante, excluir participante, sortear, sair...)
    
    while True:
        print("-"*10 + " Amigo Oculto " + "-"*10)
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
            dados = adicionar_participante()
            #Inserindo participante no dicionário
            #dados[0] -> nome // dados[1] -> email
            cadastro_participantes[dados[0]] = dados[1]
            #Inserindo nome do participante na lista que será sorteada
            nome_participantes.append(dados[0])
            
            #TESTE
            # print(cadastro_participantes)
            # print(nome_participantes)
            # print(len(cadastro_participantes))

        # Opção 2 - Remove participante
        if escolha == "2":
            if len(nome_participantes) == 0:
                #Pausa de 2 segundos para o usuário ler a mensgem
                print("Você ainda não adicionou participantes!")
                sleep(2)
                continue
            else:
                #Chama a função de tratar o nome e verifica se o nome está na lista
                eliminar = remover_participante(nome_participantes)
                if eliminar in nome_participantes:
                    cadastro_participantes.pop(eliminar)
                    nome_participantes.remove(eliminar)
                    print(f"{eliminar} foi retirado da lista!")
                    #Pausa de 2 segundos para o usuário ler a mensgem
                    sleep(2)

                    #TESTE
                    print(cadastro_participantes)
                    print(nome_participantes)
                    
                else:
                    print("Esse nome não está na lista!")
                    #Pausa de 2 segundos para o usuário ler a mensgem
                    sleep(2)

        # Opção 3 - Ver lista de participantes
        if escolha == "3":
            print("Lista de Participantes")
            for pessoa in cadastro_participantes:
                print(f"Nome: {pessoa} - E-mail: {cadastro_participantes[pessoa]}")
                #Pausa para leitura do usuário
                sleep(5)


        # Opção 4 - Realizar sorteio
        if escolha == "4":
            try:
                #Tratamento de erro para que seja inseridos no mínimo 3 participantes
                if len(cadastro_participantes) < 3:
                    raise ValueError("Mínimo de 3 participantes!")
                else:
                    #Realizar sorterio
                    print("Realizar sorteio")
            except ValueError as error:
                print(error)
                sleep(2)
           

#Misturando a lista
def mistura_lista(lista):
    """Função para embaralhar (misturar) os itens de uma lista

    Args:
        lista : Lista que deve ser embaralhada (misturada)
    """    
    random.shuffle(lista)
    return

#Solicitação que o usuário digite o nome e e-mail de cada participante
def adicionar_participante():
    """Função para tratar o nome e o e-mail que será adicionado a lista

    Returns:
        nome: str Nome do participante
        email : str Email do participante
    """    
    nome = input("Digite o nome do participante: ")
    #Tratamento do nome

    email = input(f"Digite o e-mail de {nome}: ")

    #Tratamento do e-mail

    return nome, email

#Função para remover participante
def remover_participante(lista):
    """Função para tratar o nome do participante que será removido

    Args:
        lista (string): Lista com o nome dos participantes

    Returns:
        String: Participante a ser removido
    """    
    print("Qual participante você deseja remover? ")
    for nome in lista:
        print(nome, end="\n")
    eliminar = input("Digite o nome: ")
                
    #Tratamento nome

    return eliminar
            

#Definição dos participantes


#Conferindo se o participante não tirou ele mesmo


#Conferindo se os participantes já não sairam juntos anteriormente


#Enviado via e-mail para os participantes informando quem eles devem presentear
def envio_email():

    return


#Main inicial
if __name__ == "__main__":
    main()