import csv
import numpy as np

# Real_Estate_Sales_2001-2022_GL-Short.csv - NumPy Assignment


sale_amount_list = []
assessed_value_list = []

with open("Real_Estate_Sales_2001-2022_GL-Short.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        try:
            assessed_value_list.append(float(row[5]))
            sale_amount_list.append(float(row[6]))
        except (ValueError, IndexError):
            continue

sale_amount = np.array(sale_amount_list, dtype=float)
assessed_value = np.array(assessed_value_list, dtype=float)

print("sale amount:", sale_amount)
print("assessed value:", assessed_value)

# statistics operation on real estate
print("Real Estate sale amount average:", np.average(sale_amount))
print("Real Estate sale amount mean:", np.mean(sale_amount))
print("Real Estate sale amount median:", np.median(sale_amount))
print("Real Estate sale amount standard:", np.std(sale_amount))
print("Real Estate sale amount percentile - 45:", np.percentile(sale_amount, 45))
print("Real Estate sale amount percentile - 25:", np.percentile(sale_amount, 25))
print("Real Estate sale amount percentile - 35:", np.percentile(sale_amount, 35))
print("Real Estate sale amount absolute value:", np.abs(sale_amount))
print("Real Estate sale amount maximum:", np.max(sale_amount))
print("Real Estate sale amount minimum:", np.min(sale_amount))

# math operation on real estate
print("Real Estate sale amount square root:", np.sqrt(np.abs(sale_amount)))
print("Real Estate sale amount square:", np.square(sale_amount))
print("Real Estate sale amount power:", np.power(sale_amount, 2))
print("Real Estate sale amount abs:", np.abs(sale_amount))

# perform basic arithmetic operation
addition = sale_amount + assessed_value
subtraction = sale_amount - assessed_value
division = sale_amount / assessed_value
multiplication = sale_amount * assessed_value

print("Real Estate - sale amount - assessed value - addition:", addition)
print("Real Estate - sale amount - assessed value - subtraction:", subtraction)
print("Real Estate - sale amount - assessed value - division:", division)
print("Real Estate - sale amount - assessed value - multiplication:", multiplication)

# trigonometric function
pi = (sale_amount / np.pi) + 1

# applying sin, cos, tan
sin_values = np.sin(pi)
cos_values = np.cos(pi)
tan_values = np.tan(pi)

print("Real Estate sale amount - div - pie - Sin values:", sin_values)
print("Real Estate sale amount - div - pie - cos values:", cos_values)
print("Real Estate sale amount - div - pie - tan values:", tan_values)

print("Real Estate sale amount - div - pie - exponential values:", np.exp(pi))

# calculate the log and base-10 log
positive_pi = np.abs(pi) + 1e-10

log_array = np.log(positive_pi)
log10_array = np.log10(positive_pi)

print("Real Estate sale amount - div - pie - log values:", log_array)
print("Real Estate sale amount - div - pie - Base-10 log values:", log10_array)

# hyperbolic sin
sinh = np.sinh(pi)
print("Real Estate sale amount - div - pie - hyperbolic Sin values:", sinh)

# hyperbolic cos
cosh = np.cosh(pi)
print("Real Estate sale amount - div - pie - hyperbolic cos values:", cosh)

# hyperbolic tan
tanh = np.tanh(pi)
print("Real Estate sale amount - div - pie - hyperbolic tan values:", tanh)

# inverse hyperbolic sin
asinh = np.arcsinh(pi)
print("Real Estate sale amount - div - pie - inverse hyperbolic Sin values:", asinh)

# inverse hyperbolic cos
acosh = np.arccosh(np.abs(pi) + 1)
print("Real Estate sale amount - div - pie - inverse hyperbolic Cos values:", acosh)

# real estate 2-dimensional array
D2saleassessed = np.array([sale_amount, assessed_value])

print("Real Estate sale amount and assessed value - 2 dimensional array:", D2saleassessed)

# dimension of array
print("Real Estate - 2 Dimension array - dimension of array:", D2saleassessed.ndim)

# total number of elements / shape
print("Real Estate - 2 Dimension array - shape of array:", D2saleassessed.shape)

# total size of array
print("Real Estate - 2 Dimension array - total size of array:", D2saleassessed.size)

# data type of array
print("Real Estate - 2 Dimension array - data type of array:", D2saleassessed.dtype)

# slicing of array
D2saleassessedslice = D2saleassessed[0:2, :2]
print("Real Estate - 2 Dimension array - slicing of array:", D2saleassessedslice)

D2saleassessedslice2 = D2saleassessed[:1, 3:5]
print("Real Estate - 2 Dimension array - slicing of array:", D2saleassessedslice2)

# indexing array
D2saleassesseditem = D2saleassessed[0, 3]
print("Real Estate - 2 Dimension array - indexing of array:", D2saleassesseditem)

D2saleassesseditem2 = D2saleassessed[0, 4]
print("Real Estate - 2 Dimension array - indexing of array:", D2saleassesseditem2)

# nditer
for elem in np.nditer(D2saleassessed):
    print(elem)

# ndenumerate
for index, elem in np.ndenumerate(D2saleassessed):
    print(index, elem)

# 2 x 142 = 284 elements -> 1 x 284
D2saleassessedTO284 = np.reshape(D2saleassessed, (1, 284))

print(
    "Real Estate sale amount Plus assessed value - 2 dimensional array - reshape:",
    D2saleassessedTO284
)
print("Real Estate reshape - size:", D2saleassessedTO284.size)
print("Real Estate reshape - ndim:", D2saleassessedTO284.ndim)
print("Real Estate reshape - shape:", D2saleassessedTO284.shape)

print()
