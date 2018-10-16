#!/usr/bin/env python

import string
import argparse

letters = string.ascii_lowercase

def encrypt(plaintext, key):
	encrypted = ""
	for c in plaintext:
		if c.lower() in letters:
			c_encrypted = letters[(letters.index(c.lower())+key)%26]
			if c.isupper():
				c_encrypted = c_encrypted.upper()
		else:
			c_encrypted = c
		encrypted += c_encrypted
	return encrypted
	
def decrypt(cipher, key):
	return encrypt(cipher, -key)

def bruteforce(cipher):
	for i in range(1, 26):
		print(str(i) + " : " + decrypt(cipher, i) + "\n")

def main():
    parser = argparse.ArgumentParser(description = "A simple caesar cipher program")
    parser.add_argument("command", help = "encrypt, decrypt, or brute (try all possible keys)")
    parser.add_argument("-k", "--key", help = "numeric caesar cipher key for encryption or decryption", required = False)
    parser.add_argument("-t", "--text", help = "text to be encrypted or decrypted")
    
    args = parser.parse_args()
    
    if args.command == "encrypt":
        print(encrypt(args.text, int(args.key)))
    elif args.command == "decrypt":
        print(decrypt(args.text, int(args.key)))
    elif args.command == "brute":
        bruteforce(args.text)
    else:
        print("Error: unrecognized command")
        exit(1)
        
        
if __name__ == "__main__":
    main()
