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

    try:
        #Solicitação que o usuário digite o nome e e-mail de cada participante
        while novo_participante != "n":
            nome = input("Digite o nome do participante: ")
            email = input(f"Digite o e-mail de {nome}: ")

            #Inserindo participante no dicionário
            cadastro_participantes[nome] = email
            #Inserindo nome do participante na lista que será sorteada
            nome_participantes.append(nome)

            #TESTE
            print(cadastro_participantes)
            print(nome_participantes)
            print(len(cadastro_participantes))

            novo = input("Gostaria de inserir mais um participante? s-SIM / n-NÃO: ")

            #Tratamento de erro para que seja inseridos no mínimo 3 participantes
            if len(cadastro_participantes) < 4:
                raise ValueError("Mínimo de 3 participantes!")

            #Voltar a solicitar usuário - INCOMPLETO    

            #Tratamento da escolha - INCOMPLETO
            novo.lower()

            if novo == 'n':
                break
    
    except Exception as error:
        print(error)

    #Misturando a lista
    def mistura_lista():
        
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