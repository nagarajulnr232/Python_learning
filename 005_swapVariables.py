a = 25
b = -14
def swap_XOR(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
def swap_With_Temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b
def swap_Addition(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
def swap_Subtraction(a, b):
    b = b - a
    a = a + b
    b = a - b
    return a, b
print("Using XOR : ",swap_XOR(a, b))
print("using temp : " ,swap_With_Temp(a, b))
print("using Addition operator : ",swap_Addition(a, b))
print("using Substarction operator : ",swap_Subtraction(a, b))

