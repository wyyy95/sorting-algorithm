def shell_sort(alist):
    n = len(alist)
    gap = n // 2  # 每次折半取
    while gap >= 1:  # 控制gap步长（gap要不断缩短）
        for i in range(gap, n):  # 外循环控制的是所有子序列中的所有元素
            # i = [gap,gap+1,gap+2,...,n]
            j = i
            # 内循环控制的是每个子序列的插入排序
            while j > 0:     # 走到头的时候,就结束
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2
    return alist

m = shell_sort([41,59,31,25,55,35,49])
print(m)
