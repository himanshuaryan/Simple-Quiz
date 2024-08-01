print("code by @himanshuaryan".center(110))
n = int(input("Enter number : "))
print(" ")
table = [x for x in range(1,n+1)]
print("The cube of first nth numbers are : \n")
for x in table:
    print(f"\t{x} * {x} = {x**3}")
