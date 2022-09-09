from datetime import datetime

my_time = datetime.now()

my_day = datetime.today()

print(my_time)
print(my_day)
print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')

my_str = my_time.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_str = my_time.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str = my_time.strftime('Estamos en el año %Y')
print(f'Formato Random: {my_str}')