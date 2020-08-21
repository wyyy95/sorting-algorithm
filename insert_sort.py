def insert_sort(alist):
    for i in range(1,len(alist)):  # 总共需要这么多趟
        for j in range(i, 0, -1):  # 从后往前插入，j = [i,i-1,i-2,...1]
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:     # 如果后一个数不小于前一个数，那就不用交换，跳过
                break
    return alist

m = insert_sort([36,56,87,76,12,37])
print(m)


