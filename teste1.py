print("Seja Bem-vindo!")
print("Cadastro de Usuário - Sistema Saúde")

while True:
 nome = input("Por favor, Digite seu nome completo:")
 idade = input("Por favor, Digite sua idade:")
 cpf = input("Por favor, Digite seu cpf:")
 contato = input("Por favor, Digite seu telefone:")
 endereco = input("Por favor, Digite seu endereço:")

 print("Dados Cadastrados \n")
 print(f"Nome = {nome}")
 print(f"Idade = {idade}")
 print(f"Cpf = {cpf}")
 print(f"Contato = {contato}")
 print(f"Endereco = {endereco}")

 opcao = input("\nDeseja fazer outro cadastro?(s/n):").lower()
 
 if opcao == "n":
  print("Obrigado, encerrando o sistema. Até logo!")
  break
