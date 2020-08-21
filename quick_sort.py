def quick_sort(alist, start, end):
    if start >= end:
        return
    mid = alist[start]  # 定义基准元素
    left = start
    right = end
    while left < right:  # 下面的两个语句是交替执行的，因为要有一个控制语句
        while left < right and alist[right] >= mid:  # 内部也需要left<right的条件
            right -= 1
        # 循环结束，遇到一个比基准元素小的值，要把它放到left的位置
        alist[left] = alist[right]
        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]
    alist[left] = mid  # 找到了第一个数（基准元素）在最终序列中的位置
    quick_sort(alist, start, left-1)
    quick_sort(alist, left+1, end)
    return alist

m = quick_sort([41,310,31,25,55,35,49],0,6)
print(m)