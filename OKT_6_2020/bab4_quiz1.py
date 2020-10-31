first_matrix_input = []
first_matrix_input.append(list(map(int, input().split())))
first_matrix_input.append(list(map(int, input().split())))

# New line
input()

second_matrix_input = []
second_matrix_input.append(list(map(int, input().split())))
second_matrix_input.append(list(map(int, input().split())))

first_times_second_matrix = []
first_times_second_matrix.append(  # Baris pertama
    [first_matrix_input[0][0] * second_matrix_input[0][0] +
     first_matrix_input[0][1] * second_matrix_input[1][0],
     first_matrix_input[0][0] * second_matrix_input[0][1] +
     first_matrix_input[0][1] * second_matrix_input[1][1]])
first_times_second_matrix.append(  # Baris kedua
    [first_matrix_input[1][0] * second_matrix_input[0][0] +
     first_matrix_input[1][1] * second_matrix_input[1][0],
     first_matrix_input[1][0] * second_matrix_input[0][1] +
     first_matrix_input[1][1] * second_matrix_input[1][1]])

print(first_times_second_matrix[0][0], first_times_second_matrix[0][1])
print(first_times_second_matrix[1][0], first_times_second_matrix[1][1])
