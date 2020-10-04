
class Car:
  def __init__(self, model, brand, color):
    self.model = model
    self.brand = brand
    self.color = color

    self._state = 'resting'
    self._motor = Motor(color = 'red')

  def speed(self, type='slow'):
    if type == 'fast':
        self._motor.fill_with_gasoline(10)
    else:
        self._motor.fill_with_gasoline(3)

        self._state = 'moving'


class Motor:
  def __init__(self, color, type='gasoline'):
    self.type = type
    self.color = color
    self._temperature = 0

  def fill_with_gasoline(self, amount):
    pass
