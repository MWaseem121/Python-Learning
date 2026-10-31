print("...Multiplication Table Generator...")

number = int(input("Enter the number: "))
print("Number:", number )

for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")