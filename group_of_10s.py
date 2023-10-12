numbers = list(map(int, input().split(", ")))

new_list = []
copy_list = numbers.copy()
highest_number = max(numbers)

if highest_number % 10 == 0:
    total_groups = highest_number // 10
else:
    total_groups = highest_number // 10 + 1


for group in range(1, total_groups + 1):
    current_group = group * 10
    new_list.clear()
    for number in copy_list:
        if number <= current_group and number in numbers:
            add_number = numbers.pop(numbers.index(number))
            new_list.append(add_number)

    print(f"Group of {current_group}'s: {new_list}")

    