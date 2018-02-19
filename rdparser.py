
#Java grammar for simple Java programs consisting of only a main method and print statement which prints a String

#PROG --> (IMPORTS identifier)* CLASS_DECLARATION
#CLASS_DECLARATION --> 'public class' identifier '{' MAIN_METHOD_DECLARATION '}'
#MAIN_METHOD_DECLARATION --> 'public static void main (String[] args) {' METHOD_BODY '}'
#METHOD_BODY --> PRINT_STATEMENT '(' STRING ')'
#STRING --> \" . \"