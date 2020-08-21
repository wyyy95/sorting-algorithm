def bubble(alist):
    '''冒泡排序要排序n个数，由于每遍历一趟只排好一个数字，则需要遍历n-1趟，所以最外层循环是要循环n-1次，
    而每次趟遍历中需要比较每归位的数字，则要在n-1次比较中减去已排好的i位数字，则第二层循环要遍历是n-1-i次'''
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist

m = bubble([1,4,2,14,7,3,5,62])
print(m)
