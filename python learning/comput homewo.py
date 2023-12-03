# import math
#
# n = int(input('请输入循环次数'))
# for i in range(n):
#     r = int(input('请输入您要求的圆形半径：'))  # 用户输入半径的值
#     if r < 0:
#         print('请输入正数！')  # 如果输入负数，提醒用户输入正数
#     else:
#         s = math.pi * r ** 2  # 利用圆的面积公式计算面积
#         s = round(s, 2)  # 保留两位小数，使得结果更加简洁
#         print('圆的面积是：', s)  # 输出保留两位小数后的面积
#         break

# a, b, c = map(int, input('请输入a,b,c:').split())
# print('a,b,c中最大的值为：', max(a, b, c))


def I_made_max(a, b, c):
    d = a
    if b > d:
        d = b
    if c > d:
        d = c
    return d


a, b, c = map(int, input('请输入a,b,c:').split())
print('a,b,c中最大的值为：', I_made_max(a, b, c))
