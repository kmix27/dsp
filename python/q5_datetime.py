# Hint:  use Google to find python function
from datetime import datetime, timedelta

formA = '%m-%d-%Y'
formB = '%m%d%Y'
formC = '%d-%b-%Y'


def findDays(start, stop, format):
    d0 = datetime.strptime(start, format)
    d1 = datetime.strptime(stop, format)
    if d0 > d1:
        raise ValueError("start must be before end")
    else:
        delta = d1-d0
    return delta.days

# a)
date_startA = '01-02-2013'
date_stopA = '07-28-2015'

print('A =', findDays(date_startA, date_stopA, formA), 'days')

# b)
date_startB = '12312013'
date_stopB = '05282015'

print('B =', findDays(date_startB, date_stopB, formB), 'days')

# c)
date_startC = '15-Jan-1994'
date_stopC = '14-Jul-2015'

print('C =', findDays(date_startC, date_stopC, formC), 'days')
