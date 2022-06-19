class OrgTech:
	def __init__(self, type_tech, name):
		self.name = name
		self.type_tech = type_tech

class Printer(OrgTech):
	def action(self):
		print(f'{self.type_tech} {self.name} make some documents')

class CopyMach(OrgTech):
	def action(self):
		print(f'{self.type_tech} {self.name} copy some documents')

class Scaner(OrgTech):
	def action(self):
		print(f'{self.type_tech} {self.name} scan some documents')

scan1 = Scaner('Scaner_itel', 'xxad213')
scan2 = Scaner('Scaner_HP', 'dsa22r900a')
copy1 = CopyMach('Copy machine MSI', 'pf1999p900')
print1 = Printer('printer dexp', ' 120p676')

scan1.action()
scan2.action()
copy1.action()
print1.action()


"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, 
описывающий склад. А также класс «Оргтехника», который будет базовым для
 классов-наследников. Эти классы — конкретные типы оргтехники (принтер, 
 сканер, ксерокс). В базовом классе определите параметры, общие для 
 приведённых типов. В классах-наследниках реализуйте параметры, 
 уникальные для каждого типа оргтехники"""