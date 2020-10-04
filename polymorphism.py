
class Person:

  def __init__(self, name):
    self.name = name

  def move(self):
    print('I am walking')


class Cyclist(Person):

  def __init__(self, name):
    super().__init__(name)

  def move(self):
    print('I ride my bike')


def main ():
  person = Person('Chiara')
  person.move()

  cyclist = Cyclist('Luna')
  cyclist.move()

if __name__ == '__main__':
  main()
