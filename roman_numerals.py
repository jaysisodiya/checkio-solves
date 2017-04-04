def checkio(data):
    """Given a number, convert to roman numeral
    1      I
    4      IV
    5      V
    9      IX
    10     X
    40     XL
    50     L
    90     XC
    100    C
    400    CD
    500    D
    900    CM
    1000   M
    """
    
    tempdata = data
    
    thousands = 0
    ninehundreds = 0
    fivehundreds = 0
    fourhundreds = 0
    hundreds = 0
    nineties = 0
    fifties = 0
    fourties = 0
    tens = 0
    nines = 0
    fives = 0
    fours = 0
    ones = 0
    
    outroman = ""
    
    thousands = tempdata // 1000
    tempdata = tempdata % 1000
    
    for i in range(thousands):
        outroman = outroman + 'M'

    if tempdata >= 900:
        ninehundreds = 1
        tempdata = tempdata - 900
        outroman = outroman + 'CM'
    elif tempdata >= 500:
        fivehundreds = 1
        tempdata = tempdata - 500
        outroman = outroman + 'D'
    elif tempdata >= 400:
        fourhundreds = 1
        tempdata = tempdata - 400
        outroman = outroman + 'CD'

    hundreds = tempdata // 100
    tempdata = tempdata % 100

    for i in range(hundreds):
        outroman = outroman + 'C'
    
    if tempdata >=90:
        nineties = 1
        tempdata = tempdata - 90
        outroman = outroman + 'XC'
    elif tempdata >= 50:
        fifties = 1
        tempdata = tempdata - 50
        outroman = outroman + 'L'
    elif tempdata >= 40:
        fourties = 1
        tempdata = tempdata - 40
        outroman = outroman + 'XL'
        
    tens = tempdata // 10
    tempdata = tempdata % 10

    for i in range(tens):
        outroman = outroman + 'X'
        
    if tempdata >= 9:
        nines = 1
        tempdata = tempdata - 9
        outroman = outroman + 'IX'
    elif tempdata >= 5:
        fives = 1
        tempdata = tempdata - 5
        outroman = outroman + 'V'
    elif tempdata >= 4:
        fours = 1
        tempdata = tempdata - 4
        outroman = outroman + 'IV'
        
    ones = tempdata // 1
    
    for i in range(ones):
        outroman = outroman + 'I'
    
    return outroman

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
