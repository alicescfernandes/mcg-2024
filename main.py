class Quadrado:

  def __init__(self, lado):
    self.lado = lado

  def area(self):
    return self.lado * self.lado

  def __repr__(self):
    return f"lado: {self.lado}"


instancia = Quadrado(3)
print("instancia", instancia)
