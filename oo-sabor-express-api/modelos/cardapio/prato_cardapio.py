from modelos.cardapio.item_cardapio import ItemCardapio

class PratoCardapio(ItemCardapio):
    def __init__(self, nome_prato, preco_prato, descricao_prato):
        # chama o construtor da classe ItemCardapio
        super().__init__(nome_prato, preco_prato)
        # a descrição é própria de PratoCardapio, não estando no ItemCardapio
        self._descricao_prato = descricao_prato

    @property
    def descricao_prato(self):
        return self._descricao_prato

    def __str__(self):
        return f'Prato: {self.nome}\nPreço: R$ {self.preco}\nDescrição: {self.descricao_prato}\n'
    
    def aplicar_desconto(self):
        # aplica desconto de 8% no prato, se aplicar o desconto
        self._preco -= (self._preco * 0.08)