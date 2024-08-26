nome = input("Digite aqui seu nome:")
email = input("Digite aqui seu e-mail:")

# descubra o servidor do email 
posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

# pegar o 1º nome do usuário
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

# construa uma mensagem: Usuario primeiro_nome cadastrado com sucesso com o email tal
mensagem = f"Usuario {primeiro_nome} cadastrado com sucesso com o email: {email}"
print(mensagem)

# construa uma mensagem: Enviamos um link de confirmação para o email j***@gmail.com
primeira_letra = email[0]
print(primeira_letra)
mensagem2 = f"Enviamos um link de confirmação para o email {primeira_letra}***{servidor}"
print(mensagem2)