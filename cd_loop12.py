
# Reading input
number = int(input().strip())

even_digits = []
odd_digits = []

num_str = str(number)

for digit_char in num_str:
    digit = int(digit_char)
    if digit % 2 == 0:
        even_digits.append(digit)
    else:
        odd_digits.append(digit)

even_digits.sort()
odd_digits.sort()


# Print even digits
if even_digits:
    print(*even_digits)
else:
    print("None")

# Print odd digits
if odd_digits:
    print(*odd_digits)
else:
    print("None")




"""Write a code get an integer number as input and print the odd and even digits of the number separately.

Input Description:
A single line containing an integer.

Output Description:
Print the even and odd integers of the integer in a separate line.

Sample Input :
1234

Sample Output :
2 4
1 3"""
