import numpy as np
a = [10, 20, 30, 40]

print(a)
npar = np.array(a)
print(npar)

ar = np.ones(10)
print(ar)

ar = np.ones((5,4))
print(ar)
# help(np.ones)

ar = np.ones((5,4), dtype = 'int')
print(ar)

ar = np.ones((5,4)) * 10
print(ar)

ar = np.zeros((5,4), dtype = 'int')
print(ar)

ar = np.zeros(5)  #this gives int values
print(ar)

a = np.eye(3)
print(f"a :{a}", end="\n\n")

a = np.eye(3) * 5
print(f"a :\n{a}", end="\n\n")

a = np.diag([12, 6, 7, 8])
print(f"a :\n{a}", end="\n\n")

a = np.diag([12, 6, 7, 8]) * 2
print(f"a :\n{a}", end="\n\n")

r = np.arange(1, 10)
a = np.diag(r)
print(f"a :\n{a}", end="\n\n")

r = np.arange(1, 17).reshape(4, 4)
print(r)
a = np.diag(r)
print(f"a :\n{a}", end="\n\n")

r = np.arange(1, 17).reshape(4, 4)
print(r)
a = np.diag(r)
print(f"a :\n{a}", end="\n\n")

a = np.random.random(10)
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(10, 100)
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(10, 100, size=5)
print(f"a :\n{a} type :{type(a)}", end="\n\n")

a = np.random.random(10)
print(f"a values:\n{a}", end="\n\n")
a = np.round(a)
print(f"round values of a :\n{a}", end="\n\n")

a = [10, 20, 30]
print(f"a      :{a}")
print(f"a type :{type(a)}")
print(f"a      :{id(a)}")
print(f"a[0]   :{id(a[0])}")
print(f"a[1]   :{id(a[1])}")
print(f"a[2]   :{id(a[2])}")

print(f"10     :{id(10)}")
print(f"20     :{id(20)}")
print(f"30     :{id(30)}")
print()

a = np.array([10, 20, 30])
print(f"a      :{a}")
print(f"a type :{type(a)}")
print(f"a      :{id(a)}")
print(f"a[0]   :{id(a[0])}")

print(f"a[1]   :{id(a[1])}")

print(f"a[2]   :{id(a[2])}")
print(f"10     :{id(10)}")
print(f"20     :{id(20)}")
print(f"30     :{id(30)}")
print()

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(11, 20).reshape(3, 3)

c = a * b
print(f"c :\n{c}", end="\n\n")

a = np.random.randint(1, 10, size = 3)
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(1, 10, size = (5,5))
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(1, 10, size = (2,5))
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(1, 10, size = (1,1))
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(1, 10, size = (1,5))
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(50, 100, size = (8, 8))
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(10, 30, size=10)
print(f"a :\n{a}", end="\n\n")

a = np.sort(a)
print(f"a sort:\n{a}", end="\n\n")

# a = np.sort(a, order=reversed)
# print(f"a sort:\n{a}", end="\n\n")

a = np.random.randint(50, 100, size = (8, 8))
a.sort(axis=0)
print(f"a :\n{a}", end="\n\n")

# print(help(a.sort))
a = np.random.randint(50, 100, size = (8, 8))
# a.sort(axis=0,order="reversed")
# print(f"a :\n{a}", end="\n\n")

a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])
print(f"a :\n{a}", end="\n\n")
a.sort(order='y')
print(f"a :\n{a}", end="\n\n")

a = np.random.randint(10, 90, size=10)
print(a)

print(a>30)
print(a[a>30])

# vstack stacking np array n x m and n x m = 2n x m
# vstack n x m and n x m = 2n x m
a = np.random.randint(10, 90, size=(5,5))
b = np.random.randint(10, 90, size=(5,5))
print(a)
print(b)
c = np.vstack((a, b))
print(c)

# vstack stacking np array m x n and p x n array m+p x n
# vstack n x m and p x m = n+p x m
a = np.random.randint(10, 90, size=(5,5))
b = np.random.randint(10, 90, size=(4,5))
print(a)
print(b)
c = np.vstack((a, b))
print(c)
print()

print()

# hstack stacking np array n x m and n x m  = n+n x m
# hstack n x m and n x m = n x 2m
a = np.random.randint(10, 90, size=(5,5))
b = np.random.randint(10, 90, size=(5,5))
print(a)
print(b)
c = np.hstack((a, b))
print(c)

# vstack stacking np array m x n and m x p array
# hstack n x m and m x p = n x m+p
a = np.random.randint(10, 90, size=(5,5))
b = np.random.randint(10, 90, size=(5,4))
print(a)
print(b)
c = np.hstack((a, b))
print(c)

# vstack n x m and n x m = 2n x m
# vstack n x m and p x m = n+p x m
# hstack n x m and n x m = n x 2m
# hstack n x m and m x p = n x m+p

print()
a = np.random.randint(1, 9, size=5)
b = np.random.randint(10, 90, size=(5,5))
print(a)
print(b)
c = np.column_stack((a, b))
print(c)

print()
a = np.random.randint(1, 9, size=5)
b = np.random.randint(10, 90, size=(5,4))
print(a)
print(b)
c = np.column_stack((a, b))
print(c)

print()
a = np.random.randint(1, 9, size=5)
b = np.random.randint(10, 90, size=(5,5))
print(a)
print(b)
c = np.row_stack((a, b))
print(c)

print()
a = np.random.randint(1, 9, size=5)
b = np.random.randint(10, 90, size=(4,5))
print(a)
print(b)
c = np.row_stack((a, b))
print(c)

# hstack vstack concatenation row_stack column_stack
# np.hsplit np.vsplit

print()
a = np.random.randint(10, 90, size=(8,4))

print(a)
c, d = np.hsplit(a, 2)
print(c)
print(d)
print()

c, d, e, f = np.hsplit(a, 4)
print(c)
print(d)
print(e)
print(f)
print()

print()
a = np.random.randint(10, 90, size=(8,4))

print(a)
c, d = np.vsplit(a, 2)
print(c)
print(d)
print()

c, d, e, f = np.hsplit(a, 4)
print(c)
print(d)
print(e)
print(f)
print()
