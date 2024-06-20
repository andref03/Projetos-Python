from modelos.cardapio.item_cardapio import ItemCardapio

class BebidaCardapio:
    def __init__(self, nome_bebida, preco_bebida, descricao_bebida):
        # chama o construtor da classe ItemCardapio
        super().__init__(nome_bebida, preco_bebida)
        # a descrição é própria de BebidaCardapio, não estando no ItemCardapio
        self._descricao = descricao_bebida