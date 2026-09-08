# 1
data = [5, 11, 23, 11, 40, 11, 11, 50, 11]
print(f" Кол-во элементов 11 в списке: {data.count(11)}")
data.sort()
del data[1:6]
print(f" Список после удаления 11 {data}")

# 2
s = "py20thon300is50cool"
buff_str = ""
sum = 0
for char in s:
    if char.isdigit():
        buff_str += char
    else:
        if buff_str != "":
            sum += int(buff_str)
            buff_str = ""
if buff_str != "":
    sum += int(buff_str)

print(f"Сумма чисел в строке {sum}")
print()
# 3
my_company = dict(
    name="TechCorp",
    departments=["IT", "HR"]
)
print(f"ID {id(my_company.get('departments'))}")

my_company["departments"].append("Sales")
print(f"ID {id(my_company.get('departments'))}")

for key in my_company.items():
    print(f"Ключи: {key}")
for value in my_company.values():
    print(f"Значение: {value}")
print()
# 4.1
# keys_list = ["id", "status", "level"]
# values_list = [105, "active", 3]
# empty_list = dict(zip(keys_list, values_list))
#
# for key, value in empty_list.items():
#     print(f"{key}: {value}")
# 4.2

keys_list = ["id", "status", "level"]
values_list = [105, "active", 3]
empty_list = {}
for key, value in zip(keys_list, values_list):
    print(f"{key} : {value}")
