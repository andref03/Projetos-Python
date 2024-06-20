from modelos.restaurantes import Restaurante
from modelos.cardapio.prato_cardapio import PratoCardapio
from modelos.cardapio.bebida_cardapio import BebidaCardapio

# Instâncias
restaurante_1 = Restaurante(nome='Pizza Planet', categoria='Italiana') 

# Criando avaliações
restaurante_1.receber_avaliacao('André', 9.5)
restaurante_1.receber_avaliacao('Gui', 7.5)
restaurante_1.receber_avaliacao('Lais', 8.75)

# Adicionando itens ao cardápio
prato_001 = PratoCardapio('Peixe empanado', 30.00, 'O melhor peixe empanado da cidade!')
bebida_001 = BebidaCardapio('Água c/ gás', 3.50, 'Água gaseificada, de 500 ml')

# Vinculando itens a algum restaurante
restaurante_1.adc_item_ao_cardapio(prato_001)
restaurante_1.adc_item_ao_cardapio(bebida_001)

# Aplicando desconto
prato_001.aplicar_desconto()
bebida_001.aplicar_desconto()

# Função main()
def main():
    restaurante_1.exibir_cardapio

if __name__ == '__main__':
    main()
