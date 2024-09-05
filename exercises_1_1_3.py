import numpy as np

# Define matrices using NumPy arrays directly
a = np.array([[1, 5], [1, -2]])
b = np.array([[7], [-2]])

# Print matrices
print("Matrix A:")
print(a)

print("\nMatrix B:")
print(b)

# Solve the system of linear equations Ax = B
x = np.linalg.solve(a, b)

# Print the solution
print("\nSolution (x):")
print(x)
