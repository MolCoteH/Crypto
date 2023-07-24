import math

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789_'
uppercase_alphabet = alphabet.upper()

message = input("Enter your message as a list of numbers: ")
message = [int(num) for num in message.split()]

mod = int(input("Enter the modulus: "))

uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
if uppercase:
  alphabet = uppercase_alphabet

print("Choose decryption method:")
print("1. Modular inverse(normal-start)")
print("2. Modular inverse(-1)") 

choice = input("Enter 1 or 2: ")

if choice == '2':

  print('\n')
  result = ''
  for num in message:
      mod_inv = pow(num % mod, -1, mod)
      index = mod_inv - 1
      print(index,end=' ')  
      char = alphabet[index]
      result += char

  print('\n',result)

elif choice == '1':

  message = [str(num) for num in message] # Convert back to strings

  # Dynamically generate character mapping based on modulus
  char_map = {}
  for i in range(mod):
    char_map[i] = alphabet[i % len(alphabet)]

  decrypted = ""
  print('\n')
  for num in message:
    num = int(num) % mod
    print(num,end=' ')
    decrypted += char_map[num]

  print('\n',decrypted)
  
else:
  print("Invalid choice")
