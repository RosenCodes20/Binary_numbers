num = int(input())
current_num = num
nums_list = []
while True:
    current_num //= 2
    new_num = current_num % 2
    nums_list.append(new_num)
    if current_num <= 1:
        break

nums_list.reverse()
nums_list.append(num % 2)
print("".join(map(str, nums_list)))
