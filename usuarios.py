from dados import usuarios, id

def cadastrar_usuario():
    nomeUsuario = input(' Nome do Usuario: ')
    emailUsuario = input('Email do usuario')

    usuarios = { 'id': id, 'nomeUsuario': nomeUsuario, 'emailUsuario': emailUsuario}



def listar_usuarios():
    if not usuarios:
        print('\n===== Nao possuem usuarios cadastrados =====\n')
    else:
        print(usuarios)    

