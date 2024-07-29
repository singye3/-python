def power_of(n):
    def power(x):
        return x**n
    return power

square = power_of(2)
cube = power_of(3)

print(square(3))
print(cube(3))