from dados import livros, id

def cadastrar_livro():
    global id

    titulo = input('Titulo do livro: ')
    autor =  input('Autor do livro: ')
    disponivel = True
    livro = {'id': id, 'titulo': titulo, 'autor': autor, 'disponivel': True}

    id += 1

    livros.append(livro)

    print('O livro ' + titulo + ' foi cadstrado com sucesso')

def listarLivros():
    if not livros:
        print('\n===== Nao possuem livros cadastrados =====\n')
    else:
        print(livros)    