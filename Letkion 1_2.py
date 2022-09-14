
for number in range (1, 21):
    print(number)


#even numbers
for number in range (1, 21):
    if number % 2 == 0:
        print(number)


#odd numbers
for number in range (1, 21):
    if number % 2 == 1:
        print(number)

#ask the user for 2 numbers
numb_1 = int(input("Write the first number: "))
numb_2 = int(input("Write the second number: "))

# Write "bigger" if 2nd number is bigger
if numb_2 > numb_1:
    print("Bigger")
# Write "smaller" if 2nd number is smaller
elif numb_2 < numb_1:
    print("Smaller")
else:
    print("Same number")





