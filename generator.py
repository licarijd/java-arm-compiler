# dictionaries of available registers, initialize all values to null

# all purpose registers, R0 - R12
regs = {"R0" : None, 
        "R1" : None,
        "R2" : None,
        "R3" : None,
        "R4" : None,
        "R5" : None,
        "R6" : None,
        "R7" : None,
        "R8" : None,
        "R9" : None,
        "R10" : None,
        "R11" : None,
        "R12" : None,}

# other available registers
SP = {"R13" : None} # stack pointer
LR = {"R14" : None} # link register
PC = {"R15" : None} # program counter

# instructions
MOV = 1; LDR = 2; SWI = 3;

main = "" # instructions from main body
data = "" # data segment for strings
program = "" # full ARM code
counter = 0 # for naming new strings
ARM = open("ARM.out", "w") # write output to file

def putLabel(label, section):
    """ adds labels for new sections """
    if section == "m":
        progam += label + "\n"
    else if section == "d":
        data += label + "\n"

def putInstruction(instruction, arg1, arg2):
    """ adds instructions with proper indenting """
    if instruction == MOV:
        main += "\t" + "MOV " + arg1 + ", " + "#" + str(arg2) + "\n"
        regs[arg1] = arg2
    else if instruction == LDR:
        main += "\t" + "LDR " + arg1 + ", " + "=" + "string" + str(counter) + "\n"
    else if instruction == SWI:
        main += "\t" + "SWI " + arg1 + "\n"

def genPrintStatement(string):
    """ generates arm code for print statements. the size of the string 
    and the string itself are loaded into registers and then a software
    interrupt is called which performs a system call to print the string """
    size = len(string.encode('utf-8')) # get the size of the string in bytes
    putInstruction(MOV, "R2", size)
    putInstruction(LDR, "R1", None)
    putInstruction(SWI, "0", None)
    regs["R1"] = string
    data += "string" + str(counter) + ":\n"
    data += "\t" + ".ascii " + "\"" + string + "\"" + "\n"
    counter += 1

def genProgEntry():
    """ initial lines of ARM code which lead to program entry, flags are 
    set in registers R0 and R7 so that software interrupts trigger prints"""
    putLabel(".global main", "m")
    putLabel("main", "m")
    putLabel(".data", "d")
    putInstruction(MOV, "R7", 4)
    putInstruction(MOV, "R0", 1) # setting these registers prepares the os for printing

def genProgExit():
    """ set the flag in R7 so that software interrupts now triggers system exit """
    putInstruction(MOV, "R7", 1)
    putInstruction(SWI, "0", None)

def genProgram():
    """ if the program succesfully parses, combine the main program and data
    section to make the full ARM program """
    program = main + data
    ARM.write(program)

