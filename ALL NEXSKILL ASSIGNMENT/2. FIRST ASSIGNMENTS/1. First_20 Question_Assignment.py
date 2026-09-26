# ==========================================
# PART 1: BEGINNER LEVEL
# ==========================================

print("--- PART 1 ---")

# 1. Length
s = "hello world"
ans = len(s)
print("1.", ans)

# 2. Upper and Lower
s = "Python3"
u = s.upper()
l = s.lower()
print("2.", u, l)

# 3. Count
s = "banana"
ans = s.count("a")
print("3.", ans)

# 4. First and Last
s = "drawer"
f = s[0]
e = s[-1]
print("4.", f, e)

# 5. Check word
s = "data science"
ans = "science" in s
print("5.", ans)

# 6. Slice
s = "programming"
ans = s[3:8]
print("6.", ans)

# 7. Reverse
s = "Python"
ans = s[::-1]
print("7.", ans)

# 8. Replace
s = "I love apples. Apples are great!"
ans = s.replace("apples", "oranges")
print("8.", ans)

# 9. Split and Join
s = "split this sentence"
w = s.split()
ans = "-".join(w)
print("9.", ans)

# 10. Strip
s = " padded text "
ans = s.strip()
print("10.", ans)


# ==========================================
# PART 2: INTERMEDIATE LEVEL
# ==========================================

print("\n--- PART 2 ---")

# 1. Vowels and Consonants
s = "Hello, World! 123"
v = 0
c = 0
for x in s.lower():
    if x.isalpha():
        if x in "aeiou":
            v = v + 1
        else:
            c = c + 1
print("1. Vowels:", v, "Consonants:", c)

# 2. Palindrome
s = "A man, a plan, a canal: Panama!"
cl = ""
for x in s.lower():
    if x.isalnum():
        cl = cl + x
ans = cl == cl[::-1]
print("2.", ans)

# 3. Title Case
s = "hELLO wORLD from PYTHON"
w = s.split()
res = []
for x in w:
    t = x[0].upper() + x[1:].lower()
    res.append(t)
ans = " ".join(res)
print("3.", ans)

# 4. Find Indices
s = "aaaa"
sub = "aa"
ind = []
for i in range(len(s) - len(sub) + 1):
    if s[i : i + len(sub)] == sub:
        ind.append(i)
print("4.", ind)

# 5. Frequency
s = "Baa Baa Black Sheep"
d = {}
for x in s.lower():
    if x != " ":
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
print("5.", d)

# 6. Anagram
s1 = "Listen"
s2 = "Silent"
l1 = []
for x in s1.lower():
    if x.isalpha():
        l1.append(x)
l2 = []
for x in s2.lower():
    if x.isalpha():
        l2.append(x)
l1.sort()
l2.sort()
ans = l1 == l2
print("6.", ans)

# 7. Compress
s = "aaabbcaaaa"
res = ""
ch = s[0]
cnt = 1
for i in range(1, len(s)):
    if s[i] == ch:
        cnt = cnt + 1
    else:
        res = res + ch + str(cnt)
        ch = s[i]
        cnt = 1
res = res + ch + str(cnt)
print("7.", res)

# 8. Longest Word
s = "Find the longest_word here!"
w = s.split()
long = ""
for x in w:
    cl = ""
    for char in x:
        if char.isalpha():
            cl = cl + char
    if len(cl) > len(long):
        long = cl
print("8.", long)

# 9. Remove Duplicates
s = "banana"
cl = ""
for x in s:
    if x not in cl:
        cl = cl + x
print("9.", cl)

# 10. Mask Email
s = "malikasimaslam786@gmail.com"
p = s.split("@")
name = p[0]
dom = p[1]
stars = "*" * (len(name) - 2)
ans = name[0] + stars + name[-1] + "@" + dom
print("10.", ans)
