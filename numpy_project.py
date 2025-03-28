import numpy as np

# Function to input a matrix
def input_matrix():
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    
    matrix = []
    print(f"Enter the elements of the matrix row by row:")
    
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    
    return np.array(matrix)

# Function to display a matrix
def display_matrix(matrix):
    print("\nThe matrix is:")
    print(matrix)

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return matrix1 + matrix2
    else:
        print("Matrices must have the same dimensions to add.")
        return None

# Function to subtract two matrices
def subtract_matrices(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return matrix1 - matrix2
    else:
        print("Matrices must have the same dimensions to subtract.")
        return None

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    if matrix1.shape[1] == matrix2.shape[0]:
        return np.dot(matrix1, matrix2)
    else:
        print("Matrices cannot be multiplied due to incompatible dimensions.")
        return None

# Function to transpose a matrix
def transpose_matrix(matrix):
    return np.transpose(matrix)

# Function to calculate the determinant of a matrix
def determinant_matrix(matrix):
    if matrix.shape[0] == matrix.shape[1]:  # Determinant is only defined for square matrices
        return np.linalg.det(matrix)
    else:
        print("Determinant is only defined for square matrices.")
        return None

# Main interactive loop for the Matrix Operations Tool
def matrix_operations_tool():
    print("Welcome to the Matrix Operations Tool!")

    # Input the first matrix
    print("\nInput the first matrix:")
    matrix1 = input_matrix()
    display_matrix(matrix1)

    # Ask user if they want to input a second matrix for operations that require two matrices
    choice = input("\nDo you want to input a second matrix for operations? (yes/no): ").lower()
    if choice == 'yes':
        print("\nInput the second matrix:")
        matrix2 = input_matrix()
        display_matrix(matrix2)

    while True:
        print("\nMatrix Operations Menu:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Transpose Matrix")
        print("5. Determinant of Matrix")
        print("6. Exit")
        
        operation = int(input("Enter the operation number you want to perform: "))
        
        if operation == 1:
            if choice == 'yes':
                result = add_matrices(matrix1, matrix2)
                if result is not None:
                    display_matrix(result)
            else:
                print("Addition requires two matrices.")
        
        elif operation == 2:
            if choice == 'yes':
                result = subtract_matrices(matrix1, matrix2)
                if result is not None:
                    display_matrix(result)
            else:
                print("Subtraction requires two matrices.")
        
        elif operation == 3:
            if choice == 'yes':
                result = multiply_matrices(matrix1, matrix2)
                if result is not None:
                    display_matrix(result)
            else:
                print("Multiplication requires two matrices.")
        
        elif operation == 4:
            print("\nTranspose of Matrix 1:")
            display_matrix(transpose_matrix(matrix1))
            if choice == 'yes':
                print("\nTranspose of Matrix 2:")
                display_matrix(transpose_matrix(matrix2))
        
        elif operation == 5:
            print("\nDeterminant of Matrix 1:", determinant_matrix(matrix1))
            if choice == 'yes':
                print("Determinant of Matrix 2:", determinant_matrix(matrix2))
        
        elif operation == 6:
            print("Exiting the Matrix Operations Tool.")
            break
        
        else:
            print("Invalid operation number. Please try again.")

# Run the tool
matrix_operations_tool()

