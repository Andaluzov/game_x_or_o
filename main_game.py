

import gametools as gt


print('ИГра крестики - нолики')

print('condithions')
print('number of cells')

gt.print_matrix([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
print('Start')
matr_a = []
pole_coord = []
#
matr_a = gt.load_new_game()
gt.print_matrix(matr_a)
p=True

while  p:

    gt.step_game('x',matr_a)
    if not gt.game_over(matr_a):
        gt.step_game('y',matr_a)
        p = True
    else:
        print('Game over')
        p=False



