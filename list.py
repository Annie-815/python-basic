#print largest number in  a list
numbers = [11, 32, 54, 3, 61, 18, 21]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
numbers.append(11)
numbers.insert(2,98)
print(numbers)
