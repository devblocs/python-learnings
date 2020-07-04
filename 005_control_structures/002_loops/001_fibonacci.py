num1, num2  = 0, 1

while num1 < 10:
    print(num1, end=", ")
    num1, num2 = num2, num1 + num2
print(f"\nNumber 1 : {num1}")
print(f"Number 2 : {num2}")