## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234@1, umF1#, 2w3E*, 2We3345
# Então, a saída do programa deve ser:
# ABd1234@1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

'''Prof. Icaro, me desculpe pelo uso de funçoes, sei que sai do escopo dos assuntos atuais, porem acabei utilizando,
por conta de organizacao e ficar mais pratica a correcao de erros.'''

'''A seguinte funcao esta responsavel pela separacao das senhas, ela ira remover os espacos e ira verificar, a partir 
das virgulas, o inicio e o fim de uma senha, alem de levar em consideracao o fim da string.'''
def separador(text):
    text = text.replace(" ", "")
    end = 0
    start = 0

    while start < len(text):
        senhaTemp = ""
        while end < len(text)+1:
            if (text[end] is "," or end == len(text)-1):
                senhaTemp = senhaTemp.replace(",", "")
                senhaTemp = text[start:end]
                passChecker(senhaTemp)
                start = end
                end += 1
            end += 1
        start += 1

"""O passChecker e responsavel pela verificacao, ela e chamada pelo separador, pois, como nao e utilizada uma lista,
as verificacoes ocorrem a partir da criacao de cada "senha temporaria" a partir do string texto. """
def passChecker(password):
    password = password.replace(",","")
    note = ""
    result = False
    if(len(password)<6):
        note = ("Password muito curto!")
    elif(len(password)>12):
        note = ("Password muito longo!")
    else:
        if(password.isdigit()):
            note = ("Password sem letras")
        elif(password.isalpha()):
            note = ("Password sem numeros")
        else:
            if(password.isupper()):
                note = ("Password sem minusculos")
            elif(password.islower()):
                note = ("Password sem maiusculos")
            else:
                if"#" in password or "@" in password or "$" in password :
                    print("Password perfeito:\n")
                    result = True

                else:
                    note = ("Password sem caracteres especiais")
    if(result == True):
        print(password)

    '''else:
        print (password)
        print(note)'''


x = input()
print(separador(x))


def main():
    x = input("Digite um texto ou uma senha:\n")
    print(separador(x))


if __name__ == '__main__':
    main()
