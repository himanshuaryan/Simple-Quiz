'''
define function to find the hcf between two numbers.
a = first number
b = second numver
'''
def hcf(a = 18, b = 15):
    while True:
        if b == 0:
            return a    
        else:
            return hcf(b, a%b)
            
a = int(input("\n First number : "))
b = int(input("Second number : "))
HCF = hcf(a,b)
lcm = (a*b)/HCF
print(f"\nLCM of {a} and {b} is  {lcm}.")