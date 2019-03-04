import sys
import os
import fileinput
import random

currentPosition = 0;
currentBlockPosition = 0;
args = ""

#search variables
patHash = 0; #pattern hash value
txtHash = 0
M = 0; #pattern length
Q = random.getrandbits(16); #a large prime
R = 256; #alphabet size
RM = 0; #R^(M-1) % Q
chars = []

def main():

	#Clear the output file which the scanner symbols will be written to
	f = open('symbols.txt','w')
	f.write('')
	f.close()

	commentBlock = False;

	#scan input
	with open(sys.argv[1], "r") as word_list:
		words = word_list.read().split()

	#Remove comments, tabs, spaces, and newlines
	for i in range(len(words)-1):

		#Check for and disregard comments
		if (i<len(words)-1):
			if words[i] == '/' and words [i+1] == '/' or words[i] == '/' and words [i+1] == '*':
				commentBlock = True
			if words[i] == '*' and words [i+1] == '/' or words[i] == '\n':
				commentBlock = False
		if commentBlock:
			words[i] = 'comment'

		#Remove whitespace
		if words[i] == ' ' or words[i] == '\t' or words[i] == '\n':
			del words[i]
		
	words = [i for i in words if i != 'comment']
	
	print(words)

	try:
    		checkIdentifierInitialization("p", words)
		getSym(words)
	except:
		print("Scanning Complete")
	

#First check if the word is a number. Then check for reserved words, then reserved symbols. If those aren't possibilities, assume an identifier has been reached.
def getSym(words):

	if (currentPosition < len(words)):

		#Check for reserved words in Java.
		checkForReservedWords(words[currentPosition], words)
		symList = list(words[currentPosition])

		#If the entire word isn't reserved, check individual characters.
		checkForReservedSymbols(symList,words)
		currentBlockPosition = 0;
		getSym(words)

	#Once all symbols have been checked, start parsing the scanned symbols.
	else :

		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'EofSym')
		f.close()

		sys.stdout.write("EofSym\n");

		#First line is always blank - remove it
		with open('symbols.txt', 'r') as fin:
    			data = fin.read().splitlines(True)
		with open('symbols.txt', 'w') as fout:
    			fout.writelines(data[1:])

    		#start the parser, passing in the symbols
    		os.system('python rdparser.py symbols.txt')

		sys.exit()


