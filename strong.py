import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    A strong number is a number whose sum of the factorial of its digits is equal to the number itself.
    """
    if num < 0:
        return False
    
    original_num = num
    sum_of_factorials = 0
    
    while num > 0:
        digit = num % 10  # Extract the last digit
        sum_of_factorials += math.factorial(digit)  # Add factorial of the digit to the sum
        num //= 10  # Remove the last digit
        
    return sum_of_factorials == original_num

print("Strong numbers from 1 to 5000:")
for i in range(1, 5001):
    if is_strong_number(i):
        print(i)