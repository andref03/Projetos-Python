from modelos.cardapio.item_cardapio import ItemCardapio

class BebidaCardapio(ItemCardapio):
    def __init__(self, nome_bebida, preco_bebida, descricao_bebida):
        # chama o construtor da classe ItemCardapio
        super().__init__(nome_bebida, preco_bebida)
        # a descrição é própria de BebidaCardapio, não estando no ItemCardapio
        self._descricao_bebida = descricao_bebida

    @property
    def descricao_bebida(self):
        return self._descricao_bebida

    def __str__(self):
        return f'Bebida: {self.nome}\nPreço: R$ {self.preco}\nDescrição: {self.descricao_bebida}\n'

    def aplicar_desconto(self):
        # aplica desconto de 5% na bebida, se aplicar o desconto
        self._preco -= (self._preco * 0.05)