from modelos.restaurantes import Restaurante

# Instâncias
restaurante_1 = Restaurante(nome='Pizza Planet', categoria='Italiana') 
restaurante_1.alternar_estado()
restaurante_2 = Restaurante('corbucci Massas', 'Italiana')
restaurante_3 = Restaurante('Tijuana tacos', 'Mexicana')
restaurante_3.alternar_estado()
restaurante_4 = Restaurante('ice cream', 'Sorveteria')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
