def find_insert_position(sorted_list, val):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= val:
            return i
    return len(sorted_list)

my_list = [10, 20, 30, 40, 50]
new_val = 25

pos = find_insert_position(my_list, new_val)
print("Відсортований список:", my_list)
print(f"Позиція для вставки числа {new_val}: index =", pos)

my_list.insert(pos, new_val)
print("Список після вставки:", my_list)