import os

def load_list(filenam):
    if os.path.exists(filenam):
        with open(filenam, "r") as dbfilenames:
        #Abrir o arquivo, o "with" garante que é fechado/salvo no final do bloco
            lines = dbfilenames.readlines()
            #Passa as linhas do arquivo de texto para array de strings
            return [line.strip() for line in lines]
            #Tira a quebra de linha para cada linha/nome no arquivo/array
    return []

def save_list(filenam, savedfil):
    with open(filenam, "w") as dbfilenames:
        for name in savedfil:
        #Para cada nome no arquivo
            dbfilenames.write(name+'\n')
            #Salva o nome no arquivo com uma quebra de linha

targetFileName = "savedNames.txt"
savedNames = load_list(targetFileName)

name = input("Insira um nome para salvar: ")

savedNames.append(name)
save_list(targetFileName, savedNames)
print("Lista atual: ", savedNames)

# Salvar ok, próximo passo, salvar "login" (nome e senha)
#  Case 1 v
# Preferencialmente salvar e abrir o nome e a senha no mesmo arquivo
# Mas caso dê problema com caractere, ou fazer com quebra de linha

#  Case 2 v
# Criar um arquivo para senhas e outro para nomes, mas isso pode gerar
# Disparidade entre os dados, por exemplo caso um nome venha a ser apagado
# e uma senha não, todos os nomes receberão a senha de outro usuário

