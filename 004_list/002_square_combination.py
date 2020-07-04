squares_comb = [(x, x**2) for x in range(10)]
squares_lambda = list(map(lambda x: (x, x**2), range(10)))

print("Printing combination using for loop: ")
print(squares_comb)

print("\nPrinting combination using lambda functions: ")
print(squares_lambda)