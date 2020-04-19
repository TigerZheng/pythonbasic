
"""
    author ：Tiger Z
    Time   ：2020-4-19 15:03:57
    Comment：
        Python 的元组与列表类似，不同之处在于元组的元素不能修改。
        元组使用小括号，列表使用方括号。
        元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
        支持与列表形同的通过Index截取的操作
"""


if __name__ == '__main__':
    tup1 = ('Google', 'Runoob', 1997, 2000);
    tup2 = (1, 2, 3, 4, 5);
    tup3 = "a", "b", "c", "d";  # 不需要括号也可以
    print(type(tup3))
    print(tup3)
    print(tup1)

    tup4 = (50)
    print(type(tup4))  # 不加逗号，类型为整型

    tup4 = (50,)
    print(type(tup4))  # 加上逗号，类型为元组

    tup5 = ()  # 空元组
    print(type(tup5))

    # 元组可以使用下标索引来访问元组中的值
    print("tup1[0]: ", tup1[0])
    print("tup2[1:5]: ", tup2[1:5])

    # 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
    tup6 = tup1 + tup2
    print(tup6)

    # 我们可以使用del语句来删除整个元组
    # del tup6
    # print(tup6)

    # 计算元组元素个数。
    # len(tuple)


    # 返回元组中元素最大值。
    # max(tuple)

    # 返回元组中元素最小值。
    # min(tuple)

    # 将列表转换为元组。
    # tuple(seq)
