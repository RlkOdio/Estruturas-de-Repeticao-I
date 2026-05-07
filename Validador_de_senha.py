def validar_senha(senha):
    
    # Critérios iniciais
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    caracteres_especiais = "!@#$%^&*(),.?\":{}|<>"

    # 1. Verificação de comprimento mínimo
    erros = []
    if len(senha) < 8: # Verifica se a senha tem pelo menos 8 caracteres
        erros.append("Pelo menos 8 caracteres")

    # 2. Percorrendo a string caractere por caractere
    for char in senha: 

        if char.isupper():        # Utilizado para verificar se é uma letra maiúscula
            tem_maiuscula = True

        elif char.islower():      # Utilizado para verificar se é uma letra minúscula
            tem_minuscula = True

        elif char.isdigit():      # Utilizado para verificar se é um número
            tem_numero = True

        elif char in caracteres_especiais:  # Utilizado para verificar se é um caractere especial
            tem_especial = True

    # Adicionando erros à lista se os critérios não forem atendidos

    if not tem_maiuscula:       # Utilizado para verificar se a senha tem uma letra maiúscula
        erros.append("Uma letra maiúscula")

    if not tem_minuscula:       # Utilizado para verificar se a senha tem uma letra minúscula
        erros.append("Uma letra minúscula")

    if not tem_numero:          # Utilizado para verificar se a senha tem um número
        erros.append("Um número")

    if not tem_especial:        # Utilizado para verificar se a senha tem um caractere especial
        erros.append("Um caractere especial")

    # Resultado
    if not erros:
        return "Senha forte"
    else:
        return "Requisitos ausentes: " + ", ".join(erros) # O método join() é usado para concatenar os elementos da lista 'erros' em uma única string, onde cada elemento é separado por ", ".

# Teste do código
senha_usuario = input("Digite sua senha: ")
resultado = validar_senha(senha_usuario)
print(resultado)