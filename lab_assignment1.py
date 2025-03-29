#                QUESTION 1

for num in range(2, 21, 2):
    print(num)

#                QUESTION 2

names = ['james', 'hulia', 'javi']

for name in names:
   print(name.upper())

#                QUESTION 3

for num in range(10, 0, -1):
    print(num)

#                QUESTION 4 

numbers = [10, 15, 21, 33, 42, 55, 60, 77, 81]

for num in numbers:
    if num % 3 == 0:
        print(num)

#                QUESTION 5

for num in range(1, 11):
    print(f"square of {num} is {num**2}")

#                QUESTION 6

celsius_temps = [0, 10, 20, 30, 40, 100]

for temp in celsius_temps:
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit}°F")

#               QUESTION 7

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

#               QUESTION 8

numbers = [3, 7, 12, 18, 25]

total_sum = 0  

for num in numbers:
    total_sum += num  

print(f"Sum of all numbers: {total_sum}")

#               QUESTION 9

text = "Hello"

for char in text:
    print(char)

#               QUESTION 10

words = ["apple", "banana", "cherry", "kiwi", "strawberry", "grape"]

for word in words:
    if len(word) > 5:
        print(word)


