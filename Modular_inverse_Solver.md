# Modular Inverse Solver
[Modular_inverse_Solver.py](https://github.com/MolCoteH/Crypto/blob/main/Modular_inverse_Solver.py)

This program allows you to encrypt and decrypt messages using modular arithmetic. It works by mapping each character in the message to a number based on its position in the alphabet, performing modular arithmetic operations on those numbers, and then mapping the result back to a character.

## Usage 

1. Enter your message as a space-separated list of numbers. For example: `12 15 18 21`

2. Enter the modulus - this is the number you will perform the modular arithmetic with. For example: `26` 

3. Choose whether to use uppercase letters by entering `y` or `n`.

4. (Optional) Enter a number to start the modular inverse from. Leave blank to use default of 0. (You can also use negative numbers like -1)

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

Decrypting the message from above by starting the modular inverse at 41:

``` 
Enter your message: 432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63 
Enter the modulus: 41
Use uppercase letters? (y/n): n
Start modular inverse from: -1

27 13 21 29 17 31 29 11 24 36 7 30 17 3 36 2 32 34 26 1 3 2 27 

1nv3r53ly_h4rd_c680bdc1
```

Using a modulus of 37 to encrypt "r0und_n_r0und_79c18fb3":

```
Enter your message: 128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140
Enter the modulus: 37
Use uppercase letters? (y/n): n
Start modular inverse from (leave blank for default, 0 for normal): 0

17 26 20 13 3 36 13 36 17 26 20 13 3 36 33 35 2 27 34 5 1 29 

r0und_n_r0und_79c18fb3
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
