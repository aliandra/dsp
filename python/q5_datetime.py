# Hint:  use Google to find python function

from datetime import datetime


def days_between(date_start, date_stop, date_format):
    """
    Prints the number of days between two dates.
    date_start and date_stop must be formatted the same.
    """
    dstart = datetime.strptime(date_start, date_format)
    dstop = datetime.strptime(date_stop, date_format)
    days_between = dstop - dstart
    print 'There are', days_between.days, 'days between',
    print dstart.strftime(date_format), 'and', dstop.strftime(date_format)


# a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

days_between(date_start, date_stop, '%m-%d-%Y')

# b)
date_start = '12312013'
date_stop = '05282015'

days_between(date_start, date_stop, '%m%d%Y')

# c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

days_between(date_start, date_stop, '%d-%b-%Y')
