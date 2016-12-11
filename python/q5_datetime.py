# Hint:  use Google to find python function

from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

date_format = '%m-%d-%Y'
date_start = datetime.strptime(date_start, date_format)
date_stop = datetime.strptime(date_stop, date_format)
days_between = date_stop - date_start
print 'There are', days_between.days, 'days between', 
print date_start.strftime(date_format), 'and', date_stop.strftime(date_format)



####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_format = '%m%d%Y'
date_start = datetime.strptime(date_start, date_format)
date_stop = datetime.strptime(date_stop, date_format)
days_between = date_stop - date_start
print 'There are', days_between.days, 'days between', 
print date_start.strftime(date_format), 'and', date_stop.strftime(date_format)



####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_format ='%d-%b-%Y'
date_start = datetime.strptime(date_start, date_format)
date_stop = datetime.strptime(date_stop, date_format)
days_between = date_stop - date_start
print 'There are', days_between.days, 'days between', 
print date_start.strftime(date_format), 'and', date_stop.strftime(date_format)