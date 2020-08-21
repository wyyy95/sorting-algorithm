def select(alist):
    for i in range(len(alist)):   # 总共需要循环len(alist)次
        min = i                   # 当前第‘1’(i)个数为最小值
        for j in range(i+1,len(alist)):  # 每一趟都是比较当前alist[i]与后面的数大小
            if alist[min] > alist[j]:
                min = j
        alist[min], alist[i] = alist[i], alist[min]
    return alist

m = select([38,65,97,76,13,27,49])
print(m)


m = select([38,65,54,76,13,27,49])
print(m)


