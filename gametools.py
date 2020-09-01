

def print_matrix(a):
    '''
    печать поля
        '''
    print(' ',a[0][0],' | ',a[0][1],' | ',a[0][2])

    print(' ---','+','---','+','---'  )
    print(' ', a[1][0], ' | ', a[1][1], ' | ', a[1][2])

    print(' ---', '+', '---', '+', '---')
    print(' ', a[2][0], ' | ', a[2][1], ' | ', a[2][2])

def load_new_game():
    '''
    prepaire to new game
    '''
    return ([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])





def param_of_cell(pole):
    pole_coord = []
    pole_number = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    for i in [0,1,2]:
        for j in [0,1,2]:
            if pole == pole_number[i][j]:
                pole_coord.append(i)
                pole_coord.append(j)

    return(pole_coord)


def transpose(a):
    ''''
    Transponirovanie
    '''
    n = len(a)
    m = len(a[0])
    a_transp = []
    for j in range(m):
        c = []
        for i in range(n):
            c.append(a[i][j])
        a_transp.append(c)

    return(a_transp)

def game_over(matr):
    shablonx=['x','x','x']
    shablono = ['o', 'o', 'o']
    matr_diag = []
    matr_t = transpose(matr)
    matr_diagt = []
    #diagonal
    for i in range(3):
        matr_diag.append(matr[i][i])
    if matr_diag == shablonx or matr_diag == shablono:
        return True
    # diagonal obratnaya
    n=2
    for i in [0,1,2]:
        matr_diagt.append(matr[n-i][i])
    if matr_diagt == shablonx or matr_diag == shablono:

       return True
    #rows and columns
    for i in range(3):

        if matr[i] == shablonx or matr[i] == shablono:
            return True

        if matr_t[i] == shablonx or matr_t[i] == shablono:
            return True


def step_game(gamer,matr_a):

    p = True
    while p:
        print('Player',gamer.upper())
        print('Enter your move:')
        pole = input('')
        pole_coord = param_of_cell(pole)

        if matr_a[pole_coord[0]][pole_coord[1]] != ' ':
            print('pole zanyato')

        else:
            p = False
            if gamer == 'y':
                gamer = 'o'
            matr_a[pole_coord[0]][pole_coord[1]] = gamer
        print_matrix(matr_a)