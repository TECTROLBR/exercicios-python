import calendar
from datetime import date
cal = int(input('especifique um ano? coloque 1 parao ano atual! '))
res =calendar.isleap(cal)
if cal == int ('1') :
    cal = int(date.today().year)
if res == True:
    print('este ano de {} e bissexto'.format(cal))
else:
    print('este ano de {} nao e bissexto'.format(cal))


