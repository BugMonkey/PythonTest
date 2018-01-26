# python 笔记
# list 有序集合 类似list
_list = ['1', 'a']

# tuple  元组 类似数组
_tuple = {1, 'a'}

#  dic  字典  类似map
_dic = {'a': 1, 'b': 2}

#  set  无序不重复集合，过滤重复
_set = ([1, 1, 2, 2, 3, 3])


# 函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


a = my_abs(2018 - 1966)
print(a)


# 可变参数用*表示，参数长度不一定
def my_test_more(*x):
    size = len(x)
    if size > 0:
        n = 0
        _sum = 0

        while n < size:
            _sum = _sum + int(x[n])
            n = n + 1

        return _sum
    else:
        return x


c = my_test_more(10, 35)
print(c)


# 关键字参数用**kw表示,该参数可选,kw 是dict  字典（类似map）
def my_test_muti(a, b, **kw):
    print('a', a, 'b', b, 'other{', kw, '}')
    return 0


city = my_test_muti(1, 2, c='Beijing', d='nanjing')

# 另一种写法
extra = {'city': 'Beijing', 'job': 'Engineer'}

city3 = my_test_muti(2, 3, **extra)


# 命名关键字参数 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

def my_test_muti2(a, b, *, job, adress):
    print('a', a, 'b', b, 'other{job', job, 'adress:', adress, '}')
    return 0


# 只接收city和job作为关键字参数。这种方式定义的函数如下：

city2 = my_test_muti2(1, 2, job='工人', adress='工厂')

''' 参数组合在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数或关键字参数。数量不确定的参数只可存在一个
 比如可变参数和关键字参数
 '''


#   必选参数、默认参数、可变参数、关键字参数
def f1(a, b, c=0, *d, **e):
    pass


#   必选参数、默认参数、命名关键字参数、关键字参数
def f2(a, b, c=0, *, d, **kw):
    pass


#   递归的尾递归写法：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact_iter(num, product):
    if num == 1:
        return product
    else:
        # return n * fact(n - 1)  使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的
        # 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
        return fact_iter(num - 1, num * product)


# 切片操作，用于取出list或tuple指定范围的数
'''L[index_start:index_end : step]  
   index_start开始索引，如果开始为0可省略 ，可为负数表示倒数第几个 
   index_end 结束索引，如果为最后一个可省略
   step 步长表示每隔step取'''


def since_test():
    L = list(range(100))
    # 取前十个
    result1 = L[10:]
    # 取后十个
    result2 = L[-10:]
    # 取第十个和倒数第十个之间每5个取一个
    result3 = L[10:-10:5]
    print(str(result1) + '\n' + str(result2) + '\n' + str(result3))
    pass


since_test()

# 切片操作的例子

''' 用循环实现的去空操作'''


def trim(a):
    if (len(a) > 0):
        global result
        i = 0
        b = a
        while (i < len(a) and a[i] == ' '):
            i = i + 1
            b = a[i:]

        result = b
        j = 1
        while (j < len(b) and b[-j] == ' '):
            result = b[:-j]
            j = j + 1

        return result
    else:
        return a


''' 有时循环可以用递归代替更好，如下'''


def trim2(a):
    if (len(a) > 0):
        if (a[0] == ' '):
            return trim(a[1:])
        elif (a[-1] == ' '):
            return trim(a[:-1])
        else:
            return a
    else:
        return a

    # 测试:' hello'


if trim2('  hello') != 'hello':
    print('测试失败!')
elif trim2('  hello  ') != 'hello':
    print('测试失败!')
elif trim2('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim2('') != '':
    print('测试失败!')
elif trim2(' ') != '':
    print('测试失败!')
else:
    print('测试成功!')

# 迭代
'''在Python中，迭代是通过for ... in来完成的
  isinstance('abc', Iterable)来判断是否可以迭代
'''


# 选出list中最大最小
def findMinAndMax(L):
    max = None
    min = None
    if (isinstance(L, list)):
        for index1, value1 in enumerate(L):
            if (max == None):
                max = value1
            elif (min == None):
                min = value1
            else:
                if (max < value1):
                    max = value1
                if (min > value1):
                    min = value1
    return ({'min:': min, 'max:': max})


print(findMinAndMax([1, 19, 66, 9, 1, 20, 67]))

#    列表生成式
'''   
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，for 循环后可以跟 条件语句
[x * x for x in range(1, 11) if x % 2 == 0]


'''
L = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L if (isinstance(s, str))])

# 生成器 generator 如果列表元素可以按照某种算法推算出来,可以使用

'''
1、（x * x for x in range(1, 11)）
generator的每一个元素通过next（）函数打印出来 next(g) next(g) next(g)... generator也是可迭代对象所以使用for 来迭代它
'''

g1 = (x for x in range(10))
for x, y in enumerate(g1):
    print('生成器 generator:', x, y)

'''
2、  如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
'''


def fib(n):
    a, b, n = 1, 0, 0
    if (n > 0):
        a, b = b, a + b


# 迭代器 凡是可作用于for循环的对象都是Iterable类型；
'''
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的
'''
