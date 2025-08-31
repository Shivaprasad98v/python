import math

def evaluate_functions (x):
    f = math.cos (2 * x)
    f_1 = -2 * math.sin (2 * x)
    f_2 = -4 * math.cos (2 * x)
    return f, f_1, f_2
x = math.pi
result = evaluate_functions (x)
print ("f(x): ", result[0])
print ("f_1(x): ", result[1])
print ("f_2(x): ", result[2])
