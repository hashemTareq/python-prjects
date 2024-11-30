import os

instruction = """
[1]- You have to input float numbers.
[2]- Choose from these operations ['+', '-', '*', '/'] only.
"""

def start():
  print('---------------------')
  print('- Hashem Calculator -')
  print('---------------------\n')

def inputs():
  os.system('cls')
  try:
    number_1 = float(input('First number: ').strip())
    number_2 = float(input('Second number: ').strip())
    operation = input('Operation [ +, -, *, /]: ')[0].strip()
    get_result(number_1, number_2, operation)
  except ValueError:
    print(instruction)

def get_result(number_1, number_2, operation):
  result = 0.0
  if operation in ['+', '-', '*', '/']:
    match operation:
      case '+':
        result = number_1 + number_2
      case '-':
        result = number_1 - number_2
      case '*':
        result = number_1 * number_2
      case '/':
        result = number_1 / number_2
    os.system('cls')
    print(f'{number_1} {operation} {number_2} = {result}') 
  else:
    os.system('cls')
    print(f" - We don't have these operation ['{operation}'] ...!\n")


def main_work():
  start()
  while True:
    inputs()
    choice = input('Press any key: to continue, ex to exit: ').strip()
    if choice == 'ex':
      os.system('cls')
      print('\n #- Thank\'s to use Hashem Calculator.\n')
      break
    else:
      pass

main_work()