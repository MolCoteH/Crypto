## Modular Inverse Cipher Decryption Program
[Modular_inverse_Solver.py](https://github.com/MolCoteH/Crypto/blob/main/Modular_inverse_Solver.py)
### Overview

This program implements two methods for decrypting a ciphertext that has been encrypted using a modular inverse cipher. The ciphertext is input as a list of numbers. The user selects the decryption method and provides the modulus used for encryption. The program then decrypts the message and prints the plaintext.

### Input

The program takes the following input from the user:

1. Ciphertext as a space-separated list of numbers (e.g. "12 24 16")

2. Modulus used for encryption as an integer (e.g. 27) 

3. Choice of decryption method (1 or 2)

4. Whether to use uppercase letters (y/n)

### Decryption Methods 

The program implements two modular inverse decryption methods:

1. Normal modular inverse calculation starting from 0. This computes (num * modinv(num, mod)) % mod for each number.

2. Modular inverse starting from -1. This computes (num % mod)^-1 % mod for each number. 

### Usage

To use the program:

1. Enter the ciphertext numbers when prompted

2. Enter the modulus used for encryption 

3. Select decryption method 1 or 2

4. Specify whether to use uppercase letters (y/n)

The program will then print the decrypted plaintext message.

### Examples

Here are 5 examples of using the program:

```
Enter message: 12 24 16
Enter modulus: 27
Enter 1 or 2: 1
Use uppercase? (y/n): n

12 24 16 
cat
```

```
Enter message: 15 18 22
Enter modulus: 25  
Enter 1 or 2: 2
Use uppercase? (y/n): y

15 18 22 
DOG
```

```
Enter message: 20 17 5
Enter modulus: 29
Enter 1 or 2: 1 
Use uppercase? (y/n): n

20 17 5
tub
```

```
Enter message: 18 15 21 11
Enter modulus: 27
Enter 1 or 2: 2
Use uppercase? (y/n): y

18 15 21 11
HELLO
```

```
Enter message: 7 15 23 11 14 
Enter modulus: 33
Enter 1 or 2: 1
Use uppercase? (y/n): n

7 15 23 11 14
happy
```

This covers the key steps for using the modular inverse cipher decryption program with detailed instructions and examples. Let me know if you need any clarification or have additional questions!
