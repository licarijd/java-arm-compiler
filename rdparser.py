#PROG --> IMPORTS* CLASS_DECLARATION
#IMPORTS --> 'import' IDENTIFIER
#CLASS_DECLARATION --> 'public class' IDENTIFIER '{' MAIN_METHOD_DECLARATION '}'
#MAIN_METHOD_DECLARATION --> 'public \. static \. void \. main (String[] args) {' METHOD_BODY '}'
#METHOD_BODY --> PRINT_STATEMENT | EXIT_STATEMENT | ARITHMETIC_STATEMENT
#PRINT_STATEMENT --> 'System.out.println(' ( IDENTIFIER ' ' \+ )+ ';'
#ARITHMETIC_STATEMENT --> 'System.out.println(' ( IDENTIFIER ' ' \+ )+ ';'
#EXIT_STATEMENT --> 'System.exit(0)' ';'
#IDENTIFIER --> [a-zA-Z]+
import sys
import generator as CG
import scanner as SC
import random

currentPosition = 0;

#search variables
patHash = 0; #pattern hash value
txtHash = 0
M = 0; #pattern length
Q = random.getrandbits(128); #a large prime
R = 256; #alphabet size
RM = 0; #R^(M-1) % Q

def main():
    sentence = sys.argv[1]

    #scan input
    with open(sys.argv[1], "r") as word_list:
        sentence = word_list.read().split()

    #Remove comments, tabs, spaces, and newlines
    for i in range(len(sentence)-1):

        #Remove whitespace
        if sentence[i] == ' ' or sentence[i] == '\t' or sentence[i] == '\n':
            del sentence[i]
    
    try:
        checkIdentifierInitialization("test", sentence)
        CG.genProgEntry()
        print("gen prog entry complete")
        prog(sentence);
    except:
        print("Error")

