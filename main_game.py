

import gametools as gt


print('ИГра крестики - нолики')

print('condithions')
print('number of cells')

gt.print_matrix([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
print('Start')
matr_a = []
pole_coord = []
# new game
matr_a = gt.load_new_game()
gt.print_matrix(matr_a)

gamer = 'y'
while not  gt.game_over(gamer, matr_a):
    if gamer == 'x':
        gamer = 'y'
    else:
        gamer = 'x'
    gt.step_game(gamer, matr_a)





