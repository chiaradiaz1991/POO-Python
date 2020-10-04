
class WashingMachine:

  def __init__(self): #constructor
    pass # there is no counstructor

  def wash(self, temperature = 'warm'):
    self._fill_with_water(temperature)
    self._add_soap()
    self._wash()

  def _fill_with_water(self, temperature):
    print(f'filling with water, temperature: {temperature}')

  def _add_soap(self):
    print('adding soap')

  def _wash(self):
    print('washing the clothes')
    

if __name__ == '__main__':
  washing_machine = WashingMachine()
  washing_machine.wash()
