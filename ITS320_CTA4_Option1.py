Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> amounts = int(input('Enter five floating-point values:\n'))

for number in range(0, len(amounts)):
    total += amounts(number)
print('The total is', total)

average = total / len(amounts)
print('The average is', average)

maximum = max(amounts)
print('The highest value is', maximum)

minimum = min(amounts)
print('The lowest value is', minimum)

for number in amounts:
    amounts_with_interest.append(number * 1.2)
print('Original values with 20% interest are', amounts_with_interest)
