def print_matrix(a):
    '''
    печать поля
        '''
    print(' ',a[0][0],' | ',a[0][1],' | ',a[0][2])

    print(' ---','+','---','+','---'  )
    print(' ', a[1][0], ' | ', a[1][1], ' | ', a[1][2])

    print(' ---', '+', '---', '+', '---')
    print(' ', a[2][0], ' | ', a[2][1], ' | ', a[2][2])

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
    #diagonal
    for i in range(3):
        matr_diag.append(matr[i][i])
    if matr_diag == shablonx or matr_diag == shablono:
        return True
    #rows and columns
    for i in range(3):

        if matr[i] == shablonx or matr[i] == shablono:
            return True

        if matr_t[i] == shablonx or matr_t[i] == shablono:
            return True


