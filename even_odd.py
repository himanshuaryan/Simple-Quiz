# Find the sum of first n even and odd natural numbers.
n = int(input("Enter number : ")) + 1
sum_odd = 0
sum_even = 0
for x in range(0,n):
    if (x % 2) == 0:
        sum_even += x
    elif (x % 2) == 1:
        sum_odd += x
        
print("\nSum of odd no. : ", sum_odd)
print("Sum of even no. : ", sum_even)
