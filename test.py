import re

test = 'jhsfh@hackerrank.com'

if re.match(r'([a-z]{1,6}([_]?)([0-9]{0,4}))@hackerrank.com',test):
    print('Great Journey!')
else:
    print('Fuck Journey!')

