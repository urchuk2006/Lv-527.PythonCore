n1 = input("Input 4 digits number: ")
count = 1
for x in n1:
    count *= int(x)

print("The summ is:", count)

y = str(n1)
z = y[::-1]

print("Reversed number: ", z)

print("List of sorted elements: ", sorted(y))
