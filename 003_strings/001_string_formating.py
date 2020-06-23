name = "John"
c = 3-5j

# concatenating strings using glueing technique
imaginary_print = ('The complex number {0} is formed from the real part {0.real} ' 'and the imaginary part {0.imag}.').format(c)

print("Different ways to print output to screen:")
print("1) Using format method: ")
print("Hello {0}".format(name))
print("Hello {}".format(name))
print("Hello {thisName}".format(thisName = name))
print("Hello {name}".format(**{'name' : name}))
print("Hello {0!r}".format(*[name]))
print(imaginary_print)

print("\n2) Using format literal:")
print(f"Hello {name!r}")

print("\n3) Using raw string:")
print(r"Hello \t {name}")

print("\n4) Using concatenation:")
print("Hello " + str(name))

print("\n5) Using % operator:")
print("Hello %(name)s"%{"name" : name})