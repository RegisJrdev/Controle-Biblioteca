from dados import livros, id, emprestimos, usuarios

def cadastrar_livro(titulo, autor):
    global id

    livro = {'id': id, 'titulo': titulo, 'autor': autor, 'disponivel': True}

    id += 1

    livros.append(livro)

    print('O livro ' + titulo + ' foi cadstrado com sucesso')

def listarLivros():
    if not livros:
        print('\n===== Nao possuem livros cadastrados =====\n')

    for livro in livros:
        print(livro)   

def buscar_livro_por_titulo(titulo):
    titulo = titulo.lower()
    encontrados = []

    for livro in livros:
        if titulo in livro['titulo'].lower():
            encontrados.append(livro)

    if not encontrados:
        print('Nao foram encontrados nenhum livro com esse titulo')
        return

    print('Livros Encontrados')
    for livro in encontrados:
        print(livro)



  