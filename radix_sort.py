def radix_sort(alist):
    i = 0  # 记录当前正在拿第一位，最低位为1
    max_num = max(alist)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list = [[] for _ in range(10)]  # 初始化桶数组,桶编号为0~9
        for num in alist:
            bucket_list[int(num / (10**i) % 10)].append(num)  # 找到位置放入桶数组
        alist.clear()    # 清除，为下面放入新（经过一次排序后）的数组做准备
        for x in bucket_list:   # 将桶数组中的数放回原数组中
            for y in x:
                alist.append(y)
        i += 1
    return alist


m = radix_sort([51,7,12,336,2,67,16,552])
print(m)