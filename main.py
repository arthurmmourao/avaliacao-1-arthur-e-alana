# =========================
# PARTE FUNCIONAL
# =========================

# Função pura para criar um livro
def criar_livro(id, titulo, autor):
    return {"id": id, "titulo": titulo, "autor": autor}


# Função pura para adicionar livro 
def adicionar_livro(lista_livros, livro):
    return lista_livros + [livro]


# Função pura para listar livros
def listar_livros(lista_livros):
    return lista_livros


# Função pura para atualizar livro
def atualizar_livro(lista_livros, id, novo_titulo, novo_autor):
    return [
        {"id": l["id"],
         "titulo": novo_titulo if l["id"] == id else l["titulo"],
         "autor": novo_autor if l["id"] == id else l["autor"]}
        for l in lista_livros
    ]


# Função pura para deletar livro
def deletar_livro(lista_livros, id):
    return list(filter(lambda l: l["id"] != id, lista_livros))


# Função de ordem superior (recebe função)
def aplicar_operacao(lista, operacao):
    return operacao(lista)


# =========================
# PARTE IMPERATIVA
# =========================

def menu():
    print("\n=== CRUD DE LIVROS ===")
    print("1 - Criar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")


def main():
    livros = []  # estado mutável (imperativo)
    proximo_id = 1

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")

            livro = criar_livro(proximo_id, titulo, autor)
            livros = adicionar_livro(livros, livro)  # nova lista (imutável)

            proximo_id += 1
            print("Livro adicionado!")

        elif opcao == "2":
            lista = aplicar_operacao(livros, listar_livros)

            print("\n--- Lista de Livros ---")
            for l in lista:  # uso de for (imperativo)
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


# Execução
if __name__ == "__main__":
    main()
