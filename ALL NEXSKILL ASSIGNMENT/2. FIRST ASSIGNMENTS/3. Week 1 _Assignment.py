# ==========================================
# WEEK 1 — ASSIGNMENT NO 1
# ==========================================

# Question 1: Celsius to Fahrenheit
print("--- Question 1 ---")
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)


# Question 2: Calculate Area of a Rectangle
print("\n--- Question 2 ---")
l = float(input("Enter length: "))
w = float(input("Enter width: "))
area = l * w
print("Area of Rectangle:", area)


# Question 3: Calculate Compound Interest
print("\n--- Question 3 ---")
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
ci = p * (1 + r/100)**t - p
print("Compound Interest:", ci)


# Question 4: Perimeter of a Rectangle
print("\n--- Question 4 ---")
l = float(input("Enter length: "))
w = float(input("Enter width: "))
peri = 2 * (l + w)
print("Perimeter of Rectangle:", peri)


# Question 5: Average of Three Numbers
print("\n--- Question 5 ---")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
avg = (n1 + n2 + n3) / 3
print("Average:", avg)


# Question 6: Square and Cube of a Number
print("\n--- Question 6 ---")
num = float(input("Enter a number: "))
sq = num ** 2
cube = num ** 3
print("Square:", sq)
print("Cube:", cube)


# Question 7: Distribute Items Equally
print("\n--- Question 7 ---")
candies = int(input("Enter total candies: "))
students = int(input("Enter total students: "))
each = candies // students
left = candies % students
print("Each student gets:", each)
print("Candies left over:", left)


# Question 8: Calculate Profit or Loss
print("\n--- Question 8 ---")
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    profit = sp - cp
    print("Profit amount:", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss amount:", loss)
else:
    print("No Profit No Loss")


# Question 9: Total Marks and Percentage
print("\n--- Question 9 ---")
m1 = float(input("Subject 1 marks: "))
m2 = float(input("Subject 2 marks: "))
m3 = float(input("Subject 3 marks: "))
m4 = float(input("Subject 4 marks: "))
m5 = float(input("Subject 5 marks: "))
total = m1 + m2 + m3 + m4 + m5
per = (total / 500) * 100
avg_marks = total / 5
print("Total Marks:", total)
print("Percentage:", per)
print("Average Marks:", avg_marks)


# Question 10: Salary Calculator
print("\n--- Question 10 ---")
basic = float(input("Enter basic salary: "))
hra = 0.20 * basic
da = 0.15 * basic
total_salary = basic + hra + da
print("Total Salary:", total_salary)
