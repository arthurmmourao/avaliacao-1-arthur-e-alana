# PARTE FUNCIONAL

def criar_livro(id, titulo, autor):
    return {"id": id, "titulo": titulo, "autor": autor}


def adicionar_livro(lista_livros, livro):
    return lista_livros + [livro]


def listar_livros(lista_livros):
    return lista_livros


def atualizar_livro(lista_livros, id, novo_titulo, novo_autor):
    return [
        {"id": l["id"],
         "titulo": novo_titulo if l["id"] == id else l["titulo"],
         "autor": novo_autor if l["id"] == id else l["autor"]}
        for l in lista_livros
    ]


def deletar_livro(lista_livros, id):
    return list(filter(lambda l: l["id"] != id, lista_livros))


def aplicar_operacao(lista, operacao):
    return operacao(lista)

# PARTE IMPERATIVA

def menu():
    print("\n=== CRUD DE LIVROS ===")
    print("1 - Criar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")


def main():
    livros = []
    proximo_id = 1

    livro1 = criar_livro(proximo_id, "Dom Casmurro", "Machado de Assis")
    livros = adicionar_livro(livros, livro1)
    proximo_id += 1

    livro2 = criar_livro(proximo_id, "1984", "George Orwell")
    livros = adicionar_livro(livros, livro2)
    proximo_id += 1

    livro3 = criar_livro(proximo_id, "O Pequeno Príncipe", "Antoine de Saint-Exupéry")
    livros = adicionar_livro(livros, livro3)
    proximo_id += 1

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")

            livro = criar_livro(proximo_id, titulo, autor)
            livros = adicionar_livro(livros, livro)  

            proximo_id += 1
            print("Livro adicionado!")

        elif opcao == "2":
            lista = aplicar_operacao(livros, listar_livros)

            print("\n--- Lista de Livros ---")
            for l in lista: 
                print(f'ID: {l["id"]} | {l["titulo"]} - {l["autor"]}')

        elif opcao == "3":
            id = int(input("ID do livro: "))
            novo_titulo = input("Novo título: ")
            novo_autor = input("Novo autor: ")

            livros = atualizar_livro(livros, id, novo_titulo, novo_autor)
            print("Livro atualizado!")

        elif opcao == "4":
            id = int(input("ID do livro: "))
            livros = deletar_livro(livros, id)
            print("Livro removido!")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
