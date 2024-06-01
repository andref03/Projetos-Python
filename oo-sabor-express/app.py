from modelos.restaurantes import Restaurante

# Instâncias
restaurante_1 = Restaurante(nome='Pizza Planet', categoria='Italiana') 
restaurante_1.alternar_estado()
restaurante_2 = Restaurante('corbucci Massas', 'Italiana')
restaurante_3 = Restaurante('Tijuana tacos', 'Mexicana')
restaurante_3.alternar_estado()
restaurante_4 = Restaurante('ice cream', 'Sorveteria')

restaurante_1.receber_avaliacao('André', 9.5)
restaurante_1.receber_avaliacao('Gui', 3.5)
restaurante_1.receber_avaliacao('Lais', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
