import numpy as np

x = np.array([3, 4, 5])
y = np.array([4, 9, 7])
print(x+y)

x = np.array([[1, 2], [3, 4]])
x
print(x)
print(x.ndim)
print(x.dtype)
print(np.array([[1, 2], [3.0, 4]]).dtype)
print(np.array([[1, 2], [3, 4]], float).dtype)
print(x.shape)

x = np.array([1, 2, 3, 4])
print(x.sum())

x = np.array([1, 2, 3, 4])
print(np.sum(x))

x = np.array([1, 2, 3, 4, 5, 6])
print('beginning x:\n', x)
x_reshape = x.reshape((2, 3))
print('reshaped x:\n', x_reshape)

print(x_reshape[0, 0])
print(x_reshape[1, 2])

print('x before we modify x_reshape:\n', x)
print('x_reshape before we modify x_reshape:\n', x_reshape)
x_reshape[0, 0] = 5
print('x_reshape after we modify its top left element:\n',
x_reshape)
print('x after we modify top left element of x_reshape:\n', x ,"\n")

print(x_reshape.shape, x_reshape.ndim, x_reshape.T)

print("\n", np.sqrt(x))
print("\n", x**2)
print("\n", x**0.5)

help(np.random.normal)