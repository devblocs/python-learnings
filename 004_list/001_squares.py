# using the lambda expression to append squares

squares_lambda = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

print("Print lambda processes square numbers: ")
print(squares_lambda)

print("\nPrint square numbers using for loops: ")
print(squares)