class Storage:

	def __init__(self, name):
		self.name = name
		self.goods = []


	def move(from_sr, to_sr, good):
		from_sr.goods.remove(good.obj)
		to_sr.goods.append(good.obj)
		print(f'{good.obj} mooved from {from_sr.name} to {to_sr.name}')

	def receipt(self, good):
		self.goods.append(good.obj)

	def __str__(self):
		result = f'\n {self.name} include:\n'
		for el in self.goods:
			result += str(el) + '\n'
		return result



class OrgTech:
	def __init__(self, type_tech, name):
		self.name = name
		self.type_tech = type_tech
		self.obj = [type_tech, name]

class Printer(OrgTech):
	def action(self):
		print(f'{self.type_tech} {self.name} make some documents')

class CopyMach(OrgTech):
	def action(self):
		print(f'{self.type_tech} {self.name} copy some documents')

class Scaner(OrgTech):
	def action(self):
		print(f'{self.type_tech} {self.name} scan some documents')

scan1 = Scaner('Scaner_intel', 'xxad213')
scan2 = Scaner('Scaner_HP', 'dsa22r900a')
copy1 = CopyMach('Copy machine MSI', 'pf1999p900')
print1 = Printer('printer dexp', ' 120p676')

scan1.action()
scan2.action()
copy1.action()
print1.action()

moscow = Storage('Moscow_store')
petersburg = Storage('Peters_store')


moscow.receipt(scan1)
moscow.receipt(scan2)
petersburg.receipt(copy1)
petersburg.receipt(print1)
print(moscow)
print(petersburg)

Storage.move(moscow, petersburg, scan1)

print(moscow)
print(petersburg)

"""5. Продолжить работу над первым заданием.
 Разработайте методы, которые отвечают за приём оргтехники 
 на склад и передачу в определённое подразделение компании. 
 Для хранения данных о наименовании и количестве единиц оргтехники,
  а также других данных, можно использовать любую подходящую структуру 
  (например, словарь)."""