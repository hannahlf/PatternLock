from itertools import permutations
# permutations of "123"
p = permutations("123")
for i in p:
    print(i)
print()

# permutations of 2 elements in "123"
p = permutations("123",2)
for i in p:
    print(i)

# --------------------------------------------------------------

# list comprehensive 
# generate a list in one line of code 
a = [i for i in range(5)]
print(a)

b = [(i,j) for i,j in permutations("123",2)]
print(b)

c = {i:(i,i+1) for i in range(3)}
for key in c:
    print(key,c[key])

# join elements in a list 
a = ['1','2','3']
print(''.join(a))
print()

p = permutations("123")
for i in p:
    print(''.join(i))

# --------------------------------------------------------------

# string
a = "465789321"

# find if 65 in a
if "65" in a:
    print(True)
    
# find index of 57 in a
if a.index("57") == 2:
    print(True)

# slice elements in a after index 3 (including 3)
print(a[3:])

# slice elements in a before index 4 (not including 4)
print(a[:4])

# --------------------------------------------------------------

# str() and int()
print("integer 1 to string " + str(1))
print(1+int("3"))

# sum()
print(sum(range(10)))
