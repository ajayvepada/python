z = 3 + 4j
print(z)
print(type(z))
print(z.real)
print(z.imag)
# Here using operators
a = 2 + 3j
b = 3 + 4j
print(a + b)# addition
print(a-b)#subtraction
print(a*b)#multiplication
print(a/b)#division
c = 3 + 5j
print(abs(z))# return the magnitude value of complex number
print(z.conjugate())# return the conjugate of complex number
import cmath
d = 1 + 2j
print(cmath.phase(d))#getting the phase(angle) of the complex number
print(cmath.polar(z))#getting the polar form of the complex number(magnitude,angle)
print(cmath.sqrt(z))#getting the square root of complex number