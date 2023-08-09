# Salvar ok, próximo passo, salvar "login" (nome e senha)
#  Case 1 v
# Preferencialmente salvar e abrir o nome e a senha no mesmo arquivo
# Mas caso dê problema com caractere, ou fazer com quebra de linha

#  Case 2 v
# Criar um arquivo para senhas e outro para nomes, mas isso pode gerar
# Disparidade entre os dados, por exemplo caso um nome venha a ser apagado
# e uma senha não, todos os nomes receberão a senha de outro usuário

import os
import json
#Como será usado uma "lista de objetos", que atribui um valor a uma chave
#Será utilizado um JSON para armazenar os usuários, em forma de dicionário
#Onde, mais ou menos, {["user":"password"],"[user2":"password2"]}

def load_list(filenam):
    if os.path.exists(filenam):
        with open(filenam, "r") as dbfilenames:
            try:
                return json.load(dbfilenames)
            except json.JSONDecodeError:
                return {}
    return {}

def save_list(filenam, usrsdt):
    with open(filenam, "w") as dbfilenames:
        json.dump(usrsdt, dbfilenames, indent=4)

targetFileName = "loginData.json"
savedUsers = load_list(targetFileName)

name = input("Insira um nome para salvar: ")
passwd = input("Insira agora a senha desse usuário: ")

savedUsers[name] = passwd
#Em um arquivo JSON, Chave (Nome/User) : Valor (Senha)
save_list(targetFileName,savedUsers)

print("Login salvo com sucesso!")