def prog(sentence):
    if(currentPosition == 0):
        #if (sentence[0] == 'import'):
            #imports(sentence)
        #elif (sentence[0] == 'public'):
        if (sentence[0] == 'PublicSym'):
            class_declaration(sentence)
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def class_declaration(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'PublicSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'ClassSym'):
            currentPosition+=1
            if (sentence[currentPosition] == 'IdentSym'):
                currentPosition+=1
                #identifier(sentence)
                if (sentence[currentPosition] == 'LCurlSym'):
                    currentPosition+=1
                    main_method_declaration(sentence)
                    if (sentence[currentPosition] == 'RCurlSym'):
                        currentPosition+=1
                        return True
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def main_method_declaration(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'PublicSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'StaticSym'):
            currentPosition+=1
            if (sentence[currentPosition] == 'VoidSym'):
                currentPosition+=1
                if (sentence[currentPosition] == 'MainSym'):
                    currentPosition+=1
                    if (sentence[currentPosition] == 'LparenSym'):
                        currentPosition+=1
                        if (sentence[currentPosition] == 'StringSym'):
                            currentPosition+=1
                            if (sentence[currentPosition] == 'ArraySym'):
                                currentPosition+=1
                                if (sentence[currentPosition] == 'ArgsSym'):
                                    currentPosition+=1
                                    if (sentence[currentPosition] == 'RparenSym'):
                                        currentPosition+=1
                                        if (sentence[currentPosition] == 'LCurlSym'):
                                            currentPosition+=1
                                            method_body(sentence)
                                            if (sentence[currentPosition] == 'RCurlSym'):
                                                currentPosition+=1
                                                return True
                                            else:
                                                terminate(False, sentence[currentPosition])
                                        else:
                                            terminate(False, sentence[currentPosition])
                                    else:
                                        terminate(False, sentence[currentPosition])
                                else:
                                    terminate(False, sentence[currentPosition])
                            else:
                                terminate(False, sentence[currentPosition])
                        else:
                            terminate(False, sentence[currentPosition])
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

                                    
#Only handle print statements and exit statements
def method_body(sentence):
    global currentPosition

    if (currentPosition < len(sentence)):
        if (sentence[currentPosition] == 'SystemSym') and (sentence[currentPosition+2] == 'OutSym'):
            print_statement(sentence)
            return True
        elif (sentence[currentPosition] == 'SystemSym') and (sentence[currentPosition+2] == 'ExitSym'):
            end_prog(sentence)
            return True
    else:
        terminate(True, sentence)
        

def print_statement(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'SystemSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'PeriodSym'):
            currentPosition+=1
            if (sentence[currentPosition] == 'OutSym'):
                currentPosition+=1
                if (sentence[currentPosition] == 'PeriodSym'):
                    currentPosition+=1
                    if (sentence[currentPosition] == 'PrintSym'):
                        currentPosition+=1
                        if (sentence[currentPosition] == 'LparenSym'):
                            currentPosition+=1

                            #Java lets you print a string of identifiers
                            while (sentence[currentPosition] == 'IdentSym'):
                                currentPosition+=1
                            if (sentence[currentPosition] == 'RparenSym'):
                                currentPosition+=1
                                if (sentence[currentPosition] == 'SemicolonSym'):
                                    currentPosition+=1
                                    print("ttt")
                                    print(SC.args)
                                    CG.genPrintStatement(SC.args)
                                    #terminate(True, sentence)
                                    method_body(sentence)
                                else:
                                    terminate(False, sentence[currentPosition])
                            else:
                                terminate(False, sentence[currentPosition])
                        else:
                            terminate(False, sentence[currentPosition])
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def checkIdentifierInitialization(identifier, sentence):

    if search("public", sentence) == search("void", sentence):# or search("declaration", sentence) == search(identifier, sentence):
        print("exists")
        return True
    else:
        print("dne")
        return False
   


def hash(key, M):

    print(key)
     # Compute hash for key[0..M-1].
    h = 0
    for j in range (M):
        print(R, h, key[j], Q)
        h = (R * h + ord(key[j])) % Q
        print (h)
    return h

def search(pattern, sentence):
    M = len(pattern)
    Q = random.getrandbits(128)
    RM = 1
    
    print(M)
    for i in range(M):
        RM = (R * RM) % Q
        print(RM)
    print("here")
    patHash = hash(pattern, M)
    print("here3")

    N = len(sentence)
    print(sentence)
    txtHash = hash(sentence, M)
    if (patHash == txtHash):
        print ("d0ne")
        return 0

    print("here3")
    for i in range (M, N):
        #Remove leading digit, add trailing digit, check for match.
        txtHash = (txtHash + Q - RM*txt.charAt(i-M) % Q) % Q
        txtHash = (txtHash*R + txt.charAt(i)) % Q
        if (patHash == txtHash):
            #if (check(i - M + 1)):
            return i - M + 1; # match
    return -1

def end_prog(sentence):
    global currentPosition
    print("endprog")
    if (sentence[currentPosition] == 'SystemSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'PeriodSym'):
            currentPosition+=1
            if (sentence[currentPosition] == 'ExitSym'):
                currentPosition+=1
                if (sentence[currentPosition] == 'LparenSym'):
                    currentPosition+=1
                    if (sentence[currentPosition] == 'IdentSym'):
                        currentPosition+=1
                        if (sentence[currentPosition] == 'RparenSym'):
                            currentPosition+=1
                            if (sentence[currentPosition] == 'SemicolonSym'):
                                currentPosition+=1
                                CG.genProgExit()
                                print("gen prog exit complete")
                                CG.genProgram()
                                #terminate(True, sentence)
                                method_body(sentence)
                            else:
                                terminate(False, sentence[currentPosition])
                        else:
                            terminate(False, sentence[currentPosition])
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])
        
def identifier():
    print "incomplete"

def terminate(res, current):
    global currentPosition

    if res:
        # sys.stdout.write("accepted: %s " % current);
        print("gen prog exit begin")
    else:
        sys.stdout.write("rejected: %s " % current);
        sys.exit();
   
if __name__ == "__main__": main()
