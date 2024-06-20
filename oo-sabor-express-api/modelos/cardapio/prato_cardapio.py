from modelos.cardapio.item_cardapio import ItemCardapio

class PratoCardapio(ItemCardapio):
    def __init__(self, nome_prato, preco_prato, descricao_prato):
        # chama o construtor da classe ItemCardapio
        super().__init__(nome_prato, preco_prato)
        # a descrição é própria de PratoCardapio, não estando no ItemCardapio
        self._descricao = descricao_prato