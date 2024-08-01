print("code by @himanshuaryan".center(110))
n = int(input("Enter number : "))
print(" ")
table = [x for x in range(1,n+1)]
for x in table:
    print(f"{x} * {x} = {x**2}")
