nric = input('Enter an NRIC number: ')

# Type your code below
prefix = nric[0]
valid_prefix = 'stgfSTGF'
digits = nric[1:8]
suffix = nric[-1]
totalnum = 0
seqlist = [1, 2, 3, 4, 5, 6, 7]
diglist = [2, 7, 6, 5, 4, 3, 2]
if str(digits).isdecimal() and prefix in valid_prefix:
    for i in range(len(seqlist)):
      totalnum = totalnum + seqlist[i]*diglist[i]
    if prefix == 'T' or prefix == 'G':
       totalnum += 4
    remainder = totalnum%11
    if remainder == 0:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'J'
        else:
            checkdigit = 'X'
    if remainder == 1:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'Z'
        else:
            checkdigit = 'W'
    if remainder == 2:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'I'
        else:
            checkdigit = 'U'
    if remainder == 3:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'H'
        else:
            checkdigit = 'T'
    if remainder == 4:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'G'
        else:
            checkdigit = 'R'
    if remainder == 5:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'F'
        else:
            checkdigit = 'Q'
    if remainder == 6:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'E'
        else:
            checkdigit = 'P'
    if remainder == 7:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'D'
        else:
            checkdigit = 'N'
    if remainder == 8:
        if prefix ==  'S' or prefix == 'T':
            checkdigit = 'C'
        else:
            checkdigit = 'M'
    if remainder == 9:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'B'
        else:
            checkdigit = 'L'
    if remainder == 10:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'A'
        else:
            checkdigit = 'K'
    if checkdigit == suffix:
        print('NRIC is valid.')
    else:
        print('NRIC is invalid.')
else:
        print('NRIC is invalid.')