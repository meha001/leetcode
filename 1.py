def identity_matrix(n):
    """Создает единичную матрицу размера n x n"""
    data = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return Matrix(n, n, data)

def zero_matrix(rows, cols):
    """Создает нулевую матрицу"""
    return Matrix(rows, cols)

def matrix_from_list(lst, rows, cols):
    """Создает матрицу из списка"""
    if len(lst) != rows * cols:
        raise ValueError("Неверная длина списка для матрицы")
    
    data = [lst[i*cols:(i+1)*cols] for i in range(rows)]
    return Matrix(rows, cols, data)

# Примеры использования дополнительных функций
print("Единичная матрица 3x3:")
print(identity_matrix(3))

print("\nНулевая матрица 2x3:")
print(zero_matrix(2, 3))