import numpy as np

# Define matrices using NumPy arrays directly
a = np.array([[1, 0, -3], [2, 2, 9], [0, 1, 5]])
b = np.array([[8], [7], [-2]])

# Print matrices
print("Matrix A:")
print(a)

print("\nMatrix B:")
print(b)

# Try solving the system of linear equations Ax = B
try:
    x = np.linalg.solve(a, b)
    print("\nSolution (x):")
    print(x)
except np.linalg.LinAlgError as e:
    print(f"Error in solving the system: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
