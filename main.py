class Quadrado:

  def __init__(self, lado):
    self.lado = lado

  def area(self):
    return self.lado * self.lado

  def __repr__(self):
    return f"lado: {self.lado}"

  def __add__(self, other):
    if (isinstance(other, Quadrado)):
      return Quadrado(self.lado + other.lado)


q1 = Quadrado(1)
print(q1, q1.area())

q2 = Quadrado(1)
print(q1 + q2)


class Circulo:

  def __init__(self, raio):
    self.raio = raio

  def area(self):
    return 3.14 * self.raio**2

  def __repr__(self):
    return f"raio: {self.raio}"

  def __add__(self, other):
    if (isinstance(other, Circulo)):
      return Circulo(self.raio + other.raio)


circulo = Circulo(2)
print(circulo, circulo.area())


class Retangulo:

  def __init__(self, comprimento, largura):
    self.comprimento = comprimento
    self.largura = largura

  def area(self):
    return self.comprimento * self.largura

  def __repr__(self):
    return f"Retangulo\ncomprimento: {self.comprimento} largura:{self.largura}"


rectangulo = Retangulo(2, 3)
print(rectangulo)


class Quadrado(Retangulo):

  def __init__(self, lado):
    super().__init__(lado, lado)

  def __repr__(self):
    return super().__repr__()
