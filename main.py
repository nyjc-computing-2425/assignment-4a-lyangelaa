nric = input('Enter an NRIC number: ')

# Type your code below
prefix = nric[0]
valid_prefix = 'stgfSTGF'
digits = nric[1:8]
if digits.isdigit == False or len(nric) != 9:
    print('NRIC is invalid.')
else:
  suffix = nric[-1]
  totalnum = 0
  seqlist = [1, 2, 3, 4, 5, 6, 7]
  diglist = [2, 7, 6, 5, 4, 3, 2]
  suffix_str_1 = "JZIHGFEDCBA"
  suffix_str_2 = "XWUTRQPNMLK"
  for i in range(len(diglist)):
      totalnum = totalnum + int(digits[i])*diglist[i]
  if prefix == 'T' or prefix == 'G':
    totalnum = totalnum + 4
  remainder = totalnum%11
  check_alpha = ''
  if prefix in "ST":
    check_alpha = suffix_str_1[remainder]
  elif prefix in "FG":
    check_alpha = suffix_str_2[remainder]
  if suffix == check_alpha:
    print('NRIC is valid.')
  else:
    print('NRIC is invalid.')