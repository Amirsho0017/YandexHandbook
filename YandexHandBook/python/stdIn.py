from sys import stdin
import json

records = {1: "First",
           2: "Second",
           3: "Third"}
with open("output.json", "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)

with open("data.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
records[1]["group_number"] = 2
with open("data.json", "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)

with open("data.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
print(records)

with open("output_3.txt", "w", encoding="UTF-8") as file_out:
    print("Вывод в файл с помощью функции print()", file=file_out)

lines = ["Это первая строка\n", "А вот и вторая\n", "И третья — последняя\n"]
with open("output_2.txt", "w", encoding="UTF-8") as file_out:
    file_out.writelines(lines)

with open("output_1.txt", "w", encoding="UTF-8") as file_out:
    n = file_out.write("Это первая строка\nА вот и вторая\nИ третья — последняя\n")
print(n)

with open('input.txt', encoding='UTF-8') as file_in:
    lines = file_in.readlines()
print(lines)

file_in = open('input.txt', encoding='UTF-8')
print(file_in.read().rstrip('\n'))

# lines = stdin.read()
# print([lines])
#
# lines = stdin.readlines()
# print(lines)
