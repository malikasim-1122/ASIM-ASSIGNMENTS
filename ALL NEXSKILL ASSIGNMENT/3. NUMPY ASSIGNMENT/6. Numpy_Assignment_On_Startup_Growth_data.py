import numpy as np

# startup_growth_investment_data.csv - NumPy Assignment

investment, funding_rounds = np.genfromtxt(
    "startup_growth_investment_data.csv",
    delimiter=",",
    skip_header=1,
    usecols=(3, 2),
    unpack=True,
    encoding="utf-8",
    dtype=float
)

print("investment:", investment)
print("funding rounds:", funding_rounds)

# statistics operation on startup data
print("Startup investment average:", np.average(investment))
print("Startup investment mean:", np.mean(investment))
print("Startup investment median:", np.median(investment))
print("Startup investment standard:", np.std(investment))
print("Startup investment percentile - 45:", np.percentile(investment, 45))
print("Startup investment percentile - 25:", np.percentile(investment, 25))
print("Startup investment percentile - 35:", np.percentile(investment, 35))
print("Startup investment absolute value:", np.abs(investment))
print("Startup investment maximum:", np.max(investment))
print("Startup investment minimum:", np.min(investment))

# math operation on startup data
print("Startup investment square root:", np.sqrt(np.abs(investment)))
print("Startup investment square:", np.square(investment))
print("Startup investment power:", np.power(investment, 2))
print("Startup investment abs:", np.abs(investment))

# perform basic arithmetic operation
addition = investment + funding_rounds
subtraction = investment - funding_rounds
division = investment / funding_rounds
multiplication = investment * funding_rounds

print("Startup - investment - funding rounds - addition:", addition)
print("Startup - investment - funding rounds - subtraction:", subtraction)
print("Startup - investment - funding rounds - division:", division)
print("Startup - investment - funding rounds - multiplication:", multiplication)

# trigonometric function
pi = (investment / np.pi) + 1

# applying sin, cos, tan
sin_values = np.sin(pi)
cos_values = np.cos(pi)
tan_values = np.tan(pi)

print("Startup investment - div - pie - Sin values:", sin_values)
print("Startup investment - div - pie - cos values:", cos_values)
print("Startup investment - div - pie - tan values:", tan_values)

print("Startup investment - div - pie - exponential values:", np.exp(pi))

# calculate the log and base-10 log
positive_pi = np.abs(pi) + 1e-10

log_array = np.log(positive_pi)
log10_array = np.log10(positive_pi)

print("Startup investment - div - pie - log values:", log_array)
print("Startup investment - div - pie - Base-10 log values:", log10_array)

# hyperbolic sin
sinh = np.sinh(pi)
print("Startup investment - div - pie - hyperbolic Sin values:", sinh)

# hyperbolic cos
cosh = np.cosh(pi)
print("Startup investment - div - pie - hyperbolic cos values:", cosh)

# hyperbolic tan
tanh = np.tanh(pi)
print("Startup investment - div - pie - hyperbolic tan values:", tanh)

# inverse hyperbolic sin
asinh = np.arcsinh(pi)
print("Startup investment - div - pie - inverse hyperbolic Sin values:", asinh)

# inverse hyperbolic cos
acosh = np.arccosh(np.abs(pi) + 1)
print("Startup investment - div - pie - inverse hyperbolic Cos values:", acosh)

# startup 2-dimensional array
D2investmentfunding = np.array([investment, funding_rounds])

print("Startup investment and funding rounds - 2 dimensional array:", D2investmentfunding)

# dimension of array
print("Startup - 2 Dimension array - dimension of array:", D2investmentfunding.ndim)

# total number of elements / shape
print("Startup - 2 Dimension array - shape of array:", D2investmentfunding.shape)

# total size of array
print("Startup - 2 Dimension array - total size of array:", D2investmentfunding.size)

# data type of array
print("Startup - 2 Dimension array - data type of array:", D2investmentfunding.dtype)

# slicing of array
D2investmentfundingslice = D2investmentfunding[0:2, :2]
print("Startup - 2 Dimension array - slicing of array:", D2investmentfundingslice)

D2investmentfundingslice2 = D2investmentfunding[:1, 3:5]
print("Startup - 2 Dimension array - slicing of array:", D2investmentfundingslice2)

# indexing array
D2investmentfundingitem = D2investmentfunding[0, 3]
print("Startup - 2 Dimension array - indexing of array:", D2investmentfundingitem)

D2investmentfundingitem2 = D2investmentfunding[0, 4]
print("Startup - 2 Dimension array - indexing of array:", D2investmentfundingitem2)

# You should use the builtin function nditer,
# if you don't need to have the indexes values.
for elem in np.nditer(D2investmentfunding):
    print(elem)

# if you need index as tuple 2d table
for index, elem in np.ndenumerate(D2investmentfunding):
    print(index, elem)

# 2 x 5000 ========>>>>> 1 x 10000 - reshape
D2investmentfundingTO10000 = np.reshape(D2investmentfunding, (1, 10000))

print(
    "Startup investment Plus funding rounds - 2 dimensional array - reshape:",
    D2investmentfundingTO10000
)
print(
    "Startup investment Plus funding rounds - reshape - size:",
    D2investmentfundingTO10000.size
)
print(
    "Startup investment Plus funding rounds - reshape - ndim:",
    D2investmentfundingTO10000.ndim
)
print(
    "Startup investment Plus funding rounds - reshape - shape:",
    D2investmentfundingTO10000.shape
)

print()
