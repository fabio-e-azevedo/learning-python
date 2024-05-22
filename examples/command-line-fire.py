import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    return 2 * number

  def sum(self, number1, number2):
    return number1 + number2

if __name__ == '__main__':
  fire.Fire(Calculator)
