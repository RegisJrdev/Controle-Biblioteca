from dados import usuarios, id

#Uncao para ccadastrar usuarios
def cadastrar_usuario(nome, email):
    global id
    usuario = { 'id': id, 'nome': nome, 'email': email}
    usuarios.append(usuario)

    id += 1

#Funcao para mostrar usuarios
def listar_usuarios():
    if not usuarios:
        print('\n===== Nao possuem usuarios cadastrados =====\n')
        return
    
    for usuario in usuarios:
        print(usuario)    

def buscar_usuario_por_id():
    u = input('Digite o id do usuario que deseja buscar')

    for usuario in usuarios:
        if usuario['id'] == u:
            return usuario

def atualizar_email(novoEmail):
    pass    
