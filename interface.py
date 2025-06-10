from livros import cadastrar_livro, listarLivros, buscar_livro_por_titulo
from usuarios import cadastrar_usuario, listar_usuarios
from emprestimos import emprestar_livro, listar_emprestimos, devolver_livro, visualizar_historico_emprestimo_usuario

while True:
    print('\n---------- Menu Biblioteca ----------\n')
    print('1 - Adicionar novo livro') 
    print('2 - Listar Livros') 
    print('3 - Buscar livro por título') 
    print('4 - Adicionar novo usuário') 
    print('5 - Listar todos os usuários') 
    print('6 - Realizar um empréstimo')
    print('7 - Devolver um livro') 
    print('8 - Listar Emprestimos') 
    print('9 - Visualizar historico de Emprestimos') 
    print('0 - Sair do sistema')


    opcao = int(input('Digite a opcao que deseja: '))

    if opcao == 1:
        titulo = input('Titulo do livro: ')
        autor =  input('Autor do livro: ')
        cadastrar_livro(titulo, autor)

    elif opcao == 2:
        listarLivros()  

    elif opcao == 3:
        titulo = input('Digite o titulo do livro que deseja')        
        buscar_livro_por_titulo(titulo)

    elif opcao == 4:
        nome = input(' Nome do Usuario: ')
        email = input('Email do usuario')
        cadastrar_usuario(nome, email)

    elif opcao == 5:
        listar_usuarios()

    elif opcao == 6:
        id_livro = int(input('Digite o id do livro'))
        id_usuario = int(input('Digite o id do usuario'))
        emprestar_livro(id_livro, id_usuario)

    elif opcao == 7:
        id_livro = int(input('digite o id do livro que deseja devolver'))
        devolver_livro(id_livro)

    elif opcao == 8:
        listar_emprestimos()

    elif opcao == 9:
        id_usuario = int(input('Digite o id do usuario que deseja ver o historico'))
        visualizar_historico_emprestimo_usuario(id_usuario)

    elif opcao == 0:
        break

    else:
        print('\nDigite uma opcao valida')
