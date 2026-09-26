import csv
import numpy as np

# FastFoodRestaurants (3).csv - NumPy Assignment
# Error-free version.
#
# IMPORTANT:
# This CSV contains commas inside some quoted address/website fields.
# np.genfromtxt() can misread those rows, so csv.reader is used only
# for safely reading the CSV. The actual data processing is done with NumPy.

latitude_list = []
longitude_list = []

with open("FastFoodRestaurants (3).csv", "r", encoding="utf-8", newline="") as file:
    csv_data = csv.reader(file)
    next(csv_data)  # skip header

    for row in csv_data:
        try:
            latitude_list.append(float(row[4]))
            longitude_list.append(float(row[5]))
        except (ValueError, IndexError):
            continue

latitude = np.array(latitude_list, dtype=float)
longitude = np.array(longitude_list, dtype=float)

print("latitude:", latitude)
print("longitude:", longitude)

# statistics operation on Fast Food Restaurants
print("Fast Food latitude average:", np.average(latitude))
print("Fast Food latitude mean:", np.mean(latitude))
print("Fast Food latitude median:", np.median(latitude))
print("Fast Food latitude standard:", np.std(latitude))
print("Fast Food latitude percentile - 45:", np.percentile(latitude, 45))
print("Fast Food latitude percentile - 25:", np.percentile(latitude, 25))
print("Fast Food latitude percentile - 35:", np.percentile(latitude, 35))
print("Fast Food latitude absolute value:", np.abs(latitude))
print("Fast Food latitude maximum:", np.max(latitude))
print("Fast Food latitude minimum:", np.min(latitude))

# math operation on Fast Food Restaurants
print("Fast Food latitude square root:", np.sqrt(np.abs(latitude)))
print("Fast Food latitude square:", np.square(latitude))
print("Fast Food latitude power:", np.power(latitude, 2))
print("Fast Food latitude abs:", np.abs(latitude))

# perform basic arithmetic operation
addition = latitude + longitude
subtraction = latitude - longitude
division = latitude / longitude
multiplication = latitude * longitude

print("Fast Food - latitude/longitude - addition:", addition)
print("Fast Food - latitude/longitude - subtraction:", subtraction)
print("Fast Food - latitude/longitude - division:", division)
print("Fast Food - latitude/longitude - multiplication:", multiplication)

# trigonometric function
pi = (latitude / np.pi) + 1

# applying sin, cos, tan
sin_values = np.sin(pi)
cos_values = np.cos(pi)
tan_values = np.tan(pi)

print("Fast Food latitude - div - pie - Sin values:", sin_values)
print("Fast Food latitude - div - pie - cos values:", cos_values)
print("Fast Food latitude - div - pie - tan values:", tan_values)

print("Fast Food latitude - div - pie - exponential values:", np.exp(pi))

# calculate the log and base-10 log
positive_pi = np.abs(pi) + 1e-10

log_array = np.log(positive_pi)
log10_array = np.log10(positive_pi)

print("Fast Food latitude - div - pie - log values:", log_array)
print("Fast Food latitude - div - pie - Base-10 log values:", log10_array)

# hyperbolic sin
sinh = np.sinh(pi)
print("Fast Food latitude - div - pie - hyperbolic Sin values:", sinh)

# hyperbolic cos
cosh = np.cosh(pi)
print("Fast Food latitude - div - pie - hyperbolic cos values:", cosh)

# hyperbolic tan
tanh = np.tanh(pi)
print("Fast Food latitude - div - pie - hyperbolic tan values:", tanh)

# inverse hyperbolic sin
asinh = np.arcsinh(pi)
print("Fast Food latitude - div - pie - inverse hyperbolic Sin values:", asinh)

# inverse hyperbolic cos
acosh = np.arccosh(np.abs(pi) + 1)
print("Fast Food latitude - div - pie - inverse hyperbolic Cos values:", acosh)

# Fast Food 2-dimensional array
D2latlong = np.array([latitude, longitude])

print("Fast Food latitude/longitude - 2 dimensional array:", D2latlong)

# dimension of array
print("Fast Food - 2 Dimension array - dimension of array:", D2latlong.ndim)

# total number of elements in array
print("Fast Food - 2 Dimension array - shape of array:", D2latlong.shape)

# total size of array
print("Fast Food - 2 Dimension array - total size of array:", D2latlong.size)

# data type of array
print("Fast Food - 2 Dimension array - data type of array:", D2latlong.dtype)

# slicing of array
D2latlongslice = D2latlong[0:2, :2]
print("Fast Food - 2 Dimension array - slicing of array:", D2latlongslice)

D2latlongslice2 = D2latlong[:1, 3:5]
print("Fast Food - 2 Dimension array - slicing of array:", D2latlongslice2)

# indexing array
D2latlongitem = D2latlong[0, 3]
print("Fast Food - 2 Dimension array - indexing of array:", D2latlongitem)

D2latlongitem2 = D2latlong[0, 4]
print("Fast Food - 2 Dimension array - indexing of array:", D2latlongitem2)

# You should use the builtin function nditer,
# if you don't need to have the indexes values.
for elem in np.nditer(D2latlong):
    print(elem)

# if you need index as tuple 2d table
for index, elem in np.ndenumerate(D2latlong):
    print(index, elem)

# 2 x 10000 ========>>>>> 1 x 20000 - reshape
D2latlongTO20000 = np.reshape(D2latlong, (1, 20000))

print(
    "Fast Food latitude Plus longitude - 2 dimensional array - reshape:",
    D2latlongTO20000
)
print(
    "Fast Food latitude Plus longitude - reshape - size:",
    D2latlongTO20000.size
)
print(
    "Fast Food latitude Plus longitude - reshape - ndim:",
    D2latlongTO20000.ndim
)
print(
    "Fast Food latitude Plus longitude - reshape - shape:",
    D2latlongTO20000.shape
)

print()
