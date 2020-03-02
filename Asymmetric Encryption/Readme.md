Name:- Utsav Raychaudhuri
Email Id:- utsav@pdx.edu	
2)A brief description of what you are submitting.
Ans:- This is a program which implements a public key cryptography algorithm. A 32 bit prime p,q are created using a pseudo-random generator and then tested for primality using the Miller-Rabin algorithm. This key is then used for generating the public and the private key. Using the public key the message is encrypted and using the private key the message is decrypted
3)A precise description of how to build and use your program.
The program is written in Python3 and the author assumes that you have python3 on your system for this program to work.
Execution:- python3 utsav_public_key_crypto.py
4. A list of files that should be in the archive, and a one line description of each file
utsav_public_key_crypto.py-  The main program
pubkey.txt- the file containing the public key needed for encryption
privkey.txt- The file containing the private key needed for decryption
message.text- the message needed for encryption and decryption
plaintext.txt- The file containing the plaintext after decryption
ciphertext.txt- the file containing the ciphertext after encryption