from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    # Criando lista
    restaurantes = []

    # Semelhante ao construtor
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        ## Colocando a instância na lista restaurantes[]
        Restaurante.restaurantes.append(self)

    # Semelhante ao getter/setter
    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'inativo'
    
    # Semelhante ao toString()
    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}, Estado: {self.ativo}'
    
    # Método próprio
    @classmethod
    def listar_restaurantes(cls):
        ''' Esta função é responsável por listar todos os itens da lista restaurantes[] '''

        print('\n>> Listando todos os restaurantes:\n')
        print(f'{'Nome do Restaurante'.ljust(22)} │ {'Categoria'.ljust(20)} │ {'Avaliação'.ljust(20)} │ {'Status'}')
        print(f'{''.ljust(22)} │ {''.ljust(20)} │ {''.ljust(20)} │')

        for rest in cls.restaurantes:
            print(f'> {rest.nome.ljust(20)} │ {rest.categoria.ljust(20)} │ {rest.media_avaliacoes}{''.ljust(17)} │ {rest.ativo}')
        print()
    
    # Método de instância
    def alternar_estado(self):
        self._ativo = not self._ativo

    # Método de instância
    def receber_avaliacao(self, cliente='', nota=0):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        ## Caso não haja avaliação nenhuma
        if not self._avaliacao: 
            return 0
        
        soma = sum(av._nota for av in self._avaliacao)
        qtdd_notas = len(self._avaliacao)
        ## Arredonda a média com 1 casa decimal
        media = round((soma / qtdd_notas), 1)

        return media
    
    def adc_item_ao_cardapio(self, item):
        # se verdadeiro, o item foi instanciado pela Classe Mãe chamada ItemCardapio
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante {self._nome}\n')
        
        for i, item in enumerate(self._cardapio, start=1):
            # hasattr = "se tiver o atributo"
            if hasattr(item, 'descricao_prato'):
                print(f'({i}). Nome: {item._nome}\nPreço: R$ {item._preco}\nDescrição: {item._descricao_prato}\n')
            if hasattr(item, 'descricao_bebida'):
                print(f'({i}). Nome: {item._nome}\nPreço: R$ {item._preco}\nDescrição: {item._descricao_bebida}\n')

            
