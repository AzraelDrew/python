'''
 $ @Author       : yznaisy
 $ @Date         : 2020-09-04 10:22:22
 $ @LastEditors  : yznaisy
 $ @LastEditTime : 2020-11-03 11:49:21
'''
# s="*"
# for i in range(1,10,2):
#     print(((s+" ")*i).center(18))    //设置字符长度让其居中，其余用空格填充
# for i in reversed(range(1,8,2)):    //反转
#     print(((s+" ")*i).center(18))

# s="*"
# for i in range(1,10,2):
#     print(" ".join((s*i)).center(18))
# for i in reversed(range(1,8,2)):
#     print(" ".join((s*i)).center(18))

rows = int(input('请输入菱形边长：\n'))
row = 1
while row <= rows:
    col = 1  # 保证每次内循环col都从1开始，打印前面空格的个数
    while col <= (rows - row):  # 这个内层while就是单纯打印空格
        print(' ', end='')  # 空格的打印不换行
        col += 1
    print(row * '* ')  # 每一行打印完空格后，接着在同一行打印星星，星星个数与行数相等，且打印完星星后print默认换行
    row += 1

bottom = rows - 1
while bottom > 0:
    col = 1  # 保证每次内循环col都从1开始，打印前面空格的个数
    while bottom + col <= rows:
        print(' ', end='')  # 空格的打印不换行
        col += 1
    print(bottom * '* ')  # 每一行打印完空格后，接着在同一行打印星星，星星个数与行数相等，且打印完星星后print默认换行
    bottom -= 1


# str="1234"
# print(str.center(20))
# print("+".join(str))
