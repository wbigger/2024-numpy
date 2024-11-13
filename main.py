import numpy as np

a1 = np.array([1,2,3])
print("a1",a1)

a2 = np.linspace(0,100,21)
print("a2",a2)

a3 = np.zeros(10)
print("a3",a3)

a4 = np.ones(12)
print("a4",a4)

np.random.seed(18)
r1 = np.random.rand(2,3)
print("r1",r1)

r2 = r1.reshape(3,2)
print("r2",r2)
