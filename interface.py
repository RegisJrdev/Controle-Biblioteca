from livros import cadastrar_livro, listarLivros
from usuarios import cadastrar_usuario, listar_usuarios

while True:
    print('---------- Menu Biblioteca ----------\n')
    print('1 - Cadastrar Livro') 
    print('2 - Listar Livros') 
    print('3 - Registrar Novo Usuario') 
    print('4 - Realizar Emprestimo') 
    print('5 - Devolver Livro') 
    print('6 - Fechar Sistema\n') 

    opcao = input('Digite a opcao que deseja: ')

    if opcao == '1':
        cadastrar_livro()
    elif opcao == '2':
        listarLivros()  
    elif opcao == '3':
        cadastrar_usuario()
    elif opcao == '4':
        listar_usuarios()



