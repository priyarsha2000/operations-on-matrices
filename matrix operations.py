import numpy as np
a=np.array(input('enter first the first matrix:'));
b=np.array(input('enter the second matrix:'));
print 'the first matrix a\n',a
print 'the second matrix b\n',b
add=np.add(a,b)
print'the addition of matrices is:\n',add
sub=np.subtract(a,b)
print'the subtraction of matrices is:\n',sub
div=np.divide(a,b)
print'the division of two matrices is:\n',div
multiply=np.multiply(a,b)
print'the multiplication of two matrices is:\n',multiply
root=np.sqrt(a)
print'the square root of two matrices is:\n',root
dot=np.dot(a,b)
print'the dot product of two matrices is:\n',dot
max=np.amax(a)
print 'the maximum value in a matrix:\n',max
min=np.amin(a)
print'the minimum value of a matrix:\n',min
negative=np.negative(a)
print'the negative of a matrix:\n',negative
average=np.mean(a)
print'the average value of a matrix:\n',average
power=np.power(a,b)
print'the power of a matrix:\n',power
square=np.square(a)
print'the square value of a matrix\n',square
determinant=np.linalg.det(a)
print'the determinant of a matrix\n',determinant
c=np.concatenate((a,b))
print'the concatenation of two matrices\n',c
