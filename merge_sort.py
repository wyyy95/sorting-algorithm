def merge_sort(alist):
    if len(alist) == 1:
        return alist
    mid = len(alist) // 2   # 分为两部分，并分别对其进行归并排序
    left_sorted_li = merge_sort(alist[:mid])
    right_sorted_li = merge_sort(alist[mid:])
    # 合并排序（需要分别进行遍历）
    left, right = 0, 0
    merge_sorted_li = []
    left_n = len(left_sorted_li)  # 代码优化，否则在while内每次都要求取长度
    right_n = len(right_sorted_li)
    while left < left_n and right < right_n:
        if left_sorted_li[left] <= right_sorted_li[right]:
            merge_sorted_li.append(left_sorted_li[left])
            left += 1
        else:
            merge_sorted_li.append(right_sorted_li[right])
            right += 1
    """循环结束代表超出限制，得把剩余的内容追加进去"""
    merge_sorted_li.extend(left_sorted_li[left:])  # 不用比较，直接切片添加进去，必有一个是空列表
    merge_sorted_li.extend(right_sorted_li[right:])
    return merge_sorted_li

m = merge_sort([36,65,97,76,12,27,49])
print(m)

