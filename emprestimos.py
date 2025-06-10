from dados import livros, usuarios, emprestimos

def emprestar_livro(id_livro, id_usuario):
    livroEmprestimo = None

    print("Livros:", livros)
    print("ID informado:", id_livro)

    for livro in livros:
        if livro['id'] == id_livro:
            livroEmprestimo = livro
            break

    if livroEmprestimo is None:
        print('O livro nao foi encontrado')
        return

    usuario = None

    for u in usuarios:
        if u['id'] == id_usuario:
            usuario = u
            break

    if usuario is None:
        print('O usuario nao foi encontrado')
        return
    
    if not livroEmprestimo['disponivel']:
        print('O livro ja foi emprestadpo')
        return

    livroEmprestimo['disponivel'] = False
    emprestimos.append({'id_livro': id_livro, 'id_usuario': id_usuario})    

def listar_emprestimos():
    if not emprestimos:
        print('Nao existem emprestimos ativos')   

    for emprestimo in emprestimos:
        print(emprestimo)

def devolver_livro(id_livro): 

    livroDevolvido = None 

    for livro in livros:
        if livro['id'] == id_livro:
            livroDevolvido = livro 
            break
    
    if livroDevolvido is None:
        print('Livro nao encontrado.')
        return
    
    if livroDevolvido['disponivel'] == True:
        print('este livro ja esta disponivel ou ja foi devolvido')


    emprestimo = None

    for e in emprestimos:
        if e['id_livro'] == id_livro:
            emprestimo = e
            break

    if emprestimo is None:
        print('nenhum esprestimo registrado para este livro')    
        return

    livroDevolvido['disponivel'] = True
    emprestimos.remove(emprestimo)
    print('O livro foi devolvido ')

def visualizar_historico_emprestimo_usuario(id_usuario):
    encontrou = False
    for emprestimo in emprestimos:
        if emprestimo['id_usuario'] == id_usuario:
            for livro in livros:
                if livro['id'] == emprestimo['id_livro']:
                    print(livro)
                    encontrou = True

    if not encontrou:
        print('usuario nao possui emprestimo')