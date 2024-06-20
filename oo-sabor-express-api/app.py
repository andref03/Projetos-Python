from modelos.restaurantes import Restaurante

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

# Função main()
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
