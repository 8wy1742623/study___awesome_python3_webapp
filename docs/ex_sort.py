# python3
# -*- coding: utf-8 -*-

l = [4, 7, 6, 3]
# l -> [3, 4, 6, 7]

# 分解：

# 第一次循环，需要比较三次，最大的数排列到了最后的位置：
# [4, 7, 6, 3] 
# -> [4, 7, 6, 3]
# -> [4, 6, 7, 3]
# -> [4, 6, 3, 7]

# 第二次循环，比较两次，第二大的数，排列到倒数第二的位置：
# -> [4, 6, 3, 7]
# -> [4, 3, 6, 7]

# 第三次循环，比较一次：
# -> [3, 4, 6, 7]

j = 1
while j < len(l):
    for i in range(len(l) - j):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
    j += 1 

print(l)