
class Coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, otra_coordinate):
    x_diff = (self.x - otra_coordinate.x)**2 #al cuadrado
    y_diff = (self.y - otra_coordinate.y)**2

    return (x_diff + y_diff)**0.5 #raíz cuadrada de estas distancias


if __name__ ==  '__main__':
  coord_1 = Coordinate(3, 30)
  coord_2 = Coordinate(4, 8)

  print(coord_1.distance(coord_2))
  print(isinstance(coord_2, Coordinate)) # check if the instance belongs to the class