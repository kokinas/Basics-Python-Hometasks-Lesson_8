class DelZero(Exception):
	def __init__(self, txt):
		self.txt = txt


while True:
	x = int(input('type some divider: '))
	try:
		if x != 0:
			x = 10/x
		else:
			raise DelZero("don't divide by Zero")
	except DelZero as err:
		print(err)

		






"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
 Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве 
 делителя программа должна корректно обработать эту ситуацию и не завершиться с 
 ошибкой.
"""