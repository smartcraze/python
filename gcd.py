'''
a=int(input("Enter the Value of a: "))
b=int(input("Enter the value of b: "))
while b:
    a=b                                                # use the tuple assignment to swap the variable a,b  
    b=a%b                                              # using Euclidean algorithm  
print(a)
'''

a = int(input("Enter the Value of a: "))
b = int(input("Enter the value of b: "))

while b:
    a, b = b, a % b  # Swap a and b and calculate the remainder
print("The GCD of a and b is:", a)
