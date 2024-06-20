from modelos.restaurantes import Restaurante
from modelos.cardapio.prato_cardapio import PratoCardapio
from modelos.cardapio.bebida_cardapio import BebidaCardapio

# Instâncias
restaurante_1 = Restaurante(nome='Pizza Planet', categoria='Italiana') 
restaurante_2 = Restaurante('corbucci Massas', 'Italiana')
restaurante_3 = Restaurante('Tijuana tacos', 'Mexicana')
restaurante_4 = Restaurante('ice cream', 'Sorveteria')

# Alternando estados
restaurante_1.alternar_estado()
restaurante_3.alternar_estado()

# Criando avaliações
restaurante_1.receber_avaliacao('André', 9.5)
restaurante_1.receber_avaliacao('Gui', 7.5)
restaurante_1.receber_avaliacao('Lais', 8.75)
restaurante_2.receber_avaliacao('João', 6)
restaurante_2.receber_avaliacao('Mirtes', 7.5)
restaurante_3.receber_avaliacao('Jô', 9)
restaurante_3.receber_avaliacao('João', 5.5)
restaurante_4.receber_avaliacao('Leia', 8.5)

# Adicionando itens ao cardápio
prato_001 = PratoCardapio('Peixe empanado', 30.00, 'O melhor peixe empanado da cidade!')
bebida_001 = BebidaCardapio('Água c/ gás', 3.50, 'Água gaseificada, de 500 ml')

# Função main()
def main():
    # Restaurante.listar_restaurantes()
    print(prato_001)
    print(bebida_001)

if __name__ == '__main__':
    main()
