# ==========================================
# PART A — PYTHON LISTS
# ==========================================

print("--- PART A: LISTS ---")

# 1. First and Last Element
nums = [3, 1, 4, 1, 5]
print("1.", nums[0], nums[-1])

# 2. Length of List
colors = ['red', 'blue', 'green']
print("2.", len(colors))

# 3. Append Element
colors = ['red', 'blue']
colors.append('yellow')
print("3.", colors)

# 4. Insert Element
fruits = ['apple', 'banana']
fruits.insert(1, 'orange')
print("4.", fruits)

# 5. Remove Element
fruits = ['apple', 'banana', 'grapes']
fruits.remove('banana')
print("5.", fruits)

# 6. Pop Last Element
items = [10, 20, 30]
val = items.pop()
print("6. Popped:", val, "List:", items)

# 7. Check Element Presence
nums = [1, 2, 3, 4]
ans = 3 in nums
print("7.", ans)

# 8. Slicing List
a = [0, 1, 2, 3, 4]
ans = a[2:4]
print("8.", ans)

# 9. Replace Element by Index
a = [5, 10, 15]
a[1] = 12
print("9.", a)

# 10. Count Occurrences
nums = [1, 2, 2, 3, 2]
ans = nums.count(2)
print("10.", ans)


# ==========================================
# PART B — PYTHON TUPLES
# ==========================================

print("\n--- PART B: TUPLES ---")

# 1. Indexing Tuple
t = (10, 20, 30)
print("1.", t[1])

# 2. Length of Tuple
t = ('a', 'b', 'c')
print("2.", len(t))

# 3. Unpack Tuple
t = (4, 5)
x, y = t
print("3.", x, y)

# 4. Check Presence in Tuple
t = ('a', 'b', 'c')
ans = 'b' in t
print("4.", ans)

# 5. Empty Tuple Type
t = ()
print("5.", type(t))

# 6. Concatenate Tuples
t1 = (1, 2)
t2 = (3, 4)
ans = t1 + t2
print("6.", ans)

# 7. Repeat Tuple
t = (7,)
ans = t * 3
print("7.", ans)

# 8. Find Index
t = (1, 2, 3, 2)
ans = t.index(2)
print("8.", ans)

# 9. Count Tuple Elements
t = (1, 2, 3, 2)
ans = t.count(2)
print("9.", ans)

# 10. Single Element Tuple
t = (5,)
print("10.", t)


# ==========================================
# PART C — PYTHON SETS
# ==========================================

print("\n--- PART C: SETS ---")

# 1. Create Set from List
items = [1, 2, 2, 3]
s = set(items)
print("1.", s)

# 2. Add to Set
s = {1, 2, 3}
s.add(4)
print("2.", s)

# 3. Remove from Set
s = {1, 2, 3}
s.remove(2)
print("3.", s)

# 4. Check Presence in Set
s = {1, 3, 5}
ans = 5 in s
print("4.", ans)

# 5. Length of Set
s = {10, 20, 30}
print("5.", len(s))

# 6. Clear Set
s = {1, 2, 3}
s.clear()
print("6.", s)

# 7. Add Only If Missing
s = {'a', 'b'}
if 'c' not in s:
    s.add('c')
print("7.", s)

# 8. Remove Duplicates Using Set
items = ['a', 'a', 'b']
s = set(items)
print("8.", s)

# 9. Set Union
s1 = {1, 2}
s2 = {3, 4}
ans = s1 | s2
print("9.", ans)

# 10. Set Intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
ans = s1 & s2
print("10.", ans)


# ==========================================
# PART D — PYTHON DICTIONARIES
# ==========================================

print("\n--- PART D: DICTIONARIES ---")

# 1. Read Value from Dictionary
d = {'name': 'Ali', 'age': 25}
print("1.", d['name'])

# 2. Add Key-Value Pair
d = {'name': 'Ali'}
d['city'] = 'Lahore'
print("2.", d)

# 3. Change Value
d = {'name': 'Ali', 'age': 25}
d['age'] = 30
print("3.", d)

# 4. Delete Key
d = {'name': 'Ali', 'age': 25, 'city': 'Lahore'}
del d['age']
print("4.", d)

# 5. Check Key Existence
d = {'name': 'Ali', 'age': 25}
ans = 'salary' in d
print("5.", ans)

# 6. Print All Keys
d = {'a': 1, 'b': 2}
print("6.", d.keys())

# 7. Print All Values
d = {'a': 1, 'b': 2}
print("7.", d.values())

# 8. Loop Through Dictionary
d = {'x': 10, 'y': 20}
print("8. Pairs:")
for k, v in d.items():
    print(k, "->", v)

# 9. Safe Get Method
d = {}
ans = d.get('score', 0)
print("9.", ans)

# 10. Dictionary from Two Lists
keys = ['a', 'b']
values = [1, 2]
ans = dict(zip(keys, values))
print("10.", ans)
