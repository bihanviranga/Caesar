#!/usr/bin/python
#Caesar cipher encryption.

import sys

alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetL = alphabetU.lower()


def main():
	#Determine mode.
	try:
		if sys.argv[1]=="-e":
			mode="e"
		elif sys.argv[1]=="-d":
			mode="d"
		elif sys.argv[1]=="-h" or sys.argv[1]=="-help":
			showHelp()
			sys.exit()
		else:
			print("Invalid argument. Use -e for encoding and -d for decoding. -h shows help.")
			sys.exit()
	except IndexError:
		print("Invalid argument. Use -e for encoding and -d for decoding. -h shows help.")
		sys.exit()

	#Determine key.
	try:
		key=int(sys.argv[2])
	except IndexError:
		key=int(input("Key: "))

	#Determine input string.
	try:
		msg=str(sys.argv[3])
	except IndexError:
		msg=str(input("Input string: "))

	#Call the appropriate function to encode/decode
	if mode=="e":
		encode(msg,key)
	elif mode=="d":
		decode(msg,key)
	else:
		showHelp()



def encode(msg,key):
	output = ""

	for letter in msg:
		if letter in alphabetU:
			alphabet=alphabetU
		elif letter in alphabetL:
			alphabet=alphabetL
		else:
			output+=letter
			continue

		cIndex=alphabet.index(letter)
		newIndex=cIndex+key

		while newIndex>25:
			if newIndex>25:
				newIndex=newIndex-25-1 #extra -1 is because indexing starts from zero.

		output+=(alphabet[newIndex])


	print(output)


def decode(msg,key=0):
	output = ""

	if key!=0:
		for letter in msg:
			if letter in alphabetU:
				alphabet=alphabetU
			elif letter in alphabetL:
				alphabet=alphabetL
			else:
				output+=letter
				continue

			cIndex=alphabet.index(letter)
			newIndex=cIndex-key

			while newIndex<0:
				if newIndex<0:
					newIndex=newIndex+25+1

			output+=(alphabet[newIndex])

		print(output)
	else:
		for i in range(1,26):
			decode(msg,i)


def showHelp():
	helpmsg="""
NAME:
	caesar - Encrypt and decrypt text using the famous Caesar cipher.


SYNOPSIS :
	$ caesar [mode] [key] [input]

DETAILS :

	Only text will be encrypted/decrypted. Numbers and other characters will remain intact.

	mode :
		-e = encrypt
		-d = decrypt
		-h --help = show this help file.

	key :
		The key that should be used / has been used to encrypt.

	input :
		The message that should be encrypted. Numbers and other characters will be ignored.


Version 1.0

MIT License.
Copyright Bihan Viranga <bihanviranga@gmail.com>
"""

	print(helpmsg)
	




if __name__ == "__main__":
	main()