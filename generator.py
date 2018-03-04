#Take input Java sentence, generate ARM code, and write to OUT.txt

import sys

currentPosition = 0;

def main():

    inputTest = sys.argv[1]

    #Generate appropriate ARM code
    if inputTest == "MainSym":
    	try:
      		generateMain()
    	except:
        	print("Error")

#Append ARM equivalent code to OUT.txt
def generateMain():
	with open('OUT.txt', 'a') as _file:
    		_file.write('.text\n')
    		_file.write('.global main\n')
    		_file.write('.main:\n')

if __name__ == "__main__": main()