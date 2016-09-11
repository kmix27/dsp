# Matrix Algebra
A = [[1,2,3],[2,7,4]]
B = [[1,-1],[0,1]]
C = [[5,-1],[9,1],[6,0]]
D = [[3,-2,-1],[1,2,3]]
u = [6,2,-3,5]
v= [3,5,-1,4]
w = [[1],[2],[0],[5]]

print('1. Matrix dimensions (Rank)')
import sympy


def findRank(matrix):
	x = sympy.Matrix(matrix).rref()
	return len(x[1])

print('1.1 Rank A:')
print(findRank(A))

print('1.2 Rank B:')
print(findRank(B))

print('1.3 Rank C:')
print(findRank(C))

print('1.4 Rank D:')
print(findRank(D))

print('1.5 Rank u:')
print(findRank(u))

print('1.6 Rank v:')
print(findRank(v))

print('2. Vector Operations')
print('2.1 u + v:')
addition_uv = [a+b for a,b in  zip(u,v)]
print(addition_uv)

print('2.2 u - v :')
subtraction_uv = [a-b for a,b in zip(u,v)]
print(subtraction_uv)

print('2.3 αu:')
alpha = 6
scaled_u = [item * alpha for item in u]
print(scaled_u)

print('2.4 u · v:')
multElements = [u*v for u,v in zip(u,v)]
dotProduct = sum(multElements)
print(dotProduct)

print('2.5 ||u|| :')
square = [item **2 for item in u]
norm_u = sum(square)**.5
print(norm_u)

print('3. Matrix Operations')
print('3.1 A + C: ')
def addMatrix(m1,m2):
	x = sympy.Matrix(m1)
	y = sympy.Matrix(m2)
	if x.cols != y.cols:
		print('Undefined')
	else:
		addition = x + y
		print(addition)
addMatrix(A,C)

print('3.2 A - C^T: ')
def threeTwo():
	x = sympy.Matrix(A)
	y = sympy.Matrix(C).T
	print(x - y)
threeTwo()

print('3.3 C^T + 3D:')
def threeThree():
	x = sympy.Matrix(C).T
	y = sympy.Matrix(D) * 3
	print(x + y)
threeThree()

print('3.4 BA:')
def multMatrix(m1,m2):
	x = sympy.Matrix(m1)
	y = sympy.Matrix(m2)
	if x.cols == y.rows:
		print(x*y)
	else:
		print('Undefined')
	# else:
		# print(x * y)
multMatrix(B,A)

print('3.5 BA^T:')
def multMatrixTm2(m1,m2):
	x = sympy.Matrix(m1)
	y = sympy.Matrix(m2).T
	if x.cols == y.rows:
		print(x*y)
	else:
		print('undefined')
multMatrixTm2(B,A)

print('3.6 BC:')
multMatrix(B,C)

print('3.7 CB: ')
multMatrix(C,B)

print('3.8 B^4: ')
x =sympy.Matrix(B)
print(x**4)

print('3.9 AA^T: ')
multMatrixTm2(A,A)

print('3.10 D^TD: ')
def multMatrixTm1(m1,m2):
	x = sympy.Matrix(m1).T
	y = sympy.Matrix(m2)
	if x.cols == y.rows:
		print(x*y)
	else:
		print('Undefined')
multMatrixTm1(D,D)
