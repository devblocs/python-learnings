first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number < second_number:
    print(f"Number '{first_number}' is less than '{second_number}'")
elif first_number == 0 and second_number == 0:
    print("Both the numbers are 0")
else:
    print(f"Number '{first_number}' is greater than '{second_number}'")