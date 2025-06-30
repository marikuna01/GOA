num = int(input("Enter a number (0 to stop): "))
total = num

while num != 0:
    num = int(input("Enter a number (0 to stop): "))
    total += num

print("The total sum is:", total)