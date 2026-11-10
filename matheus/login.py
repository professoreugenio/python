user = 'admin'
senha = 123

tentativas = 2

print('='*40)
print('            Login           ')
print('='*40)

for i in range(3):
  user_digitado = input('User: ')
  senha_digitada = int(input('Senha: '))

  if tentativas == 0:
    print('Acesso Bloqueado!')
    break  
  if user_digitado == user and senha_digitada == senha:
    print('Acesso permitido!')
    break
  print('User ou Senha incorretos, tente novamente')
  print(f'tentativas restantes: {tentativas} ')
  print('='*40)
  tentativas -= 1



