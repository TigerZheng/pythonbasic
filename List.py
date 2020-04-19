"""
    author ：Tiger Z
    Time   ：2020-4-19 15:02:12
    Comment：
"""

if __name__ == '__main__':

    #define list
    demo_list = [1, True,'two','string',4,5,6,7,8]

    # access element by index 索引
    print(demo_list[0])

    #Cut 切片
    print(demo_list[1:5])
    print(demo_list[:5])
    print(demo_list[4:7])
    print(demo_list[-5:-1])
    print(demo_list[-5:])

    # 加
    templist = ['one','two','three']
    print(demo_list)
    print(demo_list+templist)

    # 乘
    print(demo_list*2)

    # 检查成员
    print(True in demo_list)
    print(True not in demo_list)

    #在列表末尾添加新的对象
    demo_list.append(300)
    print(demo_list)

    #统计某个元素在列表中出现的次数
    print(demo_list.count(4))

    #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    demo_list.extend(templist)
    print(demo_list)

    #从列表中找出某个值第一个匹配项的索引位置
    print(demo_list.index(1))

    #将对象插入列表
    demo_list.insert(0, 600)
    print(demo_list)

    #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    print(demo_list.pop(0))
    print(demo_list)

    #移除列表中某个值的第一个匹配项
    print(demo_list.remove(1))
    print(demo_list)

    #反向列表中元素
    demo_list.reverse()
    print(demo_list)

    # #对原列表进行排序 list.sort(key=None, reverse=False)
    # key - - 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    # reverse - - 排序规则，reverse = True 降序， reverse = False 升序（默认）。
    random = [(2, 2), (3, 4), (4, 1), (1, 3)]
    random.sort(reverse=False)
    print(random)

    takeSecond = lambda elem:elem[1] # 获取列表的第二个元素
    random.sort(key=takeSecond ,reverse=False)
    print(random)

    #复制列表
    random = demo_list.copy()
    print(random)
    #清空列表
    demo_list.clear()
    print(demo_list)
