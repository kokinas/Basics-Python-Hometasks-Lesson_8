class Complex_n:
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	def __add__(self, other):
		x = self.real + other.real
		y = self.imag + other.imag
		return Complex_n(x, y)

	def __sub__(self, other):
		x = self.real - other.real
		y = self.imag - other.imag
		return Complex_n(x, y)

	def __str__(self):
		self_v = self.get_var_name()
		if self.imag > 0 and self.real != 0:
			return f'{self_v} = {self.real} + {self.imag}i'
		if self.imag < 0 and self.real != 0:
			return f'{self_v} = {self.real} - {abs(self.imag)}i'
		if self.imag == 0:
			return f'{self_v} = {self.real}'
		if self.real == 0:
			return f'{self_v} = {self.imag}i'


	def get_var_name(self):
		for i, j in globals().items():
			if j is self:
				return i


a = Complex_n(5, -3)
b = Complex_n(-2, 4)
c = Complex_n(2, -9)
print(a)
print(b)
print(c)
d = a + b - c
print(d)
e = b + c
print(e)
f = Complex_n(2, 0)
print (f)
g = Complex_n(0, 6)
print (g)


"""7. Реализовать проект «Операции с комплексными числами». Создайте класс 
«Комплексное число». Реализуйте перегрузку методов сложения и умножения 
комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
 класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
  Проверьте корректность полученного результата."""