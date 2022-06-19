class Date:
	
	 def __init__(self, date):
	 	self.date = date

	 @classmethod
	 def convert_to_numb(cls, date):
	 	result = ''
	 	for numb in date.split('-'):
	 		result += numb
	 	return int(result)

	 @staticmethod
	 def valid_date(date):
	 	
	 	if int(date.split('-')[1]) > 12 or int(date.split('-')[1]) < 0 :
	 		print(f'month {date} is not valid')
	 	else: 
	 		print(f'Date is valid')

x = Date.convert_to_numb('17-01-2022')
print(x)

a = Date('01-07-2022')
print (a.convert_to_numb('02-02-2022'))

Date.valid_date('12-21-2013')

z = Date('11-11-2021')
z.valid_date('12-11-2022')


"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать
 дату в виде строки формата «день-месяц-год». В рамках класса реализовать два 
 метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
  год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
  должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных."""