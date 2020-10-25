#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.__version__)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))

v = np.random.randint(20, size =(2, 3, 5))

#c = np.random.choice([3, 5, 7, 9], size=(2, 3, 5))

#d = np.random.random_sample((2,3,5))

#e = np.random.rand(2,3,5)
#f = np.random.seed(1234)

#4. Print a.
print(a)
#print(d)

#print(c)
#print(v)
#print(e)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.random.randint(1,2, size =(5, 2, 3))

f = np.ones((5,2,3))

#6. Print b.

print(b)
#print(f)

#7. Do a and b have the same size? How do you prove that in Python code?

print(a.shape == b.shape)
print(a.shape , b.shape)

#8. Are you able to add a and b? Why or why not?

#a + b
#ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3)
# not the same structure

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b,(1, 2, 0))
print(a.shape ,c.shape)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = np.add(a,c)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
#print(d)

#12. Multiply a and c. Assign the result to e.

print(np.multiply(a,c))

#13. Does e equal to a? Why or why not?

#because c is an array just of "1"


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
print(d)
d_mean= np.mean(d)
d_min = np.min(d)
d_max = np.max(d)
print( d_mean, d_min, d_max)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))

#16 y 17
x= np.copy(f)

x = [np.where(( d > d_min) & (d < d_mean), 25, \
              np.where(( d > d_mean) & (d < d_max), 75, \
                       np.where(( d == d_mean), 50 , \
                                np.where(( d == d_min), 0 ,100))))]
print(x)

# ya no supe como hacer para sustituir f empty
