def recall_password(cipher_grille, ciphered_password):

    mygrille = conv_tuptolist(cipher_grille)
    mycipher = conv_tuptolist(ciphered_password)

    solved_password = ""

    for i in range(len(mygrille)):
        solved_password += get_letters(mygrille,mycipher)
        mygrille = rotate_grille(mygrille)

    print(solved_password)
    
    return solved_password

def conv_tuptolist(intuple):
    mylist = []

    for item in intuple:
        myitem = []
        for achar in item:
            myitem.append(achar)
        mylist.append(myitem)

    return mylist

def rotate_grille(inlist):
    mylist = []

    for x in range(4):
        myitem = []
        for y in range(3,-1,-1):
            myitem.append(inlist[y][x])
        mylist.append(myitem)

    return mylist

def get_letters(listgrille,listletters):
    myletters = ''

    for x in range(len(listgrille)):
        for y in range(len(listgrille[x])):
            if listgrille[x][y] == 'X':
                myletters = myletters + listletters[x][y]

    return myletters

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
