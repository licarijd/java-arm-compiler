import sys;

sentenceLength = 0;
currentPosition = 0;

def main():

    global currentPosition;
    sentenceInput = raw_input("Please enter a sentence ");
    input = list(sentenceInput);
    try:
        sentenceLength = len(input);
	Q(input, sentenceLength);
	terminate(True, currentPosition);
    except:
    	terminate(False, currentPosition);

def Q(input, sentenceLength):
    global currentPosition;
    if currentPosition <= sentenceLength:
        if input[currentPosition] == "w" and currentPosition==0:
            currentPosition+=1;
            if input[currentPosition] == "(":
		currentPosition+=1;
		E(input, sentenceLength);
		if input[currentPosition] == ")":    
		    currentPosition+=1;
		    if input[currentPosition] == "{":
			currentPosition+=1;
                        if input[currentPosition] == "}":
                            currentPosition+=1;
                            return True;
                        else:
                            S(input, sentenceLength);
			    if input[currentPosition] == "}":
                            	currentPosition+=1;
                            	return True; 
			    else: 
			    	Q(input, sentenceLength);	                         
                    else:
                        terminate(False, currentPosition);
                   
                else:
                    terminate(False, currentPosition);
               
            else:
                terminate(False, currentPosition);
           
        elif (currentPosition>0):
	    S(input, sentenceLength);
	    if input[currentPosition] == "}":
                currentPosition+=1;
                return True; 
	    else: 
		Q(input, sentenceLength);		

	else:
            terminate(False, currentPosition);
       
    else:
        terminate(False, currentPosition);
   

def E(input, sentenceLength):

    global currentPosition;
    if currentPosition <= sentenceLength:
        if input[currentPosition] == "(":
            currentPosition+=1;
            E(input, sentenceLength);

            if input[currentPosition] == ")":
                currentPosition+=1;
                return True;
            else:
                terminate(False, currentPosition);
           
       
        elif input[currentPosition] == "t" or input[currentPosition] == "f":

            B(input, sentenceLength);
            if input[currentPosition] == "|" or input[currentPosition] == "&":

                currentPosition+=1;
                B(input, sentenceLength);
            else:
                terminate(False, currentPosition);
           
        else:
            N(input, sentenceLength);   
	    if input[currentPosition] == "+" or input[currentPosition] == "-":

                currentPosition+=1;
                N(input, sentenceLength);
            else:
                terminate(False, currentPosition);
        
       
    else:
        terminate(False, currentPosition);
   

def S(input, sentenceLength):
    
    global currentPosition;
    if currentPosition <= sentenceLength:
        V(input, sentenceLength);
        if input[currentPosition] == "=":
            currentPosition+=1;
            E(input, sentenceLength);
            if input[currentPosition] == ";":
		currentPosition+=1;
                return True;
            else:
                terminate(False, currentPosition);
           
        else:
            terminate(False, currentPosition);
       
    else:
        terminate(False, currentPosition);
   

def V(input, sentenceLength):

    global currentPosition;
    if currentPosition <= sentenceLength:
	I(input, sentenceLength);
    	if input[currentPosition] == "[":
           	currentPosition+=1;
           	E(input, sentenceLength);
           	if input[currentPosition] == "]":
                 	currentPosition+=1;
                 	return True;
           	else:
                 	terminate(False, currentPosition);
               
     	else:
           	return True;
           
       
    else:
        terminate(False, currentPosition);
   

def I(input, sentenceLength):

    global currentPosition;
    if currentPosition <= sentenceLength:
        if input[currentPosition] == "a" or input[currentPosition] == "b" or input[currentPosition] == "c" or input[currentPosition] == "d" or input[currentPosition] == "e":
	    
            L(input, sentenceLength);
	    I(input, sentenceLength);
        else:
            return True;
       
    else:
        terminate(False, currentPosition);

def D(input, sentenceLength):

    global currentPosition;
    if currentPosition <= sentenceLength:
        if input[currentPosition] == "0" or input[currentPosition] == "1" or input[currentPosition] == "2" or input[currentPosition] == "3" or input[currentPosition] == "4" or input[currentPosition] == "5" or input[currentPosition] == "6" or input[currentPosition] == "7" or input[currentPosition] == "8" or input[currentPosition] == "9":
            currentPosition+=1;
            return True;
        else:
            terminate(False, currentPosition);
       
    else:
        terminate(False, currentPosition);
        

def L(input, sentenceLength):

    global currentPosition;
    if currentPosition <= sentenceLength:
        if input[currentPosition] == "a" or input[currentPosition] == "b" or input[currentPosition] == "c" or input[currentPosition] == "d" or input[currentPosition] == "e":
            currentPosition+=1;
            return True;
        else:
            terminate(False, currentPosition);
       
    else:
        terminate(False, currentPosition);
        

def B(input, sentenceLength):

    global currentPosition;
    if currentPosition <= sentenceLength:
        if input[currentPosition] == "t" or input[currentPosition] == "f":
            currentPosition+=1;
            return True;
        else:
            terminate(False, currentPosition);
       
    else:
        terminate(False, currentPosition);
        
def N(input, sentenceLength):
    global currentPosition;
    if currentPosition <= sentenceLength:
	D(input, sentenceLength);
        if input[currentPosition] == "0" or input[currentPosition] == "1" or input[currentPosition] == "2" or input[currentPosition] == "3" or input[currentPosition] == "4" or input[currentPosition] == "5" or input[currentPosition] == "6" or input[currentPosition] == "7" or input[currentPosition] == "8" or input[currentPosition] == "9":
	    
            
	    N(input, sentenceLength);
        else:
	    
            return True;
       
    else:
        terminate(False, currentPosition);
   

def terminate(res, current):
    if res:
        sys.stdout.write("accepted\n");
    else:
        sys.stdout.write("rejected\n");
	sys.exit();
   
if __name__ == "__main__": main()