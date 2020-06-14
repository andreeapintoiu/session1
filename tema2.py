# 1. Reverse the order of the items in an array.
# Example:
# a = [1, 2, 3, 4, 5]
# Result:
# a = [5, 4, 3, 2, 1]
print("Ex.1")
a = [1, 2, 3, 4, 5]
print(a)
a.reverse()
print(a)

# 2. Get the number of occurrences of var b in array a.
# Example:
# a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
# b = 2
# Result:
# 4
print("Ex.2")
a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
b = 2
c = a.count(b)
print(c)

# 3. Given a sentence as string, count the number of words in it.
# Example:
# a = 'ana are mere si nu are pere'
# Result:
# 7
print("Ex.3")
a = 'ana are mere si nu are pere'
b = a.split()
print(b)
print(len(b))



