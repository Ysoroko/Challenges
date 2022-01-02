import sys
import re

# Types 
# M: method
# C: class
# V: variable
# ----------------------------------------------------
def t_method(lst_to_format):
    print(lst_to_format[0], end = "")
    if len(lst_to_format) > 1:
        for i in range(1, len(lst_to_format)):
            print(lst_to_format[i].capitalize(), end="")
    print("()")

def t_class(lst_to_format):
    for elem in lst_to_format:
        print(elem.capitalize(), end="")
    print("")

def t_variable(lst_to_format):
    print(lst_to_format[0], end = "")
    if len(lst_to_format) > 1:
        for i in range(1, len(lst_to_format)):
            print(lst_to_format[i].capitalize(), end="")
    print("")

def print_first_elem(string):
    first = ""
    for i, letter in enumerate(string):
        if letter.isupper():
            break
        first += letter
    print(first, end = " ") if first else print("", end ="")
    
# Operation:
# S: split 
# C: combine
# ----------------------------------------------------
def op_split(strin, typ):
    string = strin.strip('()')
    print_first_elem(string)
    l = re.findall('[A-Z][^A-Z]*', string) # find any string starting with a capital letter
    for elem in l:
        print(elem.lower(), end = " ")
    print("")
    
def op_combine(string, typ):
    to_format = string.split()
    types[typ](to_format)

# Dictionnaries of functions
operations = {
    'S': op_split,
    'C': op_combine
}

types = {
    'M': t_method,
    'C': t_class,
    'V': t_variable
}


def apply_format(lst):
    operation = lst[0]
    typ = lst[1]
    to_format = lst[2].strip()
    operations[operation](to_format, typ)
    

if __name__ == "__main__":
    for line in sys.stdin:
        line.strip()
        l = line.split(";")
        apply_format(l)