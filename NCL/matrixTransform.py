from sympy import Matrix

def matrix_block_transform(matrix_vals, block_text):
    """
    matrix_vals: flat list of 9 values for 3x3 matrix (row-major)
    block_text: 3-letter string
    """
    matrix = Matrix([
        matrix_vals[0:3],
        matrix_vals[3:6],
        matrix_vals[6:9]
    ])
    block = [ord(c.upper()) - ord('A') for c in block_text[:3]]
    vector = Matrix(block)
    result = matrix * vector % 26
    return ''.join(chr(int(n) + ord('A')) for n in result)

# Example usage:
matrix = [
    5, 1, 2,
    1, 1, 7,
    3, 3, 3
]

print(matrix_block_transform(matrix, "SKY"))
