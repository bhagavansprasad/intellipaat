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

