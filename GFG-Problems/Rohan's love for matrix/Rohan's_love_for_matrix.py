class Solution:
    def firstElement (self, n):
        # code here 
        mod = 1000000007
        # Function to perform matrix multiplication
        def matrix_multiply(A, B):
            result = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        result[i][j] += A[i][k] * B[k][j]
                        result[i][j] %= mod
            return result

    # Function to calculate matrix exponentiation using the exponentiation by squaring algorithm
        def matrix_exponentiation(A, n):
            result = [[1, 0], [0, 1]]  # Initialize result as the identity matrix
            base = A
            while n > 0:
                if n % 2 == 1:
                    result = matrix_multiply(result, base)
                base = matrix_multiply(base, base)
                n //= 2
            return result
            
        A = [[1, 1], [1, 0]]
        result_matrix = matrix_exponentiation(A, n)

        # Retrieve the value of a10 mod 1000000007
        a10_mod = result_matrix[1][0]
        return a10_mod

