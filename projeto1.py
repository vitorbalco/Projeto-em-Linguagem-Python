def boas_vindas(nome):
    return nome

#Dava pra apenas usar o print mas vamos aproveitar e aprender função.
Bomdia = boas_vindas('Boas-vindas à livraria, de Vitor Cardoso Balco!')
print(Bomdia)


#Nosso dicionario de livros,autores,IDs e editoras/ID global que vai funcionar como armazenamento dos diversos IDs de livros
lista_livro = []
id_global = 0

#Cadastro dos livros
def cadastrar_livro(id):
    print(f'\nCadastrando o livro ID: {id}')

    nome = input('Qual o nome do livro:')
    autor = input('Quem é o autor deste livro:')
    editora = input('Qual a editora deste livro:')
    livro = {
        'id': id,
        'nome': nome,            #Dicionário
        'autor': autor,
        'editora': editora
    }     #Foi utilizado o .append para adicionar o livro que vai ser cadastrado no Dicionário(lista vazia).

    lista_livro.append(livro)
    print('\nLivro cadastrado com sucesso!')

#Função que vai consultar o livro
def consultar_livro():
    while True:
        print('| ------------Menu Consultar------------ |')
        print('          1. Consultar Todos')
        print('          2. Consultar por Id')
        print('          3. Consultar por Autor')
        print('          4. Retornar ao Menu.')

        op2 = input('Consultando livro através de qual circunstância: (Todos/Id/Autor/Menu):')


        if op2 == '1':
            print('\nAqui está todos os livros cadastrados:')
            for livro in lista_livro:
                print(livro)

                                        #Consulta por todos os Dados Cadastrados,ID,Nomes,Autores.
        elif op2 == '2':
            buscar_id = int(input('Qual o ID do seu livro:'))
            encontrado = False
            for livro in lista_livro:
                if livro['id'] == buscar_id:
                    print(livro)
                    encontrado = True
            if not encontrado:
                print('Com este Id nenhum livro foi encontrado.')


        elif op2 == '3':
            autor_livro = input('Qual o autor do seu livro:')
            encontrar_autor = [livro for livro in lista_livro if livro['autor'].lower() == autor_livro.lower()]
            if encontrar_autor:
                print('\nAqui estão os livros de acordo com o autor que você pediu:')
                for livro in encontrar_autor:
                    print(livro)
            else:
                print('Não foi encontrado livros deste autor.')


        elif op2 == '4':
            break
        else:
            print('Opção errada. Tente novamente.')


#Função para remover o livro
def remover_livro():
    if lista_livro:
        try:
            remover_pelo_id = int(input('Informe o ID do livro a ser removido:'))
            livro_removido = False


            for livro in lista_livro:
                if livro['id'] == remover_pelo_id:
                   lista_livro.remove(livro)
                   print(f'O livro com o ID {remover_pelo_id} foi removido com sucesso!')
                   livro_removido = True
                   break


            if not livro_removido:
                   print(f'\nNenhum livro pode ser removido com o ID {remover_pelo_id}. ')
        except ValueError:
            print('\nID inválido. Informe um número existente.')


    else:
        print('Nenhum livro para remover.')


#Programa principal
while True:
      print('| ------------Menu Principal------------ |')
      print('| 1- Cadastrar Livro                     |')          
      print('|', '-' * 38, '|')
      print('| 2- Consultar Livro                     |')

      print('|          1. Consultar Todos.           |')
      print('|          2. Consultar por Id.          |')  # MENU
      print('|          3. Consultar por Autor.       |')
      print('|          4. Retornar ao Menu.          |')
      print('|', '-' * 38, '|')
      print('| 3- Remover livro                       |')
      print('|', '-' * 38, '|')
      print('| 4- Encerrar Programa..                 |')
      print('|', '-' * 38, '|')

      op3 = input('Qual a opção que você deseja:')
      if op3 == '1':
        id_global += 1
        cadastrar_livro(id_global)


      elif op3 == '2':
        consultar_livro()

                                 #Operações que vão colocar as funções em funcionamento.
      elif op3 == '3':
        remover_livro()


      elif op3 == '4':
        print('Encerrando o programa....')
        break


      else:
        print('Opção inválida. Tente novamente.')


print(lista_livro)