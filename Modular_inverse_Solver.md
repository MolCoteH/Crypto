# Modular Inverse Solver
[Modular_inverse_Solver.py](https://github.com/MolCoteH/Crypto/blob/main/Modular_inverse_Solver.py)

This program allows you to encrypt and decrypt messages using modular arithmetic. It works by mapping each character in the message to a number based on its position in the alphabet, performing modular arithmetic operations on those numbers, and then mapping the result back to a character.

## Usage 

1. Enter your message as a space-separated list of numbers. For example: `12 15 18 21`

2. Enter the modulus - this is the number you will perform the modular arithmetic with. For example: `26` 

3. Choose whether to use uppercase letters by entering `y` or `n`.

4. (Optional) Enter a number to start the modular inverse from. Leave blank to use default of 0.

5. The program will print out the encrypted/decrypted message.

## Examples

Encrypting "hello" with a modulus of 26:

```
Enter your message: 8 5 12 12 15
Enter the modulus: 26
Use uppercase letters? (y/n): n

8 5 12 12 15  

hello
```

Decrypting the message from above by starting the modular inverse at 13:

``` 
Enter your message: 8 5 12 12 15
Enter the modulus: 26 
Use uppercase letters? (y/n): n
Start modular inverse from: 13

6 10 18 18 22  

hello
```

Using a modulus of 35 to encrypt "attack at dawn":

```
Enter your message: 1 20 20 1 3 11   4 20   4 1 22 14
Enter the modulus: 35
Use uppercase letters? (y/n): n

1 20 20 1 3 11  4 20  4 1 22 14

attack at dawn
```

Encrypting a message with uppercase letters:

```
Enter your message: 15 18 15
Enter modulus: 26
Use uppercase letters? (y/n): y 

15 18 15

OIL
```

Using a large modulus to encrypt a longer message:

```
Enter your message: 20 8 5   12 5   20 8 15   19 15 4 5   19 8 5   13 15 4 21 12 1 18   19 15 15 12
Enter modulus: 100
Use uppercase letters? (y/n): n

20 8 5   12 5   20 8 15   19 15 4 5   19 8 5   13 15 4 21 12 1 18   19 15 15 12 

use the modular tool
```
