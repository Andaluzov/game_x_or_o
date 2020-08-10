

import gametools as gt


print('ИГра матриц')
print('Start')
print('condithions')

pole=[]
matr_a = [[' ', ' ',' ' ],[' ', ' ',' '],[' ', ' ',' ']]
#rez_matr = mt.add(matr_a, matr_b)
gt.print_matrix(matr_a)
while not gt.game_over(matr_a):
    print('Player X')
    print('Enter your move:')
    pole_row=int(input('row='))
    pole_col = int(input('col='))
   #проверка поля
    matr_a[pole_row][pole_col] = 'x'
    gt.print_matrix(matr_a)
