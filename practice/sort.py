sort_number = 0

def select_sort(origin_items, comp=lambda x, y: x < y):
    global sort_number
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
                sort_number+=1
        items[i], items[min_index] = items[min_index], items[i]
    return items

num_array=[1,5,62,33,12,35,2,6]
new_array=select_sort(num_array)
for i in range(len(new_array)):
    print(new_array[i])

print("算法比较次数：", sort_number)

sort_number=0
def maopao_sort(origin_items, comp=lambda x, y: x > y):
    global sort_number
    items = origin_items[:]
    for i in range(len(items)):
        for j in range(i,len(items)):
            if comp(items[i], items[j]):
                temp=items[i]
                items[i]=items[j]
                items[j]=temp
                sort_number+=1
    return items


new_array2 = maopao_sort(num_array)
for i in range(len(new_array2)):
    print(new_array2[i])

print("算法比较次数：", sort_number)


