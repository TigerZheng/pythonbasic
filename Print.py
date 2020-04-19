
"""
    author ：Tiger Z
    Time   ：2020-4-19 15:03:05
    Comment：
        print() 方法用于打印输出，是python中最常见的一个函数。

        该函数的语法如下：

        print(*objects, sep=' ', end='\n', file=sys.stdout)
        参数的具体含义如下：

        objects --表示输出的对象。输出多个对象时，需要用 , （逗号）分隔。

        sep -- 用来间隔多个对象。

        end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符。

        file -- 要写入的文件对象。
"""
if __name__ == '__main__':
    print('Python')

    age = 18
    print('Age：', age) # print 函数可以打印任意数量的值（value1, value2, …），这些值由逗号分隔。

    # 如果要重新定义分隔符，可以通过 sep 来指定。
    print('age', age, sep='')  # 去掉空格
    print('www', 'python', 'org', sep='.')  # 以 . 分割

    for letter in 'Python':
        print(letter,end='-') # end 默认\n

    """
        默认情况下，print 的输出被发送到标准输出流（sys.stdout）。通过重新定义 file，
        可以将输出发送到不同的流（例如：文件或 sys.stderr）中
    """
    f = open('data.txt', 'w')
    print('I am a Pythonista', file=f)
    f.close()

    """
        相对基本格式化输出采用‘%’的方法，format()功能更强大，该函数把字符串当成一个模板，
        通过传入的参数进行格式化，并且使用大括号‘{}’作为特殊字符代替‘%’
    """
    print('{} {}'.format('hello', 'world'))  # 不带字段
    print('{0} {1}'.format('hello', 'world'))  # 带数字编号
    print('{0} {1} {0}'.format('hello', 'world'))  # 打乱顺序
    print('{1} {1} {0}'.format('hello', 'world'))
    print('{a} {tom} {a}'.format(tom='hello', a='world'))  # 带关键字