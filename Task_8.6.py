class Storage:

	def __init__(self, name):
		self.name = name
		self.goods = {}

	@staticmethod
	def move(from_sr, to_sr, good, amount):
		try:
			val_from = from_sr.goods.get(good.type_tech)
			val_to = to_sr.goods.get(good.type_tech)
			if val_to == None: val_to = 0
			if amount < val_from:
				from_sr.goods.update({good.type_tech : (val_from - amount)})
				to_sr.goods.update({good.type_tech : val_to + amount})
			else:
				print('not enouhg goods')
			print(f'{good.type_tech} mooved from {from_sr.name} to {to_sr.name} in amount {amount}')
		except TypeError as tpe:
			print('amount of goods must be int')
			return tpe

	def receipt(self, good, numb):
		self.goods.update({good.type_tech : numb})


	def __str__(self):
		result = f'\n{self.name} in stock: \n'
		for key in self.goods.items():
			result += str(key[0]) + f' in amount {key[1]} \n'
		return result

class OrgTech:
	def __init__(self, type_tech, numb):
		self.type_tech = type_tech
		self.obj = {type_tech : numb}
		

class Printer(OrgTech):
	def action(self):
		print(f'{self.type_tech} make some documents')

class CopyMach(OrgTech):
	def action(self):
		print(f'{self.type_tech} copy some documents')

class Scaner(OrgTech):
	def action(self):
		print(f'{self.type_tech} scan some documents')

scan1 = Scaner('Scaner_intel', 24)
scan2 = Scaner('Scaner_HP', 54)
copy1 = CopyMach('Copy machine MSI', 22)
print1 = Printer('printer dexp', 9)

scan1.action()
scan2.action()
copy1.action()
print1.action()

moscow = Storage('Moscow_store')
petersburg = Storage('Peters_store')


moscow.receipt(scan1, 'dsa')
moscow.receipt(scan2, 9)
moscow.receipt(copy1, 2)
petersburg.receipt(copy1, 74)
petersburg.receipt(print1, 14)
print(moscow)
print(petersburg)

moscow.move(moscow, petersburg, scan1, 1)
petersburg.move(moscow, petersburg, scan1, 1)
Storage.move(moscow, petersburg, scan2, 1)

print(moscow)
print(petersburg)



"""5. Продолжить работу над первым заданием.
 Разработайте методы, которые отвечают за приём оргтехники 
 на склад и передачу в определённое подразделение компании. 
 Для хранения данных о наименовании и количестве единиц оргтехники,
  а также других данных, можно использовать любую подходящую структуру 
  (например, словарь)."""


"""


. Продолжить работу над вторым заданием. Реализуйте механизм валидации
 вводимых пользователем данных. Например, для указания количества принтеров,
  отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
 изученных на уроках по ООП."""