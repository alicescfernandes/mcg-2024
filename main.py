class Quadrado:

  def __init__(self, lado):
    self.lado = lado

  def area(self):
    return self.lado * self.lado

  def __repr__(self):
    return f"lado: {self.lado}"


q1 = Quadrado(3)
print(q1, q1.area())


class Circulo:
  def __init__(self, raio):
    self.raio = raio

  def area(self):
    return 3.14 * self.raio ** 2
    
  def __repr__(self):
    return f"raio: {self.raio}"

circulo = Circulo(2)
print(circulo, circulo.area())