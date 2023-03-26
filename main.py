def file_input():
    filename = "/Users/tix/Documents/cm1/input"
    row_matrix = []
    with open(filename, "r") as file:
        size = int(file.readline())
        accuracy = float(file.readline())
        for i in range(size):
            row_matrix.append(list(map(float, file.readline().split())))
        free_row = list(map(float, file.readline().split()))
    return row_matrix, free_row, accuracy


def console_input():
    size = int(input("Введите размер матрицы "))
    flag = True
    while flag:
        if size > 20:
            print("Размер должен не превышать 20")
            size = int(input("Введите размер матрицы "))
            continue
        flag = False
    accuracy = float(input("Введите точность"))
    print("Введите коэффициенты в матрице")
    row_matrix = []
    free_row = []
    for i in range(size):
        row_input = input(f"Введите значения строки {i + 1} через пробел: ")
        console_row = list(map(float, row_input.split()))
        if len(console_row) != size:
            print("Ошибка: количество значений в строке не соответствует количеству столбцов.")
            exit()
        row_matrix.append(console_row)
    print("Введите вектор свободных членов СЛАУ")

    free_row = list(map(float, input().split()))
    return row_matrix, free_row, accuracy


def simple_iteration_method(A, b, epsilon):
    n = len(A)
    print(n)
    # проверяем на диагональное преобладание
    for i in range(n):
        row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= row_sum:
            # меняем строчки пока его не достигнем
            for j in range(i + 1, n):
                if abs(A[j][i]) > abs(A[i][i]):
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    break
            else:
                print("Плохая матрица(")
                return None
    x = [0] * n
    x_new = [0] * n
    k = 0
    while True:
        k += 1
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if all(abs(x_new[i] - x[i]) < epsilon for i in range(n)):
            return x_new, k
        x = x_new.copy()
        error = [abs(x_new[i] - x[i]) for i in range(n)]
        print("Вектор погрешностей:", error)

input_type = -1

while input_type != 1 and input_type != 0:
    input_type = int(input("Введите 1 если ввод будет через консоль \nВведите 0 если будет файловый ввод\n"))
if input_type == 1:
    matrix, free, accuracy = console_input()
else:
    matrix, free, accuracy = file_input()
ans, k = simple_iteration_method(matrix, free, accuracy)
print("ответ: " + str(ans))
print("количество итераций = " + str(k))

