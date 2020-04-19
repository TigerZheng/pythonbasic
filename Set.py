
"""
    author ：Tiger Z
    Time   ：2020-4-19 15:04:03
    Comment：
        集合（set）是一个无序的不重复元素序列。
        可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

"""

if __name__ == '__main__':
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)                      # 这里演示的是去重功能
    print('orange' in basket)                 # 快速判断元素是否在集合内
    print('crabgrass' in basket)

    # 下面展示两个集合间的运算.
    a = set('abracadabra')
    print(a)
    b = set('alacazam')
    print(b)

    print(a - b)  # 集合a中包含而集合b中不包含的元素
    print(a | b)  # 集合a或b中包含的所有元素
    print(a & b)  # 集合a和b中都包含了的元素
    print(a ^ b)  # 不同时包含于a和b的元素

    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)

    # add()	为集合添加元素
    thisset = set(("Google", "Runoob", "Taobao"))
    print(thisset)
    thisset.add("JD")
    print(thisset)

    # update()	给集合添加元素 参数可以是列表，元组，字典等
    thisset.update({8,6})
    print(thisset)
    thisset.update([1,2],[3,4])
    print(thisset)

    # remove()	移除指定元素 如果元素不存在，则会发生错误。
    thisset.remove("JD")
    print(thisset)
    # discard()	删除集合中指定的元素 移除集合中的元素，且如果元素不存在，不会发生错误

    # clear()	移除集合中的所有元素
    # copy()	拷贝一个集合
    # difference()	返回多个集合的差集
    # difference_update()	移除集合中的元素，该元素在指定的集合也存在。
    # intersection()	返回集合的交集
    # intersection_update()	返回集合的交集。
    # isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
    # issubset()	判断指定集合是否为该方法参数集合的子集。
    # issuperset()	判断该方法的参数集合是否为指定集合的子集
    # pop()	随机移除元素
    # symmetric_difference()	返回两个集合中不重复的元素集合。
    # symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
    # union()	返回两个集合的并集
