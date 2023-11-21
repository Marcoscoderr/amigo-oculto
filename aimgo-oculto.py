import random

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


    #Solicitação que o usuário digite o nome e e-mail de cada participante
    #DEVE SER UMA FUNCAO????
    while novo_participante != "n":
        try:
            nome = input("Digite o nome do participante: ")

            #Tratamento do nome

            email = input(f"Digite o e-mail de {nome}: ")

            #Tratamento do e-mail

            #Inserindo participante no dicionário
            cadastro_participantes[nome] = email
            #Inserindo nome do participante na lista que será sorteada
            nome_participantes.append(nome)

            #TESTE
            print(cadastro_participantes)
            print(nome_participantes)
            print(len(cadastro_participantes))

            novo = input("Gostaria de inserir mais um participante? s-SIM / n-NÃO: ")
            
            #Tratamento da escolha - INCOMPLETO
            novo.lower()

            #Conferir se o usuário digitou somente os caracteres permitidos: "s" ou "n"
            if novo != "s" and novo != "n":
                raise ValueError("Digite somente 's' para SIM ou 'n' para NÃO!")
            #CORRIGIR O ERRO QUE FAZ O COMANDO VOLTAR A PEDIR O USUARIO OUTRO PARTICIPANTE
            #ELE PODE NÃO QUERER INSERIR MAIS PARTICIPANTES, MAS DIGITOU INCORRETAMENTE

            #Tratamento de erro para que seja inseridos no mínimo 3 participantes
            if novo =="n" and len(cadastro_participantes) < 3:
                raise ValueError("Mínimo de 3 participantes!")

        except ValueError as error:
            print(error)
            continue
            
        
        #Saída do loop caso a escolha seja "n"
        if novo == 'n':
            break
    
    #TESTE DE MISTURA DA LISTA CHAMANDO A FUNÇÂO MISTURA_LISTA()
    print(f"Original: {nome_participantes}")
    mistura_lista(nome_participantes)
    print(f"Teste mistura 1: {nome_participantes}")
    mistura_lista(nome_participantes)
    print(f"Teste mistura 2: {nome_participantes}")
    mistura_lista(nome_participantes)
    print(f"Teste mistura 3: {nome_participantes}")
        

#Misturando a lista
def mistura_lista(lista):
    """Função para embaralhar (misturar) os itens de uma lista

    Args:
        lista : Lista que deve ser embaralhada (misturada)
    """    
    random.shuffle(lista)
    return

#Definição dos participantes


#Conferindo se o participante não tirou ele mesmo


#Conferindo se os participantes já não sairam juntos anteriormente


#Enviado via e-mail para os participantes informando quem eles devem presentear
def envio_email():

    return


#Main inicial
if __name__ == "__main__":
    main()