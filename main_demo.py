a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]

fruits, quantities = zip(*a)

print(f"Fruits: {fruits}")
print(f"Quantities: {quantities}")