def checkForReservedWords(sym, words):
	global currentPosition
	global currentBlockPosition
	global args

	currentBlockPosition = 0

	checkForNum(sym)

	sym = words[currentPosition]

	if sym == "not":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'NotSym')
		f.close()

		sys.stdout.write("NotSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "or":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'OrSym')
		f.close()
		
		sys.stdout.write("OrSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "and":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'AndSym')
		f.close()

		sys.stdout.write("AndSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "of":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'OrSym')
		f.close()

		sys.stdout.write("OfSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "then":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'ThenSym')
		f.close()

		sys.stdout.write("ThenSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "do":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'DoSym')
		f.close()

		sys.stdout.write("DoSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "not":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'NotSym')
		f.close()

		sys.stdout.write("NotSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "if":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'IfSym')
		f.close()

		sys.stdout.write("IfSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "exit":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'ExitSym')
		f.close()

		sys.stdout.write("ExitSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "else":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'ElseSym')
		f.close()

		sys.stdout.write("ElseSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "while":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'WhileSym')
		f.close()

		sys.stdout.write("WhileSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "{":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'LCurlSym')
		f.close()

		sys.stdout.write("LCurlSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "}":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'RCurlSym')
		f.close()

		sys.stdout.write("RCurlSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "public":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'PublicSym')
		f.close()

		sys.stdout.write("PublicSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "static":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'StaticSym')
		f.close()

		sys.stdout.write("StaticSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "void":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'VoidSym')
		f.close()

		sys.stdout.write("VoidSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "main":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'MainSym')
		f.close()

		sys.stdout.write("MainSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "[]":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'ArraySym')
		f.close()

		sys.stdout.write("ArraySym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "String":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'StringSym')
		f.close()

		sys.stdout.write("StringSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "args":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'ArgsSym')
		f.close()

		sys.stdout.write("ArgsSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "System":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'SystemSym')
		f.close()

		sys.stdout.write("SystemSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "out":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'OutSym')
		f.close()

		sys.stdout.write("OutSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "println":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'PrintSym')
		f.close()

		sys.stdout.write("PrintSym\n");
		currentPosition+=1;
		getSym(words)
	elif sym == "class":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'ClassSym')
		f.close()

		sys.stdout.write("ClassSym\n");
		currentPosition+=1;
		getSym(words)
	elif "*" in sym or "/" in sym or "%" in sym or "&" in sym or "+" in sym or "-" in sym or "&" in sym or "|" in sym or "." in sym or "," in sym or ":" in sym or "(" in sym or ")" in sym or "[" in sym or "]" in sym or ";" in sym:
		symList = list(words[currentPosition])
		checkForReservedSymbols(symList,words)
	else:
		#Append the symbol to the output file and the global linked list of print arguments
		args += sym
		f = open('symbols.txt','a')
		f.write('\n' + 'IdentSym')
		f.close()

		sys.stdout.write("IdentSym\n");
		currentPosition+=1;
		getSym(words)


def checkForReservedSymbols(symList,words):
	global currentPosition
	global currentBlockPosition

	if currentBlockPosition < len(symList):

		sym = symList[currentBlockPosition]

		if sym == "<" or sym == "=" or sym == ">" or sym == "!":
			checkRelationalOp(words)
		elif sym == None:
			sys.stdout.write("null\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "*":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'TimesSym')
			f.close()

			sys.stdout.write("TimesSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "/":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'DivSym')
			f.close()

			sys.stdout.write("DivSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "%":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'ModSym')
			f.close()

			sys.stdout.write("ModSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "&":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'AndSym')
			f.close()

			sys.stdout.write("AndSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "+":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'PlusSym')
			f.close()

			sys.stdout.write("PlusSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "-":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'MinusSym')
			f.close()

			sys.stdout.write("MinusSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "|":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'OrSym')
			f.close()

			sys.stdout.write("OrSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == ".":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'PeriodSym')
			f.close()

			sys.stdout.write("PeriodSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == ",":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'CommaSym')
			f.close()

			sys.stdout.write("CommaSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == ":":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'ColonSym')
			f.close()

			sys.stdout.write("ColonSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "(":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'LparenSym')
			f.close()

			sys.stdout.write("LparenSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == ")":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'RparenSym')
			f.close()

			sys.stdout.write("RparenSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "[":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'LbrakSym')
			f.close()

			sys.stdout.write("LbrakSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == "]":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'RbrakSym')
			f.close()

			sys.stdout.write("RbrakSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
		elif sym == ";":
			#Append the symbol to the output file
			f = open('symbols.txt','a')
			f.write('\n' + 'SemicolonSym')
			f.close()

			sys.stdout.write("SemicolonSym\n");
			currentBlockPosition+=1;
			checkForReservedSymbols(symList,words)
	else:
		currentPosition+=1
		getSym(words)
	

def checkForNum(sym):

	if type(sym) == int:
		sys.stdout.write("NumberSym\n");
		currentPosition+=1;


def checkRelationalOp(words):
	global currentPosition
	global currentBlockPosition

	sym = list(words[currentPosition])
	next = list(words[currentPosition])

	if sym == "!" and next == "=":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'NeqSym')
		f.close()

		sys.stdout.write("NeqSym\n");
		currentBlockPosition+=2;
		checkForReservedSymbols(symList,words)
	elif sym == "<" and next == "=":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'LeqSym')
		f.close()

		sys.stdout.write("LeqSym\n");
		currentBlockPosition+=2;
		checkForReservedSymbols(symList,words)
	elif sym == ">" and next == "=":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'GeqSym')
		f.close()

		sys.stdout.write("GeqSym\n");
		currentBlockPosition+=2;
		checkForReservedSymbols(symList,words)
	elif sym == ">":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'GtrSym')
		f.close()

		sys.stdout.write("GtrSym\n");
		currentBlockPosition+=2;
		checkForReservedSymbols(symList,words)
	elif sym == "<" and next == "=":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'LssSym')
		f.close()

		sys.stdout.write("LssSym\n");
		currentBlockPosition+=2;
		checkForReservedSymbols(symList,words)
	elif sym == "=":
		#Append the symbol to the output file
		f = open('symbols.txt','a')
		f.write('\n' + 'EqlSym')
		f.close()

		sys.stdout.write("EqlSym\n");
		currentBlockPosition+=2;
		checkForReservedSymbols(symList,words)

def checkIdentifierInitialization(identifier, sentence):

	search("public", sentence)

	"""if search("public", sentence) == search("void", sentence):# or search("declaration", sentence) == search(identifier, sentence):
		print("exists")
		return True
	else:
		print("dne")
		return False"""

def hash(key, M, iType):

	print(key)
		# Compute hash for key[0..M-1].
	h = 0

	if (iType == "pattern"):
		for j in range (M):
			print(R, h, key[j], Q)
			h = (R * h + ord(key[j])) % Q
			print (h)

	elif (iType == "text"):
		for k in range(len(key)):
			for l in range(len(key[k])):
				chars.append(key[k][l])

		for j in range (M):
			print(R, h, chars[j], Q)
			h = (R * h + ord(chars[j])) % Q
			print (h)

	"""else:
		for j in range (M):
			print(key[j])
			g = key[j]
			print(g[0])
			for i in range (len(key[j])):
				chars.append(key[j][i])
				print(R, h, key[j][i], Q)
				h = (R * h + ord(key[j][i])) % Q
				print (h)"""
	return h

def search(pattern, txt):
	M = len(pattern)
	#Q = random.getrandbits(16)
	print("Q: ", Q)
	RM = 1

	print(M)
	for i in range(M):
		RM = (R * RM) % Q
		print(RM)
	print("here")
	patHash = hash(pattern, M, "pattern")
	print("here3")

	N = len(txt)
	print(len(txt))
	print("pathash: " , patHash)

	txtHash = hash(txt, M, "text")
	if (patHash == txtHash):
		print ("d0ne")
		return 0

	print("here39", M, N)
	for i in range (M-1, len(chars)):

		print(i-M+1, i-4, "word to check: ", chars[i-M+1], chars[i-4], chars[i-3], chars[i-2], chars[i-1], chars[i])
		
		#print(txtHash + Q - RM*ord(chars[i-M]) , Q)
		#Remove leading digit, add trailing digit, check for match.
		txtHash = (txtHash + Q - RM*ord(chars[i-M]) % Q) % Q
		#print(txtHash)
		txtHash = (txtHash*R + ord(chars[i])) % Q
		print("checking...", txtHash, "patt: ", patHash)
		if (patHash == txtHash):
			#if (check(i - M + 1)):
			print("don3")
			return i - M + 1; # match
	return -1

if __name__ == "__main__": main()