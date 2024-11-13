# operator_precedence.py
# This program demonstrates the precedence and associativity of a comprehensive list of operators in Python.

print("Demonstrating Precedence and Associativity of Various Operators:\n")

# 1. Parentheses `()`
print("Parentheses:")
# Parentheses have the highest precedence, so expressions inside them are evaluated first.
result = (5 + 3) * 2
print("(5 + 3) * 2 =", result)  # Expected: 16

print("\n")

# 2. Exponentiation `**`
print("Exponentiation:")
# Exponentiation has right-to-left associativity
result = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result)  # Expected: 512

print("\n")

# 3. Unary Plus, Unary Minus, and Bitwise NOT `+`, `-`, `~`
print("Unary Plus, Unary Minus, and Bitwise NOT:")
result = -3 + +2  # Unary minus and unary plus
print("-3 + +2 =", result)  # Expected: -1

result = ~5  # Bitwise NOT
print("~5 =", result)  # Expected: -6 (bitwise NOT of 5 flips all bits, resulting in -6)

print("\n")

# 4. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
print("Multiplication, Division, Floor Division, and Modulus:")
result = 10 * 2 // 3 % 4
print("10 * 2 // 3 % 4 =", result)  # Expected: ((10 * 2) // 3) % 4 = 2

print("\n")

# 5. Addition `+` and Subtraction `-`
print("Addition and Subtraction:")
result = 5 + 3 - 2
print("5 + 3 - 2 =", result)  # Expected: 6

print("\n")

# 6. Bitwise Left Shift `<<` and Bitwise Right Shift `>>`
print("Bitwise Left Shift and Right Shift:")
result = 8 >> 2 << 1
print("8 >> 2 << 1 =", result)  # Expected: (8 >> 2) << 1 = 2 << 1 = 4

print("\n")

# 7. Bitwise AND `&`
print("Bitwise AND:")
result = 5 & 3
print("5 & 3 =", result)  # Expected: 1 (binary: 0101 & 0011 = 0001)

print("\n")

# 8. Bitwise XOR `^`
print("Bitwise XOR:")
result = 5 ^ 3
print("5 ^ 3 =", result)  # Expected: 6 (binary: 0101 ^ 0011 = 0110)

print("\n")

# 9. Bitwise OR `|`
print("Bitwise OR:")
result = 5 | 3
print("5 | 3 =", result)  # Expected: 7 (binary: 0101 | 0011 = 0111)

print("\n")

# 10. Comparison Operators `<`, `<=`, `>`, `>=`, `==`, `!=`
print("Comparison Operators:")
result = 5 < 3
print("5 < 3 =", result)  # Expected: False

result = 5 == 5
print("5 == 5 =", result)  # Expected: True

print("\n")

# 11. Identity Operators `is`, `is not`
print("Identity Operators:")
a = 5
b = 5
result = a is b
print("a is b =", result)  # Expected: True, since integers are cached in Python

print("\n")

# 12. Membership Operators `in`, `not in`
print("Membership Operators:")
lst = [1, 2, 3]
result = 2 in lst
print("2 in [1, 2, 3] =", result)  # Expected: True

print("\n")

# 13. Logical NOT `not`
print("Logical NOT:")
result = not (5 > 3)
print("not (5 > 3) =", result)  # Expected: False

print("\n")

# 14. Logical AND `and`
print("Logical AND:")
result = 5 > 3 and 3 > 1
print("5 > 3 and 3 > 1 =", result)  # Expected: True

print("\n")

# 15. Logical OR `or`
print("Logical OR:")
result = 5 > 3 or 3 < 1
print("5 > 3 or 3 < 1 =", result)  # Expected: True

print("\n")

# 16. Combined Example
print("Combined Example with multiple operators:")
result = (5 + 3 * 2) > 8 and not (2 in lst) or 1 << 2 == 4
print("(5 + 3 * 2) > 8 and not (2 in [1, 2, 3]) or 1 << 2 == 4 =", result)
# Expected:
# Step-by-step:
# 1. Multiplication: 3 * 2 = 6
# 2. Addition: 5 + 6 = 11
# 3. Comparison: 11 > 8 = True
# 4. Membership: 2 in [1, 2, 3] = True
# 5. Logical NOT: not True = False
# 6. Left shift: 1 << 2 = 4
# 7. Comparison: 1 << 2 == 4 = True
# 8. Logical AND: True and False = False
# 9. Logical OR: False or True = True

print("\n")
