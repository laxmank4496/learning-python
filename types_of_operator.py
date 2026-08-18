# Program to demonstrate different types of operators

a = 10
b = 3

# 1. Arithmetic Operators
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# 2. Assignment Operators
print("\nAssignment Operators:")
x = 10
x += 5
print("x += 5:", x)
x -= 2
print("x -= 2:", x)
x *= 2
print("x *= 2:", x)
x /= 2
print("x /= 2:", x)

# 3. Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# 4. Logical Operators
print("\nLogical Operators:")
print("(a > 5) and (b < 5):", (a > 5) and (b < 5))
print("(a > 5) or (b > 5):", (a > 5) or (b > 5))
print("not(a > 5):", not(a > 5))

# 5. Membership Operators
print("\nMembership Operators:")
numbers = [1, 2, 3, 4, 5]
print("3 in numbers:", 3 in numbers)
print("10 not in numbers:", 10 not in numbers)

# 6. Identity Operators
print("\nIdentity Operators:")
p = numbers
q = numbers
print("p is q:", p is q)
print("p is not q:", p is not q)

# 7. Bitwise Operators
print("\nBitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)