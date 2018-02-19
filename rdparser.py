
#Java grammar for simple Java programs consisting of only a main method and print statement which prints a String

#PROG --> (IMPORTS identifier)* CLASS_DECLARATION
#IMPORTS --> 
#CLASS_DECLARATION --> 'public class' IDENTIFIER '{' MAIN_METHOD_DECLARATION '}'
#MAIN_METHOD_DECLARATION --> 'public static void main (String[] args) {' METHOD_BODY '}'
#METHOD_BODY --> PRINT_STATEMENT '(' STRING ')'
#STRING --> \" . \"
#IDENTIFIER --> [a-zA-Z]+

currentPosition = 0;

def main():
    sentence = sys.argv[1]
    try:
       prog(sentence);
    except:
        print("Error")

def prog(sentence):
    if(currentPosition == 0):
        if (sentence[0] == 'import'):
            imports(sentence)
        elif (sentence[0] == 'public'):
            class_declaration(sentence)
        else:
            #FAIL

def class_declaration(sentence)
    if (sentence[currentPosition] == 'public'):
        currentPosition+=1
        if (sentence[currentPosition] == 'class'):
            currentPosition+=1
            if (sentence[currentPosition] == 'class'):
                currentPosition+=1
                identifier(sentence)
                if (sentence[currentPosition] == '{'):
                    main_method_declaration(sentence)
                    if (sentence[currentPosition] == '}'):
                        return True

def main_method_declaration(sentence)
    if (sentence[currentPosition] == 'public'):
        currentPosition+=1
        if (sentence[currentPosition] == 'static'):
            currentPosition+=1
            if (sentence[currentPosition] == 'void'):
                currentPosition+=1
                if (sentence[currentPosition] == 'main'):
                    currentPosition+=1
                    if (sentence[currentPosition] == '('):
                        currentPosition+=1
                        if (sentence[currentPosition] == 'String'):
                            currentPosition+=1
                            if (sentence[currentPosition] == '[]'):
                                currentPosition+=1
                                if (sentence[currentPosition] == 'args'):
                                    currentPosition+=1
                                    if (sentence[currentPosition] == ')'):
                                        currentPosition+=1
                                        if (sentence[currentPosition] == '{'):
                                            currentPosition+=1
                                            method_body(sentence)
                                            if (sentence[currentPosition] == '}'):
                                                return True

def method_body()
    print_statement(sentence)
        if (sentence[currentPosition] == '('):
            currentPosition+=1
            string(sentence)
            if (sentence[currentPosition] == ')'):
                currentPosition+=1
                return True
