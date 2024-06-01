import os

# Dicionário responsável por armazenar os restaurantes cadastrados

restaurantes = [{'nome':'Pizza Planet', 'categoria':'Italiana', 'ativo': True},
                {'nome':'Japa Sushi\'s', 'categoria':'Japonesa', 'ativo': True},
                {'nome':'El Burguer', 'categoria':'Lanches', 'ativo': False}
                ]

# Funções auxiliares

def exibir_titulo():
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""") 

def exibir_opcoes():
    '''Essa função é responsável por exibir as quatro opções ao usuário'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def cadastrar_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante.

    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona novo restaurante à lista (dicionário) de restaurantes
    
    '''
    exibir_subtitulo('>> Cadastrando restaurante')
    nome_restaurante = input('> Digite o nome do restaurante: ')
    categoria_restaurante = input(f'> Digite a categoria do restaurante \"{nome_restaurante}\": ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'\n>> O restaurante \"{nome_restaurante}\" foi cadastrado com sucesso!!\n')
    retornar_menu()

def listar_restaurantes():
    '''Essa função é responsável por listar todos os restaurantes cadastrados'''
    exibir_subtitulo('>> Listando restaurantes:')
    print(f'{'Nome do Restaurante'.ljust(31)} │ {'Categoria'.ljust(37)} │ {'Status'}')
    print(f'{' '.ljust(31)} │ {' '.ljust(37)} │')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        estado = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'> Nome: {nome.ljust(20)}\t│ Categoria: {categoria.ljust(20)}\t│ Ativo: {estado}')
    print()
    retornar_menu()

def alternar_estado():
    '''Essa função é responsável por alterar o estado do restaurante'''
    exibir_subtitulo('>> Alterando estado do restaurante')
    nome_restaurante = input('> Digite o nome do restaurante para ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # Inverte o estado atual (not é uma inversora)
            mensagem = f'>> O restaurante \"{nome_restaurante}\" foi ativado com sucesso' if restaurante['ativo'] else f'>> O restaurante \"{nome_restaurante}\" foi desativado com sucesso' # Operador ternário
            print(mensagem + '\n')
    if restaurante_encontrado == False:
        print(f'>> O restaurante \"{nome_restaurante}\" não foi encontrado!\n')
    retornar_menu()

def finalizar_app():
    '''Essa função é responsável por sair do programa'''
    exibir_subtitulo('\n\t>> Saindo do programa.')

def escolher_opcao():
    '''Essa função é responsável por satisfazer a opção escolhida pelo usuário'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print()
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado()
            case 4:
                finalizar_app()
            case _:
                opt_invalida()
    except:
        print()
        opt_invalida()
    print()

# Funções para melhorar legibilidade

def opt_invalida():
    '''Essa função é responsável por mostrar a mensagem de opção escolhida erroneamente'''
    print('>> Opção inválida!\n')
    retornar_menu()

def retornar_menu():
    '''Essa função é responsável por retornar ao menu principal'''
    input('>>> Pressione Enter para retornar ao menu principal...')
    main()

def exibir_subtitulo(subtitulo):
    '''Essa função é responsável por exibir o subtítulo da opção escolhida'''
    os.system('cls')
    print(subtitulo + '\n')

# Função main()

def main():
    '''Essa função é responsável por organizar o código na ordem correta de excução (menu principal)'''
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
