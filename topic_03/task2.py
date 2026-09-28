# Початковий список
numbers = [3, 1, 4]
print("Початковий список:", numbers)

numbers.append(5)
print("Після append(5):", numbers)

numbers.extend([9, 2])
print("Після extend([9, 2]):", numbers)

numbers.insert(1, 10)
print("Після insert(1, 10):", numbers)

numbers.remove(10)
print("Після remove(10):", numbers)

numbers.sort()
print("Після sort():", numbers)

numbers.reverse()
print("Після reverse():", numbers)

numbers_copy = numbers.copy()
print("Копія списку:", numbers_copy)

numbers.clear()
print("Після clear():", numbers)