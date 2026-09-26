import numpy as np

price , street , city , bed =np.genfromtxt ("RealEstate-USA (3).csv" , delimiter="," , skip_header=1 , usecols=(2,4,6,8) , unpack=True , encoding=None , dtype=int)
print("price:", price)
print("street:", street)
print("city:", city)
print("state:", bed)

print(np.max(price))

# statistics operation on realestate 
print("Real Estate.com price average:", np.average(price))
print("Real Estate.com price mean:" , np.mean(price))
print("Real Estate.com price median:", np.median(price))
print("Real Estate.com price standard:" , np.std(price))
print("Real Estate.com price percentile - 45:", np.percentile(price,45))
print("Real Estate.com price percentile  - 25:" ,np.percentile(price,25))
print("Real Estate.com price percentile  - 35:", np.percentile(price,35))
print("Real Estate.com price absolute value:" , np.abs(price))
print("Real Estate.com price maximum:" , np.max(price))
print("Real Estate.com price minimum:" , np.min(price))

# math operation on realestate.com

print("Real Estate.com price square root:" , np.sqrt(price))
print("Real Estate.com price square:", np.square(price))
print("Real Estate.com price power" , np.power(price , price))
print("Real Estate.com price abs:" , np.abs(price))


# perform basic arthematic operation 

addition = price + bed
substraction = price - bed
division = price / bed
multiplication = price * bed

print("Real Estate.com - bath - addition:", addition)
print("Real Estate.com - bath - substracton :" , substraction)
print("Real Estate.com - bath - division:" , division)
print("Real Estate.com - bath - multiplication :" , multiplication)


# trignometic funtion on realestate
pi = (price / np.pi) + 1

# applying sin ,cos ,tan
sin_values = np.sin(pi)
cos_values = np.cos(pi)
tan_values = np.tan(pi)

print("Realestate.com price - div - pie  - Sin values:" , sin_values)
print("Realestate.com price - div - pie  - cos values:" , cos_values)
print("Realestate.com price - div - pie  - tan values:" , tan_values)

print("Realestate.com price - div - pie  - exponential values:" , np.exp(pi))

# calculate the log and base-10 log

log_array = np.log(pi)
log10_array = np.log(pi)

print("Realestate.com price - div - pie  - log values:" , log_array)
print("Realestate.com price - div - pie  - Base-10 log values:" , log10_array)

# hyperbolic sin

sinh = np.sinh(pi)

print("Realestate.com price - div - pie  - hyperbolic Sin values:" , sinh)

# hyperbolic cos

cosh = np.cosh(pi)

print("Realestate.com price - div - pie  - hyperbolic cos values:" , cosh)

# hyperbolic tan

tanh = np.tanh(pi)

print("Realestate.com price - div - pie  - hyperbolic tan values:" , tanh)

# inverse hyperbolic sin

asinh = np.arcsinh(pi)
print("Realestate.com price - div - pie  - inverse hyperbolic Sin values:" , asinh)

# inverse hyperbolic cos 
acosh = np.arccos(pi)
print("Realestate.com price - div - pie  - inverse hyperbolic Sin values:" , acosh)

# realestate 2 - dimentional array

D2pricebed = np.array([price ,
bed])

print("Realestate.com price - div - pie  - 2 dimentional array:", D2pricebed)

# dimension of array
print("Real Estate.com - 2 Dimension array - dimension of array 1:", D2pricebed.ndim)

# total number of element i array

print("Real Estate.com - 2 Dimension array - total number  of array 1:" , D2pricebed.shape)

#  total size of array

print("Real Estate.com - 2 Dimension array - total size of array :" , D2pricebed.size)

# data type of  array

print("Real Estate.com - 2 Dimension array - data type of array:" , D2pricebed.dtype)

# slicing of array

D2pricebedslice = D2pricebed[2:3:1 , :2:1]
print("Real Estate.com - 2 Dimension array  - slicing of array:", D2pricebedslice)
D2pricebedslice2 = D2pricebed[:1 , 3:5:3]
print("Real Estate.com - 2 Dimension array  - slicing of array:", D2pricebedslice2)

# indexing array
D2pricebeditem = D2pricebed[0 , 3]
print("Real Estate.com - 2 Dimension array  - indexing of array:", D2pricebeditem)
D2pricebeditem2 = D2pricebed[0 , 4]
print("Real Estate.com - 2 Dimension array  - indexing of array:" , D2pricebeditem2)

#You should use the builtin function nditer, if you don't need to have the indexes values.

for elem in np.nditer(D2pricebed):
    print(elem)

# if you need index as tuple 2d table

for index, elem in np.ndenumerate(D2pricebed):
    print(index,elem)

# 2 x 149 ========>>>>> 1  x 400 - reshape
D2pricebedTO400 = np.reshape(D2pricebed , (1 , 400)) 

print("Realestate price Plus bed - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : " , D2pricebedTO400)
print("Realestate price Plus bed - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : size" , D2pricebedTO400.size)
print("Realestate price Plus bed - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim" , D2pricebedTO400.ndim)
print("Realestate price Plus bed - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : shape" , D2pricebedTO400.shape)


print()


