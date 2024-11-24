# Custom exception to handle invalid input for Fibonacci sequence
class OutOfMagnitudeException(Exception):
    pass

# Function to compute the nth Fibonacci number using recursion
def fibonnaci(n):
    # Check for invalid input and raise an exception if n is negative
    if n < 0:
        raise OutOfMagnitudeException  # Raise custom exception

    # Base cases: return n for the first two Fibonacci numbers (0 and 1)
    if n == 1 or n == 0:
        return n

    # Special case: explicitly return 1 for the second Fibonacci number
    if n == 2:
        return 1

    # Recursive case: calculate Fibonacci as the sum of the previous two numbers
    return fibonnaci(n-1) + fibonnaci(n-2)



# Function to compute the greatest common divisor (GCD) of two numbers using subtraction
def gcd(a, b):
    # Base case: If one number is 0, return the other number
    if a == 0:
        return b
    if b == 0:
        return a

    # Base case: If both numbers are equal, return one of them
    if a == b:
        return a

    # Recursive case: Subtract the smaller number from the larger one
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)




# Function to compare two strings lexicographically
def compareTo(s1, s2):
    # Base case: both strings are empty, they are equal
    if s1 == "" and s2 == "":
        return 0

    # Base case: one string is empty
    if s1 == "":
        return -1  # s1 is less than s2
    if s2 == "":
        return 1  # s1 is greater than s2

    # Compare the first character of each string
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])  # Return difference in ASCII values

    # Recursive case: compare the rest of the strings
    return compareTo(s1[1:], s2[1:])

# Example usage: compare strings and print results
print(compareTo("apple", "banana"))  # Output: Negative number ("apple" < "banana")
print(compareTo("grape", "grape"))   # Output: 0 ("grape" == "grape")
print(compareTo("zebra", "ant"))     # Output: Positive number ("zebra" > "ant")


print(f"Fibonacci(0): {fibonnaci(0)}")  # Output: 0
print(f"Fibonacci(1): {fibonnaci(1)}")  # Output: 1
print(f"Fibonacci(5): {fibonnaci(5)}")  # Output: 5 (Sequence: 0, 1, 1, 2, 3, 5)
print(f"Fibonacci(7): {fibonnaci(7)}")  # Output: 13 (Sequence: 0, 1, 1, 2, 3, 5, 8, 13)

# Example 5: Invalid input for Fibonacci
try:
    print(f"Fibonacci(-3): {fibonnaci(-3)}")  # This will raise OutOfMagnitudeException
except OutOfMagnitudeException:
    print("Error: Negative input is not allowed for Fibonacci sequence.")

print("GDC: ", gcd(100, 125))  # Output: GDC: 25
print("GDC: ", gcd(0, 15))  # Output: GDC: 15
print("GDC: ", gcd(25, 0))  # Output: GDC: 25
print("GDC: ", gcd(10, 10))  # Output: GDC: 10
print("GDC: ", gcd(13, 17))  # Output: GDC: 1
print("GDC: ", gcd(81, 153))  # Output: GDC: 9
print("GDC: ", gcd(0, 0))  # Output: GDC: 0

