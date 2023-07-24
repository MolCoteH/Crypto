import math

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789_'
uppercase_alphabet = alphabet.upper()

while True:
  message = input("Enter your message as a list of numbers: ")
  try:
    message = [int(num) for num in message.split()]
    break
  except ValueError:
    print("Please enter only numbers separated by spaces")
    
while True:
  mod = input("Enter the modulus: ")
  if mod.isdigit():
    mod = int(mod)
    break 
  else:
    print("Please enter a number")
    
uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
if uppercase:
  alphabet = uppercase_alphabet
  
while True:
  from_num = input("Start modular inverse from (leave blank for default, 0 for normal): ")
  if from_num.isdigit() or from_num == '' or from_num == '0':
    break
  else:
    print("Please enter a number or leave blank")
    
if from_num == '0' or from_num == '':
  message = [str(num) for num in message]

  char_map = {}
  for i in range(mod):
    char_map[i] = alphabet[i % len(alphabet)]

  decrypted = ""
  print('\n')
  for num in message:
    num = int(num) % mod
    print(num, end=' ')
    decrypted += char_map[num]

  print('\n', decrypted)

elif from_num:
  from_num = int(from_num)
  
  print('\n')
  result = ''
  for num in message:
    mod_inv = pow(num % mod, from_num, mod)
    index = (mod_inv + from_num) % len(alphabet)
    print(index, end=' ')
    char = alphabet[index]
    result += char

  print('\n', result)

else:
   print('Goodby')
