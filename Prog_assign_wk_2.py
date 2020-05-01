"""
CTEC 121
Brandon Norton
Programming assingment wk2
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
   
# 1. Assignment Statements
    Number = 15.6
    number = 5
    print("The answer is", Number + number)

# 2. end/sep
    print("hi", end=" " )
    print("there!")
    print("There","are","underscores!", sep="_")

# 3. Tab quote backslash
    print("hello\t...")

# 4. Input
    '''
    name = input("Please type your name.")
    print(name)
    '''

# 5. Simultaneous Assignment
    '''
    x, y = 7+12, 9-8
    print(x, y)
    print()
    a, b = eval(input("please enter 2 numbers with a comma between."))
    print(a, b)
    print()
    '''
# 6. Integer Arithmetic 
    print(5/2)
    print(5//2)

# 7. Definite loops
    '''
    for i in range(10):
        print(i)
    
    for j in range(11,26,3):
        print(j)
    '''
# 8. Math Functions
import math
d = 4.25
print(math.pi)
print(math.sqrt(d))
print(math.ceil(d))
print(math.floor(d))
print(math.pow(d,2))
print(math.pow(d,3))

main()    